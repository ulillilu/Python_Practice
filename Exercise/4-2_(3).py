from collections import Counter

numbers = [1, 2, 6, 8, 7, 5, 9, 5, 6, 7, 9, 2, 6, 7, 3, 1, 5, 8]
counter = {}
count = Counter(numbers)

for number in numbers:
    counter[number] = count[number]

print(counter)