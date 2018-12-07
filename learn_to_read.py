#!/usr/bin/env python3

import os
from request import get_file_with_cookie, get_page_with_cookie

tmp = "tmp.png"
address = "https://www.newbiecontest.org/epreuves/prog/prog10.php"
answer_address = "https://www.newbiecontest.org/epreuves/prog/verifpr10.php?chaine={}"

def main():
    get_file_with_cookie(address, tmp)
    text = read_file(tmp)
    answer = get_page_with_cookie(answer_address.format(text))
    print(answer)

def read_file(f):
    text = os.popen('gocr {}'.format(f)).read()
    text = text.split("\n")[0]
    return text

main()
