#딕셔너리의 요소에 접근하기
dictionary = {
    "name": "7D 건조 망고",
    "type": "당절임",
    "ingredient": ["망고", "설탕", "메타종아황산나트륨", "치자황색소"],
    "origin": "필리핀"
}

print("name:", dictionary["name"])
print("type:", dictionary["type"])
print("ingredient:", dictionary["ingredient"])
print("origin:", dictionary["origin"])
print()

dictionary["name"] = "8D 건조 망고"
print("name:", dictionary["name"])