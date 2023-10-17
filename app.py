# flask 를 사용하는 이유는 간단한 웹을 만드는게 쉬우므로
from flask import Flask, render_template, jsonify, request
# render_template 는 html, jsonify 는 json 출력에 사용

from utils import get_movie_info

app = Flask(__name__)

# mongodb 를 사용하는 이유는 연습이므로 코드가 짧은 것을 선택
from pymongo import MongoClient

# mongodb 사용 준비
client = MongoClient('127.0.0.1') # db 이름 사용
db = client.whdgh

# 메인 페이지
@app.route("/")
def home():
    # templates 디렉토리의 파일을 출력
    return render_template('index.html')

# json 
@app.route('/memo', methods=['GET'])
def listing():
    articles = list(db.articles.find({}, {'_id':False}))
    return jsonify({'all_articles': articles})

@app.route('/memo', methods=['POST'])
def saving():
    url_receiver = request.form['url_give']
    comment_receive = request.form['comment_give']

    title, image, desc = get_movie_info(url_receiver)

    # mongodb 에는 dict 를 만들어서 저장하면 됨
    # 여기는 dict 생성
    doc = {
        'title' : title,
        'image' : image,
        'desc' : desc,
        'url' : url_receiver,
        'comment' : comment_receive
    }
    # db에 저장
    db.articles.insert_one(doc)

    return jsonify({'msg' : '저장 완료'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)