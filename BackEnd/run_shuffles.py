import random
from relation_checkers import check_all_relations
import copy

HANDSIZE = 7
PRIZEAMOUNT = 6


def run_shuffles(relations, basics, amount, DECKLIST):
    nobasic = 0
    for i in range(amount):
        shuffle(DECKLIST)
        hand = take_hand(DECKLIST)
        if not has_basic(hand, basics):
            nobasic += 1
            continue
        prizes, deck = place_prizes(DECKLIST)
        check_all_relations(hand, prizes, deck, relations)
    return nobasic


def place_prizes(DECKLIST):
    prizes = copy.copy(DECKLIST[HANDSIZE:HANDSIZE + PRIZEAMOUNT])
    deck = copy.copy(DECKLIST[HANDSIZE + PRIZEAMOUNT:])
    return prizes, deck


def shuffle(DECKLIST):
    random.shuffle(DECKLIST)
    return None


def take_hand(DECKLIST):
    hand = copy.copy(DECKLIST[:HANDSIZE])
    return hand


def has_basic(hand, basics):
    for card in hand:
        if card in basics:
            return True
    return False
