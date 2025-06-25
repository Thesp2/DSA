'''
Enter the number:5
    *  
   *** 
  *****
 *******
*********
'''
def pyramid():
    num=int(input('Enter the number:'))
    tri=[]
    for i in range(num):
        r= ' '*(num - i - 1) + '*'*(2*i+1)
        tri.append(r)

    print(*tri,sep='\n')

pyramid()



        
