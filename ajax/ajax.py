from bs4 import BeautifulSoup
import json
from urllib.request import Request, urlopen
import time
import random

def get_html(current_year):
    req = Request(
        url=f'https://www.scrapethissite.com/pages/ajax-javascript/?ajax=true&year={current_year}',
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    return urlopen(req).read()

output = {}

def main(output):
    for year in range(2010,2016):
        soup=BeautifulSoup(get_html(year),features='lxml')
        output[str(year)]=json.loads(soup.p.string)
        time.sleep(random.randint(1,3))
        print('-')
        print('Done with year: '+str(year))
    return output

main(output)

with open('movies.json','w') as f:
        json.dump(output,f,indent=4)