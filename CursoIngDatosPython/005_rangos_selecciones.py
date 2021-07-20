from icecream import ic
import pandas as pd

# pd.options.display.max_rows = 5 # Delimita los resultados en pantalla

def run():
    geeks = pd.read_csv('./web_scraper/files/geeks_2021_07_20_articles.csv')
    ic(geeks.info())
    ic(geeks)

    ic(geeks['title'])
    ic(geeks.iloc[1:4])
    ic(geeks.iloc[5]['title'])
    ic(geeks.iloc[:6, 0])
    ic(geeks.loc[:, 'body':'title'])


if __name__ == '__main__':
    run()