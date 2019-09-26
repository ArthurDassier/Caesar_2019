#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import operator
import codecs as c
import binascii
import math
import struct


def xor_string(input_bytes, key):
    final_sentence = b''
    key_index = 0
    for bytes_index in input_bytes:
        final_sentence += bytes([operator.xor(bytes_index, key[key_index])])
        if (key_index + 1) == len(key):
            key_index = 0
        else:
            key_index += 1
    return final_sentence


def main():
    with open(sys.argv[1], 'r') as file:
        first_line = file.readline()
        first_line = first_line.replace(" ", "")
        first_line = first_line.replace("\n", "")
        line = file.read()
        line = line.replace(" ", "")
        line = line.replace("\n", "")
        if len(first_line) == 0 or len(line) == 0:
            exit(84)
        binary = bytes.fromhex(line)
        key = bytes.fromhex(first_line)
        message = xor_string(binary, key)
        print(message.hex().upper())


if __name__ == "__main__":
    try:
        main()
    except Exception:
        exit(84)