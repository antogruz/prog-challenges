sessid = "fc00efc3560fd888cb076344407a2e67"
smfcookie89 = "a%3A4%3A%7Bi%3A0%3Bs%3A5%3A%2259438%22%3Bi%3A1%3Bs%3A40%3A%22ad298775288608b19f0382a471dd333380effb1f%22%3Bi%3A2%3Bi%3A1733388307%3Bi%3A3%3Bi%3A0%3B%7D"

import os

def get_page_with_cookie(address):
    return os.popen("curl '{address}'   -H 'Cookie: PHPSESSID={sessid}; SMFCookie89={smf}'".format(address=address, sessid=sessid, smf=smfcookie89)).read()
