'''
ENter the number=5
*****
****
***
**
*
'''

def inverted_rat():
    num=int(input('Enter the number:'))
    tri=[]

    for i in range(num, 0, -1):
        r='*'*i
        tri.append(r)

    print(*tri,sep='\n')

inverted_rat()