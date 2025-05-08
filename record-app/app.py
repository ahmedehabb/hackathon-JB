import subprocess
import os

def run_record_sh():
    try:
        # Assuming record.sh is in the same directory as the Python script
        script_path = os.path.join(os.path.dirname(__file__), "record.sh")

        # Ensure the script is executable
        os.chmod(script_path, 0o755)  # Make it executable (rwxr-xr-x)

        # Run the script
        process = subprocess.Popen(
            [script_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            cwd=os.path.dirname(__file__) # Run the script from its own directory
        )

        stdout, stderr = process.communicate()

        if process.returncode == 0:
            print("Script executed successfully:")
            print(stdout.decode())
            return stdout.decode()
        else:
            print("Script execution failed:")
            print(stderr.decode())
            return None

    except FileNotFoundError:
        print("Error: record.sh not found.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None