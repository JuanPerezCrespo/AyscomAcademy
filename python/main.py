# main.py
from source.logging import logger
from source import extract

def main():
    print("Hello")
    extract.extract_data()

if __name__ == "__main__":
    logger.info("Application started.")
    main()
    logger.info("Application finished.")