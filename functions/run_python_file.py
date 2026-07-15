import os
import subprocess

def run_python_file(working_directory: str, file_path: str, args: list[str] | None = None) -> str:
    try:
        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        absolute_path = os.path.abspath(working_directory)

        full_path = os.path.join(absolute_path, file_path)
        normalized_target_path = os.path.normpath(full_path)

        if not os.path.isfile(normalized_target_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        is_valid_path = os.path.commonpath([absolute_path, normalized_target_path]) == absolute_path
        if not is_valid_path:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        else:
            command = ["python", normalized_target_path]
            if args is not None:
                command.extend(args)
            completed_process = subprocess.run(command, text=True, capture_output=True, timeout=30, cwd=working_directory)
            result = ""
            if completed_process.returncode != 0:
                result += f"Process exited with code {completed_process.returncode}\n"
            if completed_process.stdout is None and completed_process.stderr is None:
                result += "No output produced"
            else:
                result += f"STDOUT: {completed_process.stdout}\n"
                result += f"STDERR: {completed_process.stderr}"
            return result
    except Exception as e:
        return f"Error: executing Python file: {e}"