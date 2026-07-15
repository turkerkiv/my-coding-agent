import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        absolute_path = os.path.abspath(working_directory)

        full_path = os.path.join(absolute_path, directory)
        normalized_target_path = os.path.normpath(full_path)

        if not os.path.isdir(normalized_target_path):
            return f'Error: "{directory}" is not a directory'

        is_valid_path = os.path.commonpath([absolute_path, normalized_target_path]) == absolute_path
        if not is_valid_path:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        else:
            dir_items = []
            for filename in os.listdir(normalized_target_path):
                full_file_path = os.path.join(normalized_target_path, filename)
                dir_items.append(f"- {filename}: file_size={os.path.getsize(full_file_path)} bytes, is_dir={os.path.isdir(full_file_path)}")
            return "\n".join(dir_items)
    except:
        return f'Error: unexpected error'

schema_get_files_info = {
    "type": "function",
    "function": {
        "name": "get_files_info",
        "description": "Lists files in a specified directory relative to the working directory, providing file size and directory status",
        "parameters": {
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}