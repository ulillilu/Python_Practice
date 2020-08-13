#자식 클래스로써 부모의 함수 재정의(오버라이드) 하기
class CustomException(Exception):
    def __init__(self):
        Exception.__init__(self)
        print("#### 오류 생성 ! ####")
    def __str__(self):
        return "오류 발생"

raise CustomException