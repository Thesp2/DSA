def inverted_pyramid():
    num=int(input('Enter the number:'))
    py=[]
    for i in range(num, 0, -1):
        r=" " * (num - i) + "*" * (2 * i - 1)
        py.append(r)

    print(*py, sep="\n")

inverted_pyramid()