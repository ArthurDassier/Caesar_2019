#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import sys
import operator
import codecs as c

def main():
    with open(sys.argv[1], 'r') as file:
        first_line = file.readline()[:-1]
        second_line = file.readline()
        file.seek(0)
        if len(first_line) == len(second_line):
            sys.stdout.write(str(hex(operator.xor(int(file.readline()[:-1], base=16), int(file.readline(), base=16)))).upper()[2:] + '\n')
        else:
            exit(84)

if __name__ == "__main__":
    try:
        main()
    except Exception:
        exit(84)