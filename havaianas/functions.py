import json
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen


def get_html(url):
    req = Request(
        url,
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    return urlopen(req).read()

def get_data(name):
    with open(f"{name}.json") as f:
        data = json.load(f)
    return data

def dump_data(name, data):
    with open(f"{name}.json", 'w') as f:
        json.dump(data, f, indent=4)

def scrape(link_init):
    soup = BeautifulSoup(
        get_html(f'https://www.havaianas-store.com/{link_init}'), 'lxml')
    gift = json.loads(soup('head')[-1]('script')
                      [-1].text.replace('\n', '').strip())
    category_init = soup('div', 'col', 'ol')
    composition = soup('div', 'col-sm-12 col-md-8 value content')
    images = soup('div', 'carousel-item active')
    try:
        category = category_init[0]('li')[3].text.replace('\n', '')
    except:
        category = ""
    try:
        low_price = gift["offers"]["lowprice"]["sales"]
        previous_prices = [low_price["decimalPrice"]]

        price = gift["offers"]["highprice"]["sales"]
        current_price = price["decimalPrice"]

        currency = gift["offers"]["highprice"]["sales"]
        currency = currency["currency"]
    except:
        low_price_init = soup('strike')
        previous_prices = [low_price.text[:-2] for low_price in low_price_init]

        price_init = soup('span', 'sales')
        current_price = price_init[0].text.replace('\n', '')[:-2]

        currency = gift["offers"]["priceCurrency"]
    try:
        composition = composition[0].text.replace('\n', '').strip()
    except:
        composition = ""
    try:
        images = images[0]('img')[0].get('src')
    except:
        images = ""
    try:
        name = gift["name"]
    except:
        name = ""
    try:
        reference = gift["mpn"]
    except:
        reference = ""
    try:
        description = gift["description"]
    except:
        description = ""
    try:
        brand = gift["brand"]["name"]
    except:
        brand = ""
    return {
        "name": name,
        "reference": reference,
        "description": description,
        "images": images,
        "current_price": current_price,
        "previous_prices": previous_prices,
        "url": f'https://www.havaianas-store.com/{link_init}',
        "from": "havaianas-store",
        "currency": currency,
        "brand": brand,
        "category": category,
        "composition": composition
    }