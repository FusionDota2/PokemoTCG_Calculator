import csv


def read_infiles(infile_pokemon, infile_combochecks):
    basics = list()
    relations = dict()
    DECKLIST = list()
    with open(infile_pokemon) as infile_pokemon:
        for line in csv.reader(infile_pokemon):
            DECKLIST.append(line[0])
            if line[-1] == 'True':
                basics.append(line[0])
    with open(infile_combochecks) as infile_combochecks:
        for line in infile_combochecks.readlines():
            relations.update({line: 0})
    return relations, basics, DECKLIST
