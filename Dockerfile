FROM python:3.8-slim

# 먼저 다운로드를 수행
RUN apt-get update
# dockerfile 의 경우 질문이 나오면 에러가 발생하므로 - y 옵션 사용
RUN apt-get install -y --no-install-recommends

# 작업 디렉토리를 설정하는데 아무 곳이나 상관 없음
WORKDIR /usr/src/app
# 의존성 설정을 가져와서 설치
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .

# 개방할 포트 번호
# 항상 5000번인게 아니라 app.py 파일에서 포트 번호로 5000을 사용했으므로
# 이 번호를 사용 - 어떤 포트를 사용하냐에 따라 다르게 설정해줘야 함
EXPOSE 5000

# 실행 부분
# flask 가 기본으로 사용하는 이름이 app.py 이기 때문에 이렇게 지정이 가능
# flask 의 기본 파일명을 가진 파일을 run 하도록 수행
# -m 과 flask, run 대신 app.py 를 직접 지정해도 됨
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]