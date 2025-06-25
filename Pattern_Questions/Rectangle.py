def ractangle():
    num1=int(input("The number of rows in the rectangle:"))
    num2=int(input("The number of columns in the rectangle:"))
    Rect=[]
    for i in range(num1):
        r='*'*num2
        Rect.append(r)
            
    print(*Rect,sep='\n')

ractangle()