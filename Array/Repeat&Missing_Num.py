def repeat_missing_num(arr):
    n=len(arr)
    sn=(n*(n+1))/2
    s2n=(n*(n+1)*((2*n)+1))/6
    s,s2=0,0
    for i in range(n):
        s+=arr[i]
        s2+=(arr[i]*arr[i])

    val1=s-sn
    val2=(s2-s2n)/val1

    x=(val1+val2)/2
    y=x-val1

    print("Repeating Number,Missing Number\n",[int(x),int(y)])
    

numbers=[3,6,3,1,2,4]
result=repeat_missing_num(numbers)
print(result)



