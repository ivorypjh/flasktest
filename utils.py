import requests
from bs4 import BeautifulSoup

def get_movie_info(url):
    # user-agent 는 접속한 클라이언트의 정보
    headers = {
        'User-Agent': '''mozilla/5.0 (windows nt 10.0; win64; x64) applewebkit/537.36 (khtml, like gecko) chrome/118.0.0.0 safari/537.36'''
    }

    # html 읽어오기
    data = requests.get(url, headers=headers)

    # 파싱 준비
    soup = BeautifulSoup(data.text, 'html.parser')

    # 데이터 파싱
    title = soup.select_one('div.title_area.type_keep._title_area > h2 > span > strong').get_text()
    image = soup.select_one('div.cm_info_box > div.detail_info > a > img')['src']
    description = soup.select_one('div.cm_info_box > div.detail_info > div > span').get_text()

    return title, image, description

