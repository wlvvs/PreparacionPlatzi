import argparse
import logging
import re
import datetime
import csv
import news_page_objects as news
from requests.exceptions import HTTPError
from requests.models import ContentDecodingError
from urllib3.exceptions import MaxRetryError
from common import config

logging.basicConfig(level=logging.INFO)
is_well_formed_url= re.compile(r'^https?://.+/.+$')
is_root_path = re.compile(r'^/.+$')
logger = logging.getLogger(__name__)

def _news_scraper(news_site_uid):
    host = config()['news_sites'][news_site_uid]['url']

    logging.info('Beginning scraper for {}'.format(host))
    logging.info('Finding links in homepage...')

    homepage = news.HomePage(news_site_uid, host)

    articles = []
    for link in homepage.article_links:
        article = _fetch_article(news_site_uid, host, link)

        if article:
            logger.info('Article fetched!')
            articles.append(article)

    _save_articles(news_site_uid, articles)


def _save_articles(news_site_uid, articles):
    now = datetime.datetime.now().strftime('%Y_%m_%d')
    out_file_name = '{news_site_uid}_{datetime}_articles.csv'.format(
        news_site_uid = news_site_uid,
        datetime = now
    )
    dir_news = './files/{}'
    csv_headers = list(filter(lambda property: not property.startswith('_'), dir(articles[0])))

    with open(dir_news.format(out_file_name), mode = 'w+', encoding = 'utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(csv_headers)

        for article in articles:
            row = [str(getattr(article, prop)) for prop in csv_headers]
            writer.writerow(row)


def _fetch_article(news_site_uid, host, link):
    logger.info('Start fetching article at {}'.format(link))

    article = None
    try:
        article = news.ArticlePage(news_site_uid, _build_link(host, link))
    except (HTTPError, MaxRetryError, ContentDecodingError) as e:
        logger.warn('Error while fetching article!', exc_info = False)

    if article and not article.body:
        logger.warn('Invalid article. There is no body.')
        return None

    return article


def _build_link(host, link):
    if is_well_formed_url.match(link):
        return link
    elif is_root_path.match(link):
        return '{host}{uri}'.format(host=host, uri=link)
    else:
        return '{host}/{uri}'.format(host=host, uri=link)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    news_site_choices = list(config()['news_sites'].keys())
    parser.add_argument('news_site',
                        help='The news site that you want to scrape',
                        type=str,
                        choices=news_site_choices)

    args = parser.parse_args()
    _news_scraper(args.news_site)