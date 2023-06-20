import csv
with open('apach_logs.txt.txt') as f:
    for r in csv.reader(f, delimiter=" "):
        print(r)