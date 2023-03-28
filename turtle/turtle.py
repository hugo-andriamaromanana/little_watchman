from bs4 import BeautifulSoup
import json
from urllib.request import Request, urlopen
import time
import random


def get_html(url):
    req = Request(
        url,
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    return urlopen(req).read()


output = {}


def main(output):
    init_soup = BeautifulSoup(
        get_html('https://www.scrapethissite.com/pages/frames/?frame=i'), 'lxml')

    family_name = init_soup('h3', 'family-name')
    images_link = init_soup('div', 'col-md-4 turtle-family-card')

    names = [name.string for name in family_name]
    images = [image.img.get('src') for image in images_link]

    for i in range(len(names)):
        soup = BeautifulSoup(get_html(
            f'https://www.scrapethissite.com/pages/frames/?frame=i&family={names[i]}'), 'lxml')
        descriptions = soup('p', 'lead')[0].text.strip().replace('\n', '')
        output[names[i]] = {
            'Description': descriptions,
            'Image': images[i]
        }
        time.sleep(5+random.randint(0, 10))

        print('-' * 20)
        print(f'Page {names[i]} done!')

    return output


main(output)

with open('turtle.json', 'w') as f:
    json.dump(output, f, indent=4)
