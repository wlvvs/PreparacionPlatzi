from icecream import ic
import pandas as pd
from urllib.parse import urlparse


def run():
    hipertextual = pd.read_csv('./web_scraper/files/hipertextual_2021_07_20_articles.csv')

    hipertextual['newspaper_uid'] = 'hipertextual'
    hipertextual['host'] = hipertextual['url'].apply(lambda url: urlparse(url).netloc)
    missing_titles_mask = hipertextual['title'].isna()
    
    missig_titles = (hipertextual[missing_titles_mask]['url']
                    .str.extract(r'(?P<missing_titles>[^/]+)$')
                    .applymap(lambda title: title.split('-'))
                    .applymap(lambda title_word_list: ' '.join(title_word_list))
                    )
    ic(missig_titles)


if __name__ == '__main__':
    run()