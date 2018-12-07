#!/usr/bin/env python3

from request import get_page_with_cookie
import re

address = "https://www.newbiecontest.org/epreuves/prog/prog9/epreuve9.php"
output = "https://www.newbiecontest.org/epreuves/prog/prog9/verifpr9.php?prenom={}&prix={}"

def main():
    text = get_page_with_cookie(address)
    prenom, prix = solve(text)
    answer = get_page_with_cookie(output.format(prenom, prix))
    print(answer)

def solve(text):
    configs = get_configs(text)
    barettes = get_barettes(text)
    processors = get_processors(text)
    return get_max_price(configs, compute_prices(barettes), compute_prices(processors))

def get_max_price(text, barettes, processors):
    max_price = 0
    max_name = ""
    guys = text.split(". ")
    for guy in guys[:-1]:
        name, proc, barette = parse_config(guy)
        price = int(barettes[barette]) + int(processors[proc])
        if price > max_price:
            max_price = price
            max_name = name

    return max_name, max_price

def parse_config(guy):
    all = re.split(' a un processeur de | et dispose de ', guy)
    return tuple(all)

def compute_prices(text):
    prices = {}
    refs = text.split("</tr>")
    for r in refs[:-1]:
        key, price = get_key_and_price(r)
        prices[key] = price
    return prices

def get_key_and_price(r):
    fields = r.split("<td>")
    key = fields[1].split("</td")[0]
    price = fields[2].split("</td")[0]
    return key, price

def get_configs(text):
    return get_between(text, '<hr width="90%" />', "<br><br>")

def get_barettes(text):
    before = """
<tr>
	<td align='center'>Désignation</td>
	<td align='center'>Prix (en euros)</td>
<tr>
"""
    return get_between(text, before, "\n</table>")

def get_processors(text):
    before = """
<table width=70% border='1px solid' align='center'>
<tr>
	<td colspan='2' align='center'><b>Tarifs des processeurs</b></td>
<tr>
<tr>
	<td align='center'>Désignation</td>
	<td align='center'>Prix (en euros)</td>
<tr>
"""
    return get_between(text, before, "\n</table>")

def get_between(text, before, after):
    return text.split(before)[1].split(after)[0]

main()
