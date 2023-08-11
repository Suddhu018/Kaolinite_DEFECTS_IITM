import subprocess
import sys

def open_with_vesta(file_path):
    try:
        if sys.platform.startswith('darwin'):  # macOS
            subprocess.run(['open', '-a', 'VESTA', file_path])
        elif sys.platform.startswith('win32'):  # Windows
            subprocess.run(['start', 'VESTA', file_path], shell=True)
        elif sys.platform.startswith('linux'):  # Linux
            subprocess.run(['vesta', file_path])
        else:
            raise OSError(f"Unsupported operating system: {sys.platform}")
    except FileNotFoundError:
        print("Vesta application not found.")
    except Exception as e:
        print(f"An error occurred: {e}")



