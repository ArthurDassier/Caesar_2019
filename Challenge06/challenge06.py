#!/usr/bin/env python3.7
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


def single_byte_xor(line):
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
    return (format(best_score['key'], 'x'))



def hamming_distance(str_one, str_two):
    distance = 0

    for x, y in zip(str_one, str_two):
        xored = operator.xor(x, y)

        distance += sum([1 for bits in bin(xored) if bits == '1'])
    return distance


def first_guess():
    with open(sys.argv[1], 'r') as file:
        line = file.read()
        line = line.replace(" ", "")
        line = line.replace("\n", "")

    tab = []

    for keysize in range(5, 41):

        chunks = [line[i:i+keysize] for i in range(0, len(line), keysize)]

        chunk_1 = chunks[0]
        chunk_2 = chunks[1]
        distance = hamming_distance(bytes(chunk_1, 'utf-8'), bytes(chunk_2, 'utf-8'))
        tab.append(((distance / keysize), keysize))
    #print(min(tab)[1])
    text_chunks = [line[i:i+round(min(tab)[1])] for i in range(0, len(line), round(min(tab)[1]))]
    truc = []
    for elem in text_chunks:
        truc.append(single_byte_xor(elem))
    print (*truc, sep='')

def main():
    print(hamming_distance(b'Hello', b'World'))
    first_guess()

if __name__ == "__main__":
    #try:
        main()
    #except Exception:
    #   exit(84)