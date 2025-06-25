def Hollow_Square():
    num=int(input("Entert the number:"))
    Square=[]
    for i in range(num):
        if i==0 or i==(num-1):
            s='*'*num
            Square.append(s)
        
        else:
            r='*'+' '*(num-2)+'*'
            Square.append(r)
    print(*Square,sep='\n')

Hollow_Square()