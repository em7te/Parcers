import requests
from bs4 import BeautifulSoup


def parse_ssr():
    parse = requests.get('https://stopgame.ru/games/filter?rating=izumitelno')
    soup = BeautifulSoup(parse.text, 'html.parser')
    soup_div = soup.find_all('div', class_='caption')
    result_list = []
    for i in soup_div:
        result = i.a.text.lstrip().rstrip()
        if result is not None:
            result_list.append(result)

    return result_list


if __name__ == '__main__':
    for i in parse_ssr():
        print(i)
