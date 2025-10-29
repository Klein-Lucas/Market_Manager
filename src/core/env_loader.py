import os
from dotenv import load_dotenv

def initialize_environment():
    """
    Load environment variables from a .env file.
    """
    env_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')
    if os.path.exists(env_file):
        load_dotenv(env_file)
        print("Environment variables loaded from .env file.")
    else:
        print(".env file not found.")