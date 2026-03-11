import re

from enum import Enum
from htmlnode import HTMLNode
from parentnode import ParentNode
from leafnode import LeafNode
from textnode import TextNode, TextType, text_node_to_html_node
from inline_markdown import text_to_textnodes

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def markdown_to_blocks(markdown):
    blocks = []
    sections = markdown.split("\n\n")

    for section in sections:
        cln_section = section.strip()

        if cln_section != "":
            blocks.append(cln_section)
    
    return blocks

def block_to_block_type(block):
    lines = block.split("\n")

    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    elif len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    elif block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH

        return BlockType.QUOTE
    elif block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH

        return BlockType.UNORDERED_LIST
    elif block.startswith("1. "):
        i = 1

        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH

            i += 1

        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    html_nodes = []

    for node in text_nodes:
        html_nodes.append(text_node_to_html_node(node))
    
    return html_nodes

def markdown_to_html_node(markdown):
    children_htmls = []
    blocks = markdown_to_blocks(markdown)

    for block in blocks:
        # Determine type
        block_type = block_to_block_type(block)

        match block_type:
            case BlockType.PARAGRAPH:
                paragraph_node = ParentNode("p", children=text_to_children(block.replace("\n", " ")))
                children_htmls.append(paragraph_node)
            case BlockType.HEADING:
                hash_count = block.count("#")
                cleaned_block = block.replace("# ", "").replace("#", "").replace("\n", " ")
                heading_node = ParentNode(f"h{hash_count}", children=text_to_children(cleaned_block))
                children_htmls.append(heading_node)
            case BlockType.CODE:
                code_node = TextNode(block.replace("\n", "", 1).strip("`"), TextType.CODE)
                pre_node = ParentNode("pre", children=[text_node_to_html_node(code_node)])
                children_htmls.append(pre_node)
            case BlockType.QUOTE:
                list_nodes = []
                cleaned_block = block.replace("> ", "").replace("\n", " ")
                quote_node = ParentNode("blockquote", children=text_to_children(cleaned_block))
                children_htmls.append(quote_node)
            case BlockType.UNORDERED_LIST:
                list_nodes = []
                lines = block.split("\n")

                for line in lines:
                    list_nodes.append(ParentNode("li", children=text_to_children(line.strip("- "))))
                
                unorder_node = ParentNode("ul", children=list_nodes)
                children_htmls.append(unorder_node)
            case BlockType.ORDERED_LIST:
                list_nodes = []
                lines = block.split("\n")
                i = 1

                for line in lines:
                    list_nodes.append(ParentNode("li", children=text_to_children(line.strip(f"{i}. "))))
                    i += 1
                
                ordered_node = ParentNode("ol", children=list_nodes)
                children_htmls.append(ordered_node)
    
    return ParentNode("div", children=children_htmls)

def block_to_block_type_regex(block):
    headings_pattern = r"#{1,6}\s{1}\w+"
    # code_block_pattern = r"^```(?:\s*(\w+))?([\s\S]*?)```$"
    code_block_pattern = r"^`{3}\n[\w\W\d\D\s\S]+`{3}$"
    quote_pattern = r"^>\s*(.+)$"
    unordered_list_pattern = r"^\s*[-+*]\s+(.+)$"
    ordered_list_pattern = r"^\s*\d+\.\s+(.+)$"

    if re.search(headings_pattern, block):
        return BlockType.HEADING
    elif re.search(code_block_pattern, block):
        return BlockType.CODE
    elif re.search(quote_pattern, block):
        return BlockType.QUOTE
    elif re.search(unordered_list_pattern, block):
        return BlockType.UNORDERED_LIST
    elif re.search(ordered_list_pattern, block):
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH
