#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import codecs as c


def main():
    with open(sys.argv[1], 'r') as file:
        line = file.read()
        line = line.replace(" ", "")
        line = line.replace("\n", "")
        display = c.encode(c.decode(line, 'hex'), 'base64').decode()
        display = display.strip()
        for char in display:
            if ord(char) != 0 and ord(char) != 10:
                sys.stdout.write(char)
        sys.stdout.write('\n')


if __name__ == "__main__":
    try:
        main()
    except Exception:
        exit(84)