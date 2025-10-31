# main.py
from source.extract import read_csv
from source.logging import logger
from source.transform import transform_data

csv_file = "../files/sales.csv"
csv_content = read_csv(csv_file)

def main():
    print(read_csv(csv_file))
    print(transform_data(csv_content))


if __name__ == "__main__":
    logger.info("Application started.")
    main()
    logger.info("Application finished.")
 