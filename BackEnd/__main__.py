from run_shuffles import *
from infile_parser import read_infiles

HANDSIZE = 7
PRIZEAMOUNT = 6


def __main__(infile_decklist, infile_relations, amount=20000):
    relations, basics, DECKLIST = read_infiles(infile_decklist, infile_relations)
    nobasic_amount = run_shuffles(relations, basics, amount, DECKLIST)
    print('Odds for basic in percentile:')
    print(round(100 - nobasic_amount / amount * 100, 2))
    for relation in relations:
        print(relation)
        print(round(relations[relation] / amount * 100, 2))
    print('ByeBye')


__main__('Decklist.csv', 'Relations.txt')
