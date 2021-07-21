from icecream import ic
import pandas as pd
import matplotlib.pyplot as plt


def run():
    hipertextual1 = pd.read_csv('./web_scraper/files/clean_hipertextual_2021_07_20_articles.csv')
    hipertextual2 = pd.read_csv('./web_scraper/files/clean_hipertextual_2021_07_21_articles.csv')
    hipertextual = pd.concat([hipertextual1, hipertextual2])
    ic(hipertextual)
    ic(hipertextual.describe())
    hipertextual.drop_duplicates(subset=['title'], keep = 'first', inplace = True)
    ic(hipertextual)
    ic(hipertextual.describe())

    genbeta1 = pd.read_csv('./web_scraper/files/clean_genbeta_2021_07_20_articles.csv')
    genbeta2 = pd.read_csv('./web_scraper/files/clean_genbeta_2021_07_21_articles.csv')
    genbeta = pd.concat([genbeta1, genbeta2])
    ic(genbeta)
    ic(genbeta.describe())
    genbeta.drop_duplicates(subset=['title'], keep = 'first', inplace = True)
    ic(genbeta)
    ic(genbeta.describe())

    hipertextual['n_tokens_title'].plot(style = 'k.')
    genbeta['n_tokens_title'].plot(style = 'r.')
    plt.show()

    hipertextual['n_tokens_body'].plot(style = 'k.')
    genbeta['n_tokens_body'].plot(style = 'r.')
    plt.show()

    all_news = pd.concat([hipertextual, genbeta])
    grouped = all_news.groupby('newspaper_uid')
    grouped.hist()
    plt.show()

    ic(grouped['n_tokens_body'].agg(['min', 'mean', 'max']))
    grouped.plot()
    plt.show()


if __name__ == '__main__':
    run()