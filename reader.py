#!/usr/bin/env python3

import os

tmp = "tmp.txt"
address = "https://www.newbiecontest.org/epreuves/prog/prog10.php"
sessid = "387c6a652eeb756a10f99d8f6bf37634"
answer_address = "https://www.newbiecontest.org/epreuves/prog/verifpr10.php"

def main():
    file = get_file(address)
    text = read_file(file)
    print(text)

def get_file(address):
    os.system("wget {} -o {}".format(address,tmp))
    return tmp

def read_file(f):
    text = os.popen('gocr {}'.format(f)).read()
    text = text.split("\n")[0]
    return text


main()
