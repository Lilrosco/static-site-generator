import re

from textnode import TextType, TextNode

VALID_DELIMITERS = {
    "`": TextType.CODE,
    "**": TextType.BOLD,
    "_": TextType.ITALIC
}

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    if delimiter not in VALID_DELIMITERS:
        raise Exception(f"Invalid delimiter: '{delimiter}'")

    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            if node.text.count(delimiter) % 2 != 0:
                raise Exception(f"Missing an opening or closing '{delimiter}'")
            
            sub_nodes = node.text.split(delimiter)
            new_nodes.append(TextNode(sub_nodes[0], TextType.TEXT))

            if len(sub_nodes) > 1:
                # Was able to split on delimiter otherwise it wasn't found
                new_nodes.append(TextNode(sub_nodes[1], text_type))
                new_nodes.append(TextNode(sub_nodes[2], TextType.TEXT))

    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)
