'''
                MiniCrawler
Author:         Kovács Péter
Date:           2022.06.

Iteration:      2. 
Goal:           Create functions for these tasks:
                - read the html source of the given url and implement basic error handling
                - collect all link address from the response to a list by regular expressions
                - print the list to the standard output 

Help:           Reguláris kifejezések ellenőrzése + cheatsheet:  https://regex101.com/
'''

from types import NoneType
import requests, re

ROOT_URL = "http://www.progmasters.hu"

def get_html_of(url):
    response = requests.get(url)

    if response.status_code !=  200:
        print(f"Can not reach {url}. Error: {response.status_code}")
        exit(0)

    return response.content.decode()

def collect_links_from(url):
    html = get_html_of(url)
    results = re.findall("<a href=\".*\">", html) # A link tagek kiszűrésére használt regex kifejezés

    for result in results:
        link = re.search("http(s)?://([a-z]*\.)?progmasters.hu(/.*/)?",result)
        if type(link) is not NoneType: # Ez azért kell, mert lehet, hogy nem talált egyezést az előző kifejezés
            print(link.group())

def run():
    collect_links_from(ROOT_URL)