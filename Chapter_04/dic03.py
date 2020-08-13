#딕셔너리에 요소 제거하기
dictionary = {
    "name": "7D 건조 망고",
    "type": "당절임"
}

print("요소 제거 이전:", dictionary)

del dictionary["name"]
del dictionary["type"]

print("요소 제거 이후:", dictionary)