# -*- coding: utf-8 -*-
__author__ = 'bglebov'

import csv
import re
import json

def export():
    with open('c:\\temp\\blank.log', 'r') as f:
        with open('c:\\temp\\blank.csv', 'w') as csvfile:

            lines = [l[29:] for l in f.read().split('\n') if l != '']
            writer = csv.writer(csvfile, delimiter=';')

            writer.writerow(['Имя', 'Фамилия', 'Компания', 'Должность', 'Контактный телефон', 'Email'])

            for line in lines:
                try:
                    person = eval(line)
                    writer.writerow([person['firstname'].encode('utf-8'),
                                    person['lastname'].encode('utf-8'),
                                    person['company'].encode('utf-8'),
                                    person['phone'].encode('utf-8'),
                                    person['position'].encode('utf-8'),
                                    person['email'].encode('utf-8')])
                except Exception as ex:
                    print ex


if __name__ == '__main__':
    export()