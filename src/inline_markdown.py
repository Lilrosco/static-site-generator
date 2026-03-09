import re

from textnode import TextType, TextNode

VALID_DELIMITERS = {
    "`": TextType.CODE,
    "**": TextType.BOLD,
    "_": TextType.ITALIC
}

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    if delimiter not in VALID_DELIMITERS:
        raise ValueError(f"Invalid delimiter: '{delimiter}'")

    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
        else:
            if old_node.text.count(delimiter) % 2 != 0:
                raise ValueError(f"Missing an opening or closing '{delimiter}'")
            
            sub_nodes = old_node.text.split(delimiter)

            for i in range(len(sub_nodes)):
                if sub_nodes[i] != "":
                    if i % 2 == 0:
                        new_nodes.append(TextNode(sub_nodes[i], TextType.TEXT))
                    else:
                        new_nodes.append(TextNode(sub_nodes[i], text_type))

    return new_nodes

def extract_markdown_images(text):
    pattern = r"!\[(.*?)\]\((.*?)\)"
    return re.findall(pattern, text)

def extract_markdown_links(text):
    pattern = r"\[(.*?)\]\((.*?)\)"
    return re.findall(pattern, text)

def split_nodes_image(old_nodes):
    new_nodes = []

    for old_node in old_nodes:
        original_text = old_node.text
        images = extract_markdown_images(original_text)

        if old_node.text_type != TextType.TEXT or len(images) == 0:
            new_nodes.append(old_node)
        else:
            for image in images:
                img_alt = image[0]
                img_url = image[1]
                sections = original_text.split(f"![{img_alt}]({img_url})", 1)

                if len(sections) != 2:
                    raise ValueError("invalid markdown, image section not closed")
                
                if sections[0] != "":
                    new_nodes.append(TextNode(sections[0], TextType.TEXT))
                
                new_nodes.append(
                    TextNode(img_alt, TextType.IMAGE, img_url)
                )

                original_text = sections[1]
            
            if original_text != "":
                new_nodes.append(TextNode(original_text, TextType.TEXT))

    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []

    for old_node in old_nodes:
        original_text = old_node.text
        links = extract_markdown_links(original_text)

        if old_node.text_type != TextType.TEXT or len(links) == 0:
            new_nodes.append(old_node)
        else:
            for link in links:
                link_text = link[0]
                link_url = link[1]
                sections = original_text.split(f"[{link_text}]({link_url})", 1)

                if len(sections) != 2:
                    raise ValueError("invalid markdown, link section not closed")
                
                if sections[0] != "":
                    new_nodes.append(TextNode(sections[0], TextType.TEXT))
                
                new_nodes.append(
                    TextNode(link_text, TextType.LINK, link_url)
                )

                original_text = sections[1]
            
            if original_text != "":
                new_nodes.append(TextNode(original_text, TextType.TEXT))

    return new_nodes

def text_to_textnodes(text):
    text_nodes = [TextNode(text, TextType.TEXT)]

    text_nodes = split_nodes_delimiter(text_nodes, "**", TextType.BOLD)
    text_nodes = split_nodes_delimiter(text_nodes, "_", TextType.ITALIC)
    text_nodes = split_nodes_delimiter(text_nodes, "`", TextType.CODE)
    text_nodes = split_nodes_image(text_nodes)
    text_nodes = split_nodes_link(text_nodes)

    return text_nodes
