import os
import shutil

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
