import os
from config import MAX_CHARS

def get_file_content(working_directory: str, file_path: str) -> str:
        try:
            absolute_path = os.path.abspath(working_directory)

            full_path = os.path.join(absolute_path, file_path)
            normalized_target_path = os.path.normpath(full_path)
            
            if not os.path.isfile(normalized_target_path):
                return f'Error: File not found or is not a regular file: "{file_path}"'

            is_valid_path = os.path.commonpath([absolute_path, normalized_target_path]) == absolute_path
            if not is_valid_path:
                return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
            else:
                with open(normalized_target_path, "r") as f:
                    file_content_str = f.read(MAX_CHARS)
                    if f.read(1):
                        file_content_str += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
                return file_content_str
        except Exception as e:
            return f'Error: {e}'