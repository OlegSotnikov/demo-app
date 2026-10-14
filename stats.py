import csv
from collections import defaultdict


def month_totals(path):
    totals = defaultdict(float)
    with open(path, newline="") as f:
        for row in csv.DictReader(f):
            totals[row["date"][:7]] += float(row["amount"])
    return dict(totals)
