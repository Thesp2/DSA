def hollow_rat():
    num=int(input('Entrt the number:'))
    Tri=[]

    for i in range(1, num+1):
        if i==1 or i==2 or i==num:
            Tri.append('*'*i)
        else:
            row='*'+' '*(i-2) + '*'
            Tri.append(row)
    print(*Tri,sep='\n')

hollow_rat()