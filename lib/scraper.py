import wget
from dotenv import load_dotenv
import os

def download():
    load_dotenv()

    try:
        wget.download(os.getenv("URL"), os.getenv("FILENAME"))
        print("Download successfully completed")
    except Exception as e:
        print("Error: ", e)

def remove():
    load_dotenv()

    try:
        os.remove(os.getenv("FILENAME"))
        print(f"File {os.getenv('FILENAME')} has been deleted")
    except OSError as e:
        print("Error: ", e)
