#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import operator
import codecs as c
import binascii
import math
import struct

character_frequencies = {
    'a': 0.08167, 'b': 0.01492, 'c': 0.02782, 'd': 0.04253, 'e': 0.1270,
    'f': 0.02228, 'g': 0.02015, 'h': 0.06094, 'i': 0.06966, 'j': 0.00153,
    'k': 0.00772, 'l': 0.04025, 'm': 0.02406, 'n': 0.06749, 'o': 0.07507,
    'p': 0.01929, 'q': 0.00095, 'r': 0.05987, 's': 0.06327, 't': 0.09056,
    'u': 0.02758, 'v': 0.00978, 'w': 0.02360, 'x': 0.00150, 'y': 0.01974,
    'z': 0.00074
}


def find_english_score(input_bytes):
    english_score = []
    for byte in input_bytes.lower():
        actual_score = character_frequencies.get(chr(byte), 0)
        english_score.append(actual_score)
    return sum(english_score)


def xor_on_char(input_bytes, char_value):
    final_sentence = b''
    for index in input_bytes:
        final_sentence += bytes([operator.xor(index, char_value)])
    return final_sentence


def main():
    with open(sys.argv[1], 'r') as file:
        line = file.read()
        line = line.replace(" ", "")
        line = line.replace("\n", "")
        first_text = binascii.unhexlify(line)
        tab_of_data = []
        for key_value in range(256):
            message = xor_on_char(first_text, key_value)
            score = find_english_score(message)
            data = {
                # 'message': message,
                'score': score,
                'key': key_value
                }
            tab_of_data.append(data)
        best_score = sorted(tab_of_data, key=lambda x: x['score'], reverse=True)[0]
        print(format(best_score['key'], 'x'))


if __name__ == "__main__":
    try:
        main()
    except Exception:
        exit(84)