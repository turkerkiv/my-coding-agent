import os

def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        absolute_path = os.path.abspath(working_directory)

        full_path = os.path.join(absolute_path, file_path)
        normalized_target_path = os.path.normpath(full_path)

        if os.path.isdir(normalized_target_path):
            return f'Error: Cannot write to "{file_path}" as it is a directory'

        is_valid_path = os.path.commonpath([absolute_path, normalized_target_path]) == absolute_path
        if not is_valid_path:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        else:
            parents_path = os.path.join(absolute_path, os.path.dirname(file_path))
            os.makedirs(parents_path, exist_ok=True)
            with open(normalized_target_path, "w") as f:
                length_written = f.write(content)
            return f'Successfully wrote to "{file_path}" ({length_written} characters written)'
    except Exception as e:
        return f'Error: {e}'


schema_write_file = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "Writes the specified content to the specified file, relative to the working directory",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "The path of a file that we wanted to overwrite with specified content, relative to the working directory",
                },
                "content": {
                    "type": "string",
                    "description": "The actual content we want to write to a file",
                },
            },
            "required":["file_path", "content"]
        },
    },
}