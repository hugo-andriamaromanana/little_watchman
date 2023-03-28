## Havaianas-Store Scraper

This Python script allows you to scrape product information from the Havaianas-Store website, including product name, reference, description, images, price, currency, brand, category, and composition.

## Requirements

    Python 3
    Beautiful Soup 4 (bs4)
    lxml parser for Beautiful Soup
    urllib.request for requesting web pages
    json for loading and dumping data

## Usage

    Edit the scrape(link_init) function to match the specific HTML structure of the page you want to scrape.
    Call the scrape(link_init) function, passing in the link to the specific product page on the Havaianas-Store website you want to scrape.
    The function will return a dictionary containing the scraped data.
    Use the dump_data(name, data) function to save the scraped data to a JSON file.

## Functions

    get_html(url): Takes a URL as an argument and returns the HTML content of the page as a string.
    get_data(name): Takes the name of a JSON file as an argument and returns the data in that file as a dictionary.
    dump_data(name, data): Takes a name for a JSON file and a dictionary of data and saves the data to the file.
    scrape(link_init): Takes a link to a product page on the Havaianas-Store website as an argument and returns a dictionary of scraped data for that product.

## Disclaimer

Please be aware that web scraping may violate the terms of service of some websites. Use at your own risk.