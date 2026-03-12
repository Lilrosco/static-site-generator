import os
import shutil

from block_markdown import markdown_to_blocks, markdown_to_html_node

def extract_title(markdown):
    header = None
    blocks = markdown_to_blocks(markdown)

    for block in blocks:
        if block.startswith("# "):
            header = block.replace("# ", "").strip()
            break

    if not header:
        raise ValueError("Header 1 is not found in markdown")

    return header

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    try:
        with open(from_path, 'r') as from_file:
            markdown = from_file.read()
    except FileNotFoundError:
        print(f"Error: The file '{from_path}' was not found.")

    try:
        with open(template_path, 'r') as template_file:
            template = template_file.read()
    except FileNotFoundError:
        print(f"Error: The file '{template_path}' was not found.")

    content = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    html = template.replace("{{ Title }}", title).replace("{{ Content }}", content)

    try:
        with open(dest_path, 'w') as dest_file:
            output = dest_file.write(html)
    except Exception as e:
        print(f"An error occurred when writing file: {e}")

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for filename in os.listdir(dir_path_content):
        file_path = os.path.join(dir_path_content, filename)
        destination_path = os.path.join(dest_dir_path, filename)

        if os.path.isfile(file_path):
            if filename[-3:] == ".md":
                destination_path = os.path.join(dest_dir_path, filename.replace(".md", ".html"))
                generate_page(file_path, template_path, destination_path)
        elif os.path.isdir(file_path):
            print(f"Making sub directory: {destination_path}")
            os.mkdir(destination_path)
            generate_pages_recursive(file_path, template_path, destination_path)
