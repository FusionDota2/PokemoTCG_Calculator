def check_all_relations(hand, prizes, deck, relations):
    for relation in relations.keys():
        if eval(relation):
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


def is_in_deck(card, hand, prizes, DECKLIST):
    if is_in_hand(card, hand) or is_in_prizes(card, prizes):
        notindeckamount = hand.count(card) + prizes.count(card)
        if notindeckamount == DECKLIST.count(card):
            return False
        else:
            return True
    else:
        return True
