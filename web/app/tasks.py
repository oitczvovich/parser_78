import json
import hashlib
import datetime
import os
import requests_cache
import sqlite3
from bs4 import BeautifulSoup
from requests_html import HTMLSession
from celery import shared_task
from dotenv import load_dotenv
import os


load_dotenv()
URL_FOR_SLUG = os.getenv('URL_FOR_SLUG')
URL_FOR_POST = os.getenv('URL_FOR_POST')
VARIABLES = os.getenv('VARIABLES')


def get_slug_articles(url):
    query = """
        query newsViewer_Query($newsSection: ID!) {
        newsViewer: viewer {
            ...NewsgroupList_viewer_B1myn
            id
        }
        }

        fragment NewsgroupList_viewer_B1myn on Viewer {
        sideArticles: articles(first: 13, section: $newsSection, d: false, h: false, hidden: false) {
            edges {
            node {
                ...homeNewsListItem
            }
            }
        }
        }

        fragment homeNewsListItem on Article {
        slug
        availableAt
        }
    """
    session = HTMLSession()
    response = session.post(
        url=url,
        json={
            "query": query,
            "variables": {"newsSection": VARIABLES}
            }
        )
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['newsViewer']['sideArticles']['edges']
        with open('parser.json', 'w') as file:
            json.dump(posts, file)
    else:
        print("Ошибка соединения")


def get_post():
    with open('parser.json', 'r') as file:
        news = json.load(file)
        for new in news:
            date_post = new['node']['availableAt']
            date_create = convert_to_unix_timestamp(date_post)
            slug = new['node']['slug']
            session = requests_cache.CachedSession()
            post_url = f'{URL_FOR_POST}/{date_post[:10]}/{slug}'
            post_id = create_hash_id(data=post_url)
            response = session.get(post_url)
            response.encoding = 'utf-8'
            soup = BeautifulSoup(response.text, 'lxml')
            post_title = soup.find('h1').text
            post_text = str(soup.find('div', attrs={'class': 'news__inner'}))

            conn = sqlite3.connect('posts.sqlite3')
            cursor = conn.cursor()
            cursor.execute("SELECT MAX(date_create) FROM app_post")
            first_record = cursor.fetchone()
            if first_record is None:
                first_record = 0
            else:
                first_record = int(first_record[0])
            if date_create > first_record:
                cursor.execute('''
                    INSERT INTO app_post (
                        post_id,
                        post_url,
                        post_title,
                        post_text,
                        date_create
                        )
                    VALUES (?, ?, ?, ?, ?)
                ''', (post_id, post_url, post_title, post_text, date_create))

                conn.commit()
                conn.close()
            conn.close()


def create_hash_id(data):
    """Создание ID с помощью хэширования на основе ссылки на новость."""
    post_id = hashlib.md5(data.encode()).hexdigest()
    return post_id


def convert_to_unix_timestamp(date_string):
    dt = datetime.datetime.fromisoformat(date_string)
    timestamp = dt.timestamp()
    return int(timestamp)


@shared_task()
def main():
    get_slug_articles(url=URL_FOR_SLUG)
    get_post()
