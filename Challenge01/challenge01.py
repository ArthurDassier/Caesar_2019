#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import sys
import codecs as c


def main():
    with open(sys.argv[1], 'r') as file:
        line = file.read()
        line = line.replace(" ", "")
        line = line.replace("\n", "")
        sys.stdout.write(c.encode(c.decode(line, 'hex'), 'base64').decode())


if __name__ == "__main__":
    try:
        main()
    except Exception:
        exit(84)