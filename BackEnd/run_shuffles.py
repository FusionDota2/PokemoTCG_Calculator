import random
from relation_checkers import check_all_relations
import copy

random.seed(4)
HANDSIZE = 7
PRIZEAMOUNT = 6


def run_shuffles(relations, basics, amount, DECKLIST):
    relationhits_global = list()
    for i in range(len(relations.keys())):
        relationhits_global.append(0)
    nobasic = 0
    relationhits = list()
    for i in range(len(relations.keys())):
        relationhits.append(0)
    for i in range(amount):
        shuffle(DECKLIST)
        hand = take_hand(DECKLIST)
        if not has_basic(hand, basics):
            nobasic += 1
            continue
        prizes, deck = place_prizes(DECKLIST)
        check_all_relations(hand, prizes, deck, relations, relationhits)
        for j in range(len(relationhits)):
            relationhits_global[j] += relationhits[j]
    return relationhits_global, nobasic


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
