from functions import *

woman_page='https://www.havaianas-store.com/fr/fr/femme-all?=&start=0&sz=688'
men_page='https://www.havaianas-store.com/fr/fr/homme-all?=&start=0&sz=317'
flash_page='https://www.havaianas-store.com/fr/fr/flash-sale?=&start=0&sz=378'
new_page='https://www.havaianas-store.com/fr/fr/nouvelle-collection?=&start=0&sz=337'

TARGETS=[woman_page,men_page,flash_page,new_page]

shop = get_data('shop')

def main(shop):
    page = TARGETS[2]
    target=get_html(page)
    soup = BeautifulSoup(target, 'lxml')
    links = soup('div', 'pdp-link')
    for link in links:
        link_init = link.find('a').get('href')
        shop.append(scrape(link_init))
        print(f'Added {link_init} to shop')
    return shop

if __name__ == '__main__':
    shop=main(shop)
    dump_data('shop',shop)