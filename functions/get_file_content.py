import os

MAX_CHARS = 10000


def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        # Resolve absolute paths
        abs_working_dir = os.path.abspath(working_directory)
        
        if os.path.isabs(file_path):
            abs_target_path = os.path.abspath(file_path)
        else:
            abs_target_path = os.path.abspath(os.path.join(working_directory, file_path))

        # 1. Check if the file path is outside the permitted working directory
        if os.path.commonpath([abs_working_dir, abs_target_path]) != abs_working_dir:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        # 2. Check if the path exists and is a regular file
        if not os.path.isfile(abs_target_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        # 3. Read content with truncation check
        with open(abs_target_path, "r", encoding="utf-8") as f:
            content = f.read(MAX_CHARS)
            if f.read(1):
                content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
            return content

    except Exception as e:
        return f"Error: {e}"

schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": f"Retrieves the content (at most {MAX_CHARS} characters) of a specified file within the working directory",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the file to read, relative to the working directory",
                },
            },
            "required": ["file_path"],
        },
    },
}
