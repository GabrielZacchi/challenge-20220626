from pathlib import Path
import os
import environ

BASE_DIR = Path(__file__).resolve().parent.parent


env = environ.Env(DEBUG=(bool, False))
# reading .env file
env_file = os.path.join(BASE_DIR, ".env")
environ.Env.read_env(env_file)