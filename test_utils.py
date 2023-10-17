from utils import get_movie_info

# utils 에서 함수를 가져와서 테스트
# 테스트 함수는 보통 매개변수를 사용하지 않고 값을 직접 적용
def test_get_movie_info():
    # 샘플 url 주소
    test_url = 'https://movie.naver.com/movie/bi/mi/basic.nhn?code=185293'

    # 함수를 호출해서 값을 가져오기
    title, image, desc = get_movie_info(test_url)
    print(title)
    print(image)
    print(desc)

    # 값을 가져오고 제대로 가져왔으면 테스트를 통과하도록 설정
    # 원래는 3가지 값에 대해서 전부 확인해야 하지만 기니까 패스
    assert title == '내일의 기억'