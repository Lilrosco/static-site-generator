import re

from enum import Enum

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
