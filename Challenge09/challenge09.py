#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import operator
import codecs as c
import binascii
import math
import struct
import base64


def main():
    with open(sys.argv[1], 'r') as file:
        key = file.readline()
        key = key.replace(" ", "")
        key = key.replace("\n", "")
        init_vector = file.readline()
        init_vector = init_vector.replace(" ", "")
        init_vector = init_vector.replace("\n", "")
        ciphertext = file.read()
        ciphertext = ciphertext.replace(" ", "")
        ciphertext = ciphertext.replace("\n", "")
        # To Do


if __name__ == "__main__":
    try:
        main()
    except Exception:
        exit(84)