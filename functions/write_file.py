import os


def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        # Resolve absolute paths
        abs_working_dir = os.path.abspath(working_directory)

        if os.path.isabs(file_path):
            abs_target_path = os.path.abspath(file_path)
        else:
            abs_target_path = os.path.abspath(
                os.path.join(working_directory, file_path)
            )

        # 1. Check if file path is outside permitted working directory
        if os.path.commonpath([abs_working_dir, abs_target_path]) != abs_working_dir:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        # 2. Check if the target is an existing directory
        if os.path.isdir(abs_target_path):
            return f'Error: Cannot write to "{file_path}" as it is a directory'

        # 3. Ensure parent directories exist
        parent_dir = os.path.dirname(abs_target_path)
        if parent_dir:
            os.makedirs(parent_dir, exist_ok=True)

        # 4. Write content to the file
        with open(abs_target_path, "w", encoding="utf-8") as f:
            f.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f"Error: {e}"


schema_write_file = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "Writes text content to a specified file within the working directory (overwriting if the file exists)",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the file to write, relative to the working directory",
                },
                "content": {
                    "type": "string",
                    "description": "Text content to write to the file",
                },
            },
            "required": ["file_path", "content"],
        },
    },
}
