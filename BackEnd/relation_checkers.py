def check_all_relations(hand, prizes, deck, relations):
    for relation in relations.keys():
        if eval(relation):
            # print(hand)
            relations[relation] += 1
			