import os
import shutil
import sys

from copycontents import recursive_contents_copy
from gencontents import generate_pages_recursive

base_path = "/"
dir_path_static = "./static"
dir_path_public = "./docs"
dir_path_content = "./content"
template_path = "./template.html"

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

def copy_static_content_to_public():
    # To check if the path exists
    if os.path.exists(dir_path_public):
        print(f"{dir_path_public} exists, deleting contents...")
        delete_folder_contents(dir_path_public)
    else:
        print(f"{dir_path_public} does not exists, creating directory...")
        os.mkdir(dir_path_public)

    recursive_contents_copy(dir_path_static, dir_path_public)


def main():
    if len(sys.argv) > 0:
        base_path = sys.argv[0]

    copy_static_content_to_public()
    generate_pages_recursive(base_path, dir_path_content, template_path, dir_path_public)

if __name__ == "__main__":
    main()
