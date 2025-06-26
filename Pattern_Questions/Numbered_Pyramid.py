def num_pyramid():
    num=int(input('Enter the number:'))
    pyramid = []
    
    for i in range(1, num + 1):
        spaces = ' ' * (num - i)
        numbers = ' '.join(str(x) for x in range(1, i + 1))
        pyramid.append(spaces + numbers + spaces)
 
    print(*pyramid, sep='\n')

num_pyramid()