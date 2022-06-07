'''
                MiniCrawler
Author:         Kovács Péter
Date:           2022.06.04

Iteration:      1. 
Goal:           Read the html source of a predefined url with the help of
                the 'requests' package. Present it on the standard output!
'''

import requests # Ezzel a csomaggal fogunk HTTP kéréseket küldeni és fogadni

ROOT_URL = "http://www.progmasters.hu"

def run():
    response = requests.get(ROOT_URL)
    html = response.content.decode() # Ha a beérkező tartalom encode-olt, akkor nem lesz olvasható
    print(html)