from icecream import ic
import pandas as pd
from urllib.parse import urlparse


def run():
    hipertextual = pd.read_csv('./web_scraper/files/hipertextual_2021_07_20_articles.csv')

    hipertextual['newspaper_uid'] = 'hipertextual'
    hipertextual['host'] = hipertextual['url'].apply(lambda url: urlparse(url).netloc)

    ic(hipertextual.head(5))
    ic(hipertextual['host'].value_counts())


if __name__ == '__main__':
    run()