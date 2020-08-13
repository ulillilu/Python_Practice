numbers = [273, 103,5, 32, 65, 9, 72, 800, 99]

for number in numbers:
    if number % 2 == 0:
        print("{}는 짝수입니다.".format(number))
    else:
        print("{}는 홀수입니다.".format(number))

print()

for number_1 in numbers:
    if number_1 < 10:
        print("{}는 1자릿수 입니다.".format(number_1))
    elif number_1 < 100:
        print("{}는 2자릿수 입니다.".format(number_1))
    elif number_1 < 1000:
        print("{}는 3자릿수 입니다.".format(number_1))
