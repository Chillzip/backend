import sys
import os

# Add the 'src' directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))

from main import app  # now importing from src/main.py

if __name__ == '__main__':
    app.run()