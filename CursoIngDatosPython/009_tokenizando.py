from icecream import ic
import pandas as pd
import hashlib
from urllib.parse import urlparse
import nltk
from nltk.corpus import stopwords


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

    stripped_title = (hipertextual
        .apply(lambda row: row['title'], axis = 1)
        .apply(lambda body: list(body))
        .apply(lambda letters: list(map(lambda letter: letter.replace('\t', ''), letters)))
        .apply(lambda letters: list(map(lambda letter: letter.replace('\r', ''), letters)))
        .apply(lambda letters: list(map(lambda letter: letter.replace('\n', ''), letters)))
        .apply(lambda letters: ''.join(letters))
    )

    hipertextual['body'] = stripped_body
    hipertextual['title'] = stripped_title
    stop_words = set(stopwords.words('spanish'))
    
    def tokenize_column(df, column_name):
        return (df
            .dropna()
            .apply(lambda row: nltk.word_tokenize(row[column_name]), axis = 1)
            .apply(lambda tokens: list(filter(lambda token: token.isalpha(), tokens)))
            .apply(lambda tokens: list(map(lambda token: token.lower(), tokens)))
            .apply(lambda word_list: list(filter(lambda word: word not in stop_words, word_list)))
            .apply(lambda valid_word_list: len(valid_word_list))
        )
    hipertextual['n_token_title'] = tokenize_column(hipertextual, 'title')
    hipertextual['n_token_body'] = tokenize_column(hipertextual, 'body')

    ic(hipertextual.info())
    ic(hipertextual)


if __name__ == '__main__':
    """
    nltk.download('punkt')
    nltk.download('stopwords')

    Estos puntos de instalación se ejecutan una sola vez y posteriormente, el
    compilador los toma para utilizarlos
    
    """
    run()