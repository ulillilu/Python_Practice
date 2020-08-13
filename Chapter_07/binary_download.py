#이미지 읽어 들이고 저장하기
from urllib import request

target = request.urlopen("http://www.hanbit.co.kr/images/common/logo_hanbit.png")
output = target.read()
print(output)

#바이너리 쓰기 모드로 출력
file = open("output.png", "wb")
file.write(output)
file.close()