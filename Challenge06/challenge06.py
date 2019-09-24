#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import sys
import operator
import codecs as c
import binascii
import math
import struct

def hamming_distance(chaine1, chaine2):
    return sum(c1 != c2 for c1, c2 in zip(chaine1, chaine2))

def hamming_distance2(chaine1, chaine2):
    return len(list(filter(lambda x : ord(x[0])^ord(x[1]), zip(chaine1, chaine2))))

def main():
    str1 = 'Hello'
    str2 = 'World'
    print(hamming_distance(bytes(str1, 'utf-8'), bytes(str2, 'utf-8')))

if __name__ == "__main__":
    try:
        main()
    except Exception:
        exit(84)