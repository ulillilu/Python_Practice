#finally 구문 사용해 파일 닫기
try:
    file = open("info.txt", "w")
    예외.발생해라()
    file.close()
except Exception as e:
    print(e)
finally:
    file.close()
print("# 파일이 제대로 닫혔는지 확인하기")
print("file.closed:", file.closed)