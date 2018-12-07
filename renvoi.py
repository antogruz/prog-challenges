#!/usr/bin/env python3

import re
from request import get_page_with_cookie

address = "https://www.newbiecontest.org/epreuves/prog/prog1.php"
output = "https://www.newbiecontest.org/epreuves/prog/verifpr1.php"

def main():
    text = get_page_with_cookie(address)
    text = re.sub("[^0-9]", "", text)
    answer = get_page_with_cookie(output + "?solution=" + text)
    print(answer)

main()
