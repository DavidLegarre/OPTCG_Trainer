import json


def test_data():
    data = json.load(open("onepiece_cards.json", "r", encoding="utf-8"))
    print(len(data))
