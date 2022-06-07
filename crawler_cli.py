'''
                MiniCrawler
Author:         Kovács Péter
Date:           2022.06.

Iteration:      4. 
Goal:           Add parameters to the main function with 'click' decorators for a
                CLI experience.
                --url        --> The root url (required, string)
                --depth, -d  --> How deep can go the recursivity (default=2, int)
                --file, -f   --> Write results into this file (default=none, string)
                Refactor the program based on these new variables.  

Help:           
'''

from types import NoneType
import requests, re
import click

DOMAIN = None
ENABLED_DEPTH = None
RESULT_FILE = None
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
    #global DOMAIN, ENABLED_DEPTH, RESULT_FILE
    
    html = get_html_of(url)
    results = re.findall("<a href=\".*\">", html)

    for result in results:
        link_match = re.search(f"http(s)?://([a-z]*\.)?{DOMAIN}(/.*/)?",result) #Eddig beégetett progmasters.hu volt. Próbáljuk általánosítani kicsit
        
        if acceptable(link_match):
            link_url = link_match.group()

            if RESULT_FILE is None:
                print(INTENDATION*depth, link_url)
            else:
                RESULT_FILE.write(f"{INTENDATION*depth}{link_url}\r\n")

            add_to_visited_urls_this(link_url)

            if depth < ENABLED_DEPTH:
                collect_links_from(link_url, depth+1)
        '''
        # Önellenőrzéshez: kiíratom a nem elfogadható (=már vizsgált) url-t, hogy lássam, tényleg ismétlésről lenne szó
        else:
            if type(link_match) is not NoneType:
                print(f"Not acceptable:{link_match.group()}")
        '''

@click.command()
@click.option('--url', prompt="Give me an url", help="Crawler will start from here.")
@click.option('--depth', '-d', default=1, help="How deep the recursive process can go. Default: 1")
@click.option('--file', '-f', default="none", help="Crawler try to write results into this file, if defined.")
def main(url, depth, file):    
    global DOMAIN, ENABLED_DEPTH, RESULT_FILE, VISITED_URLS # Funkción belül muszáj globálissá tenni, különben egy lokális változatot használna belőle

    DOMAIN = return_domain_of(url)
    ENABLED_DEPTH = depth

    if file  != "none":
        RESULT_FILE = open(file,"a")

    print("Crawler is running...")
    add_to_visited_urls_this(url)
    collect_links_from(url, 0)

    if RESULT_FILE is not None:
        RESULT_FILE.close()
    
    print("Crawler finished!")

if __name__ == "__main__":
    main()