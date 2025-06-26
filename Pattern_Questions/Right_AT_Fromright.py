def right_angle_triangle():
    num=int(input('Enter the number='))
    tri=[]

    for i in range(1, num+1):
        row=' ' * (num - i) + '*' * (i)
        tri.append(row)

    print(*tri, sep='\n')

right_angle_triangle()