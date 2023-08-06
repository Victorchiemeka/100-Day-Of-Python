def main():
    total = decorator(3, 4)
    print(total)


def decorator(a, b):
    sum = a + b
    return sum


main()
