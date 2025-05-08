import os
import subprocess

def run_record_sh():
    print("Running record.sh script...")
    try:
        # Assuming record.sh is in the same directory as the Python script
        script_path = os.path.join(os.path.dirname(__file__), "record.sh")
        # Ensure the script is executable
        os.chmod(script_path, 0o755)  # Make it executable (rwxr-xr-x)
        print(f"Script path: {script_path}")

        # Get the current environment
        my_env = os.environ.copy()

        # Run the script, passing the environment
        process = subprocess.Popen(
            [script_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            cwd=os.path.dirname(__file__),  # Run the script from its own directory
            env=my_env  # Pass the environment
        )
        print("Script is running...")
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
    
if __name__ == "__main__":
    run_record_sh()