import subprocess
import sys

def main():
    subprocess.run([sys.executable, "-m", "pip", "--version"])
