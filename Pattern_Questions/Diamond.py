def diamond():
    num=int(input('Enter the number:'))
    tri=[]
    for i in range(num):
        upper= ' '*(num - i - 1) + '*'*(2*i+1)
        tri.append(upper)
    
    for i in range(num-1, 0, -1):
        lower=" " * (num - i) + "*" * (2 * i - 1)
        tri.append(lower)

    print(*tri,sep='\n')

diamond()