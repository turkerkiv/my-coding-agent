import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        if os.path.isfile(directory):
            return f'Error: "{directory}" is not a directory'
         
        absolute_path = os.path.abspath(working_directory)

        full_path = os.path.join(absolute_path, directory)
        normalized_target_path = os.path.normpath(full_path)

        is_valid_dir = os.path.commonpath([absolute_path, normalized_target_path]) == absolute_path
        if not is_valid_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        else:
            return f'Success: "{directory}" is within the working directory'
    except:
        return f'Error: unexpected error'