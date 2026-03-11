import os
import shutil

from block_markdown import BlockType, markdown_to_blocks, markdown_to_html_node

STATIC_DIRECTORY = "./static"
WORKING_DIRECTORY = "./public"

def delete_folder_contents(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                print(f"Deleting File: {file_path}")
                os.unlink(file_path) # Removes file/link
            elif os.path.isdir(file_path):
                print(f"Deleting Sub Directory: {file_path}")
                shutil.rmtree(file_path) # Removes directory
        except Exception as e:
            print(f"Failed to delete {file_path}. Reason: {e}")

def recursive_contents_copy(src_folder, target_folder):
    for filename in os.listdir(src_folder):
        file_path = os.path.join(src_folder, filename)
        destination_path = os.path.join(target_folder, filename)

        try:
            if os.path.isfile(file_path):
                print(f"Copying {file_path} to {destination_path}")
                shutil.copy(file_path, destination_path)

            elif os.path.isdir(file_path):
                print(f"Making Sub Directory: {file_path} to {destination_path}")
                os.mkdir(destination_path)
                recursive_contents_copy(file_path, destination_path)
        except Exception as e:
            print(f"Failed to copy {file_path} to {destination_path}. Reason: {e}")

def copy_static_content_to_public():
    # To check if the path exists
    if os.path.exists(WORKING_DIRECTORY):
        print(f"{WORKING_DIRECTORY} exists, deleting contents...")
        delete_folder_contents(WORKING_DIRECTORY)
    else:
        print(f"{WORKING_DIRECTORY} does not exists, creating directory...")
        os.mkdir(WORKING_DIRECTORY)

    recursive_contents_copy(STATIC_DIRECTORY, WORKING_DIRECTORY)

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
            print(markdown)
    except FileNotFoundError:
        print(f"Error: The file '{from_path}' was not found.")

    try:
        with open(template_path, 'r') as template_file:
            template = template_file.read()
            print(template)
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


def main():
    copy_static_content_to_public()
    generate_page("./content/index.md", "template.html", "./public/index.html")

if __name__ == "__main__":
    main()
