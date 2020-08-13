#if 조건문에 else 구문을 추가해서 짝수와 홀수 구분
number = input("정수 입력> ")
number = int(number)

if number % 2 == 0:
    print("짝수입니다.")
else:
    print("홀수입니다.")