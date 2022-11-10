#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pprint
import csv
import re
import os

file_path = os.path.expanduser("~/catkin_ws/src/sk_practice/config/")

def main():
    male = []
    with open(file_path + 'eg_male.csv') as fm:
        reader = csv.reader(fm)
        for row in reader:
            male += [re.sub("-|\.|'",'',name.lower()) for name in row if re.match("\D",name)]
    female = []
    with open(file_path + 'eg_female.csv') as ff:
        reader = csv.reader(ff)
        for row in reader:
            female += [re.sub("-|\.|'",'',name.lower()) for name in row if re.match("\D",name)]

    male = list(set(male))
    female = list(set(female))
    return male[1::],female[1::]
if __name__ == '__main__':
    pprint.pprint(main()[0])
