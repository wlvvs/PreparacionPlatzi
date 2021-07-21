from icecream import ic
import pandas as pd
import hashlib
from urllib.parse import urlparse


def run():
    hipertextual = pd.read_csv('./web_scraper/files/hipertextual_2021_07_20_articles.csv')

    hipertextual['newspaper_uid'] = 'hipertextual'
    hipertextual['host'] = hipertextual['url'].apply(lambda url: urlparse(url).netloc)
    missing_titles_mask = hipertextual['title'].isna()
    
    missig_titles = (hipertextual[missing_titles_mask]['url']
                    .str.extract(r'(?P<missing_titles>[^/]+)/?$')
                    .applymap(lambda title: title.split('-'))
                    .applymap(lambda title_word_list: ' '.join(title_word_list))
                    )
    
    uids = (hipertextual
        .apply(lambda row: hashlib.md5(bytes(row['url'].encode())), axis = 1)
        .apply(lambda hash_object: hash_object.hexdigest())
    )

    hipertextual['uid'] = uids
    hipertextual.set_index('uid', inplace = True)

    stripped_body = (hipertextual
        .apply(lambda row: row['body'], axis = 1)
        .apply(lambda body: list(body))
        .apply(lambda letters: list(map(lambda letter: letter.replace('\t', ''), letters)))
        .apply(lambda letters: list(map(lambda letter: letter.replace('\r', ''), letters)))
        .apply(lambda letters: list(map(lambda letter: letter.replace('\n', ''), letters)))
        .apply(lambda letters: ''.join(letters))
    )
    ic(hipertextual.info())
    ic(hipertextual)
    ic(stripped_body)


if __name__ == '__main__':
    run()