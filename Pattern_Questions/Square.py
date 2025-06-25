def star_square():
    num=int(input("Enter the number:"))
    square=[]

    for nu in range(num):
        p='*'* num
        square.append(p)

    print(*square,sep= '\n')

star_square()
# n=int(input("Enter the number:"))
# square=[]

# for num in range(n):
#     p='*'* n
#     square.append(p)

# print(square)