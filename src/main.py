from src.data_fetching.data_test import test_data
from src.data_fetching.fetch_data import fetch_all_card_data


def fetch_data():
    fetch_all_card_data()
    test_data()

if __name__=='__main__':
    fetch_data()