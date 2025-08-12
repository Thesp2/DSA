def sortarray(arra,arrb):
    n=len(arra)
    m=len(arrb)

    gap=(n+m+1)//2

    while gap>0:
        i=0
        j=gap

        while j<n+m:
            if j<n and arra[i]>arra[j]:
                arra[i],arra[j]=arra[j],arra[j]
            elif j>=n and i<n and arra[i]>arrb[j-n]:
                arra[i],arrb[j-n]=arrb[j-n],arra[i]
            elif i>=n and arrb[i-n]>arrb[j-n]:
                arrb[i - n], arrb[j - n] = arrb[j - n], arrb[i - n]
            i+=1
            j+=1
        if gap==1:
            break
        gap=(gap+1)//2

a = [1, 5, 9, 10, 15, 20]
b = [2, 3, 8, 13]
sortarray(a, b)

for ele in a:
    print(ele, end=' ')
print()
for ele in b:
    print(ele, end=' ')