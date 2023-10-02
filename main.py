import os
import sys

# Add the current directory to sys.path
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

from app import app as application

if __name__ == "__main__":
    application.run(port=8000)