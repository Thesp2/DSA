def numbered_rat():
    num=int(input('Enter the number:'))
    tri=[]

    for i in range(1, num+1):
        r= str(i) * i
        tri.append(r)

    print(*tri, sep='\n')

numbered_rat()