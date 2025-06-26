def sandglass():
    num=int(input('Enter the number:'))
    tri=[]
    
    for i in range(num, 0, -1):
        lower=' ' * (num - i) + '*' * (2 * i - 1)
        tri.append(lower)
    
    for i in range(1, num):
        upper= ' '*(num - i - 1) + '*' * (2 * i + 1)
        tri.append(upper)
    
    print(*tri,sep='\n')

sandglass()