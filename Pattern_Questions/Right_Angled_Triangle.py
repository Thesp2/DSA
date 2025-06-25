'''
Expected output
Enter the number:5
*
**
***
****
*****
'''

def right_angled_triangle():
    num=int(input('Entrt the number:'))
    Tri=[]

    for i in range(num):
        r='*'*(i+1)
        Tri.append(r)

    print(*Tri,sep='\n')

right_angled_triangle()