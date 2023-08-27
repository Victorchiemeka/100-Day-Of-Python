def add(*agrs):
    sum = 0
    for i in agrs:
        sum += i
    return sum


all = add(2, 4, 2, 1)

print(all)
