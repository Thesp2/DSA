def floyed_triangle():
    num=int(input("Enter the number:"))
    tri=[]
    temp=1
    for i in range(1, num+1):
        temp_list=[]
        for j in range(i):
            temp_list.append(str(temp))
            temp += 1
        tri.append(' '.join(temp_list))
    print(*tri, sep='\n')

floyed_triangle()