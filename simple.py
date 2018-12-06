#!/usr/bin/env python3

import os
import re

sessid = "55fd7ee4fa8147105a7a806d8aeca83e"
smfcookie89 = "a%3A4%3A%7Bi%3A0%3Bs%3A5%3A%2259438%22%3Bi%3A1%3Bs%3A40%3A%22ad298775288608b19f0382a471dd333380effb1f%22%3Bi%3A2%3Bi%3A1733327492%3Bi%3A3%3Bi%3A0%3B%7D"
address = "https://www.newbiecontest.org/epreuves/prog/prog1.php"
output = "https://www.newbiecontest.org/epreuves/prog/verifpr1.php"

def main():
    text = os.popen("curl '{address}'   -H 'Cookie: PHPSESSID={sessid}; SMFCookie89={smf}'".format(address=address, sessid=sessid, smf=smfcookie89)).read()
    text = re.sub("[^0-9]", "", text)
    print(text)



main()
