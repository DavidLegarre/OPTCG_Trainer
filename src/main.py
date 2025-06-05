from src.data_fetching.data_test import test_data
from src.data_fetching.fetch_data import fetch_all_card_data
from src.game_state.cards.actions.triger_parser import parse_effects
from loguru import logger


def main():
    text = "[On Play] Look at 5 cards from the top of your deck and place them at the top or bottom of the deck in any order."

    text = text.strip().lower()
    logger.info(text)

    effects = parse_effects(text)

    print(effects)


if __name__ == "__main__":
    main()
