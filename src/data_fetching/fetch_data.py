import requests
import json
from typing import List
from tqdm import tqdm


BASE_URL = "https://optcgapi.com/api"


def fetch_all_card_data() -> List[dict]:
    # 1. Get all set IDs
    sets = requests.get(f"{BASE_URL}/allSets/").json()

    all_cards = []
    # 2. For each set, fetch its cards
    for s in tqdm(sets):
        set_id = s["set_id"]
        cards = requests.get(f"{BASE_URL}/sets/{set_id}/").json()
        all_cards.extend(cards)

    with open("onepiece_cards.json", "w", encoding="utf-8") as f:
        json.dump(all_cards, f, ensure_ascii=False, indent=2)

    return all_cards


