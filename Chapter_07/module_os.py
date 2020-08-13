#os 모듈
import os

print("현재 운영체제:", os.name)
print("현재 폴더:", os.getcwd())
print("현재 폴더 내부의 요소:", os.listdir())

#폴더가 비어있는 경우 폴더 생성 및 제거
os.mkdir("hello")
os.rmdir("hello")

with open("original.txt", "w") as file:
    file.write("hello")
os.rename("original.txt", "new.txt")

os.remove("new.txt")

os.system("dir")

