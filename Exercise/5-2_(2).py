min_people = 2
max_people = 10
total = 100
memo = {}

def problem(remain_people, sit_people):
    key = str([remain_people, sit_people])
    if key in memo:
        return memo[key]
    if remain_people < 0:
        return 0
    if remain_people == 0:
        return 1
    
    count = 0
    for i in range(sit_people, max_people + 1):
        count += problem(remain_people - i, i)

    memo[key] = count

    return count

print(problem(total, min_people))