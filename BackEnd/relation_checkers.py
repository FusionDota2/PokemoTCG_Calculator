def check_all_relations(hand, prizes, deck, relations):
    for relation in relations.keys():
        if eval(relation):
            # print(hand)
            relations[relation] += 1


def is_in_hand(card, hand):
    if card in hand:
        return True
    else:
        return False


def is_in_prizes(card, prizes):
    if card in prizes:
        return True
    else:
        return False


def is_in_deck(card, deck):
    if card in deck:
        return True
    else:
        return False
