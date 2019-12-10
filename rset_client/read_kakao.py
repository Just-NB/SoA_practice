import requests
import pprint

from keys import KAKAO_REST_KEY

KAKAO_BASE_URL = 'https://dapi.kakao.com'

if __name__ == "__main__":
    header = {'Authorization' : 'KakaoAK ' + KAKAO_REST_KEY}

    res = requests.get(
        url=KAKAO_BASE_URL+'/v3/search/book?target=title&query=미움받을 용기',
        headers=header
    )
    # if res.status_code == 200:
    #     books = res.json()
    #     pprint.pprint(books['documents'])
    #
    #     for book in books['documents']:
    #         # title - author
    #         print("{0:20} - {1:20}".format(book['title'], str(book['authors'])))
    #     # pprint.pprint(books['documents'][0]['title'])
    #     # pprint.pprint(books)
    # else:
    #     print("Error : {0}".format(res.status_code))

    res2 = requests.get(
        url=KAKAO_BASE_URL+'/v2/search/image?query=설현',
        headers=header
    )
    if res2.status_code == 200:
        docs = res2.json()
        # pprint.pprint(docs)
        images = []
        for image in docs['documents']:
            images.append(image['image_url'])

        print(images)
        # pprint.pprint(res2.json())
    else:
        print("Error : {0}".format(res2.status_code))
