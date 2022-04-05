import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

if os.getenv("ENV") == "test":
    load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env.test"))
else:
    load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))

DATABASE_FILENAME = os.getenv("DATABASE_FILENAME") or "database.sqlite"
DATABASE_FILE_PATH = os.path.join(dirname, '..', 'data', DATABASE_FILENAME)
