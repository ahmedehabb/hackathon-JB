import os
import subprocess

def execute_code(request: str) -> str:
    """Executes the code received in the request and returns the output."""
    print("Executing code...")



def execute_python_code(code_string: str) -> str:
    """Executes Python code and returns the output."""
    try:
        process = subprocess.Popen(
            ["python3", "-c", code_string],  # Or "python" depending on your system
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        stdout, stderr = process.communicate(timeout=10)  # Adjust timeout as needed
        if stderr:
            return f"Error: {stderr}"
        else:
            return stdout
    except subprocess.TimeoutExpired:
        return "Error: Code execution timed out."
    except Exception as e:
        return f"Error: {e}"