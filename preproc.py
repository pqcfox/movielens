import csv
import re


def strip_year(title):
    match = re.match(r'(.*) \(\d+\)', title)
    if match is None:
        return title
    return match.group(1)

with open('u.data') as f:
    reader = csv.reader(f, delimiter='\t')
    datalines = [[line[1], line[0], line[2]] for line in reader]

with open('largedata.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(datalines)

# HACK: u.item won't read in utf-8; use latin-1
with open('u.item', encoding='latin-1') as f:
    reader = csv.reader(f, delimiter='|')
    keylines = [[line[0], strip_year(line[1])] for line in reader]

with open('largekey.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(keylines)
