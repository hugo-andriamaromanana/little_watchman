from bs4 import BeautifulSoup
import json
from urllib.request import Request, urlopen
import time
import random


def get_html(page):
    req = Request(
        url=f'https://www.scrapethissite.com/pages/forms/?page_num={page}&per_page=100',
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    return urlopen(req).read()


output = {}


def main(output):

    count = 1

    for page in range(1, 7):

        soup = BeautifulSoup(get_html(page), features='lxml')

        teams = soup("td", "name")
        years = soup("td", "year")
        wins = soup("td", "wins")
        losses = soup("td", "losses")
        ot_losses = soup("td", "ot-losses")
        win_rate = soup("td", "pct")
        goals_for = soup("td", "gf")
        goals_against = soup("td", "ga")
        plus_minus = soup("td", "diff")

        for i in range(len(teams)):
            team_var = teams[i].text.strip()
            year_var = years[i].text.strip()
            win_var = wins[i].text.strip()
            loss_var = losses[i].text.strip()
            ot_loss_var = ot_losses[i].text.strip()
            goal_for_var = goals_for[i].text.strip()
            goal_against_var = goals_against[i].text.strip()
            plus_minus_var = plus_minus[i].text.strip()
            win_rate_var = win_rate[i].text.strip()

            output[f'Game: {count}'] = {
                'team': team_var,
                'year': year_var,
                'win': win_var,
                'loss': loss_var,
                'ot_loss': ot_loss_var,
                'win_rate': win_rate_var,
                'goal_for': goal_for_var,
                'goal_against': goal_against_var,
                'plus_minus': plus_minus_var
            }

            count += 1

        time.sleep(5+random.randint(0, 10))

        print('-' * 20)
        print(f'Page {page} done!')

    return output


main(output)

with open('hockey.json', 'w') as fp:
    json.dump(output, fp, indent=4)