# main.py
from source.extract import read_csv
from source.logging import logger

csv_file = "../files/sales.csv"

def main():
    print(read_csv(csv_file))

if __name__ == "__main__":
    logger.info("Application started.")
    main()
    logger.info("Application finished.")
 