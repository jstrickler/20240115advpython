import csv

with open('../DATA/presidents.csv') as presidents_in:
    rdr = csv.reader(presidents_in)  # <1>
    for row in rdr:  # <2>
        print('{:25s} {:12s} {}'.format(
            row[1],row[2], row[-1]
        ))
