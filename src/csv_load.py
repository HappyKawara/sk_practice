#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pprint
import csv
import re

def main():
    male = []
    with open('eg_male.csv') as fm:
        reader = csv.reader(fm)
        for row in reader:
            male += [re.sub('-','',name.lower()) for name in row if re.match(r'\D|\.|^\n',name) ]
    female = []
    with open('eg_female.csv') as ff:
        reader = csv.reader(ff)
        for row in reader:
            female += [re.sub('-','',name.lower()) for name in row if re.match(r'\D|\.|^\n|\"',name) ]

    male = list(set(male))
    female = list(set(female))
    return male[1::],female[1::]
if __name__ == '__main__':
    pprint.pprint(main()[1])
