'''
                MiniCrawler
Author:         Kovács Péter
Date:           2022.06.

Iteration:      3. 
Goal:           Implement recursivity
                - add the previously explored links to a list
                - iterate through them and collect additional links from their source code too
                - avoid duplicatums
                - use intendation on the output, based on the depth of recursivity

Help:           
'''

from types import NoneType
import requests, re

ROOT_URL = "http://www.progmasters.hu"
INTENDATION = "   "
VISITED_URLS = list()

def add_to_visited_urls_this(url):
    global VISITED_URLS
    VISITED_URLS.append(url)

def get_html_of(url):
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Can not reach {url}. Error: {response.status_code}")
        exit(0)
        
    return response.content.decode()

def acceptable(link_match):
    global VISITED_URLS

    if type(link_match) is NoneType:
        return False
    if link_match.group() in VISITED_URLS:
        return False
    
    return True

def return_domain_of(root_url):

    match = re.match('https?://.*\.[a-z]{2,3}', root_url)
    domain = match.group()
    split_result = domain.split('.',1) # Max. egy splitet hajt végre, így a végére hivatkozhatok egyként

    return split_result[1]

def collect_links_from(url, depth):
    html = get_html_of(url)
    results = re.findall("<a href=\".*\">", html)

    for result in results:
        link_match = re.search(f"http(s)?://([a-z]*\.)?{return_domain_of(ROOT_URL)}(/.*/)?",result) #Eddig beégetett progmasters.hu volt. Próbáljuk általánosítani kicsit
        
        if acceptable(link_match):
            link_url = link_match.group()
            print(INTENDATION*depth, link_url)

            add_to_visited_urls_this(link_url)

            if depth < 1:
                collect_links_from(link_url, depth+1)
        '''
        # Önellenőrzéshez: kiíratom a nem elfogadható (=már vizsgált) url-t, hogy lássam, tényleg ismétlésről lenne szó
        else:
            if type(link_match) is not NoneType:
                print(f"Not acceptable:{link_match.group()}")
        '''
def run():
    add_to_visited_urls_this(ROOT_URL)
    collect_links_from(ROOT_URL, 0)