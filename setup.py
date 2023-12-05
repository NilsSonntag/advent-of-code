import os
import venv
import subprocess
import platform
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

def create_venv():
    """Create a virtual environment."""
    VENV_DIRECTORY = "venv"

    if not os.path.exists(VENV_DIRECTORY):
        logging.info("Creating virtual environment...")
        venv.create(VENV_DIRECTORY, with_pip=True)
    else:
        logging.info("Virtual environment already exists.")

def install_requirements():
    """Install requirements in the virtual environment."""
    logging.info("Installing requirements...")
    VENV_DIRECTORY = "venv"
    if platform.system() == "Windows":
        subprocess.run([f"{VENV_DIRECTORY}\\Scripts\\activate.bat", "&&", "pip", "install", "-r", "requirements.txt"])
    else:
        subprocess.run([f"source {VENV_DIRECTORY}/bin/activate", "&&", "pip", "install", "-r", "requirements.txt"])

def setup_aoc_session():
    """Set up the Advent of Code session."""
    if 'AOC_SESSION' not in os.environ:
        session_id = input('Enter session ID: ')
        os.environ['AOC_SESSION'] = session_id
    logging.info("Advent of Code session set up.")

if __name__ == "__main__":
    create_venv()
    install_requirements()
    setup_aoc_session()