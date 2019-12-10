import pprint

import requests
from flask import Blueprint, render_template
from keys import KAKAO_REST_KEY

KAKAO_BASE_URL = 'https://dapi.kakao.com'
header = {'Authorization' : 'KakaoAK ' + KAKAO_REST_KEY}

news_blueprint = Blueprint('news', __name__)


@news_blueprint.route('/main')
def news_main():
    return 'welcome news {0}'.format("SOA news main")


@news_blueprint.route('/sports')
def news_sports():
    return 'welcome sports news {0}'.format("SOA Sports")


@news_blueprint.route('/images')
def books():
    res = requests.get(
        url=KAKAO_BASE_URL + '/v2/search/image?query=파이썬',
        headers=header
    )

    if res.status_code == 200:
        docs = res.json()
        images = []
        for image in docs['documents']:
            images.append(image['image_url'])
    else:
        print("Error : {0}".format(res.status_code))

    return render_template(
        'images.html',
        images=images,
        nav_menu='image'
    )


@news_blueprint.route('/books')
def images():
    res = requests.get(
        url=KAKAO_BASE_URL+'/v3/search/book?target=title&query=미움받을 용기',
        headers=header
    )

    if res.status_code == 200:
        docs = res.json()
        books = []
        for book in docs['documents']:
            books.append(book)
    else:
        print("Error : {0}".format(res.status_code))

    return render_template(
        'books.html',
        books=books,
        nav_menu='book'
    )



