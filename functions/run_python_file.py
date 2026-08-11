import os
import subprocess


def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    try:
        # Resolve absolute paths
        abs_working_dir = os.path.abspath(working_directory)

        if os.path.isabs(file_path):
            abs_target_path = os.path.abspath(file_path)
        else:
            abs_target_path = os.path.abspath(
                os.path.join(working_directory, file_path)
            )

        # 1. Check if outside permitted working directory
        if os.path.commonpath([abs_working_dir, abs_target_path]) != abs_working_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        # 2. Check if file exists and is a regular file
        if not os.path.isfile(abs_target_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        # 3. Check if file ends with .py
        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        # 4. Build command list
        command = ["python", abs_target_path]
        if args:
            command.extend(args)

        # 5. Run subprocess
        completed_process = subprocess.run(
            command,
            cwd=abs_working_dir,
            capture_output=True,
            text=True,
            timeout=30,
        )

        # 6. Build output string
        output_lines = []

        if completed_process.returncode != 0:
            output_lines.append(
                f"Process exited with code {completed_process.returncode}"
            )

        stdout = completed_process.stdout
        stderr = completed_process.stderr

        if not stdout and not stderr:
            output_lines.append("No output produced")
        else:
            if stdout:
                output_lines.append(f"STDOUT:\n{stdout}")
            if stderr:
                output_lines.append(f"STDERR:\n{stderr}")

        return "\n".join(output_lines)

    except Exception as e:
        return f"Error: executing Python file: {e}"


schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Executes a specified Python file within the working directory and returns its output",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the Python file to run, relative to the working directory",
                },
                "args": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "Optional list of arguments to pass to the Python script",
                },
            },
            "required": ["file_path"],
        },
    },
}
