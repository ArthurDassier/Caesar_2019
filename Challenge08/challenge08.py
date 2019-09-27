#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import operator
import codecs as c
import binascii
import math
import struct
import base64

def chunks_repetition(ciphertext, block_size):
    chunks = []
    for i in range(0, len(ciphertext), block_size):
        chunks += ciphertext[i:i + block_size]
    number_of_repetitions = len(chunks) - len(set(chunks))
    return (ciphertext, number_of_repetitions)

def main():
    with open(sys.argv[1], 'r') as file:
        ciphertext = file.read()
        ciphertext = ciphertext.replace(" ", "")
        ciphertext = ciphertext.splitlines()
        ciphertext_decoded = []
        for cipher in ciphertext:
            ciphertext_decoded.append(base64.b64decode(cipher))
        repetitions = [chunks_repetition(cipher, 16) for cipher in ciphertext_decoded]
        print(ciphertext.index(base64.b64encode(max(repetitions, key=lambda x:x[1])[0]).decode("utf-8")) + 1)



if __name__ == "__main__":
    try:
        main()
    except Exception:
        exit(84)