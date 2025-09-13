class twostacks:
    def __init__(s,n):
        s.size=n
        s.arr=[0]*n
        s.top1=-1
        s.top2=n

    def push1(s,x):
        if s.top1<s.top2-1:
            s.top1+=1
            s.arr[s.top1]=x
    
    def push2(s,x):
        if s.top1<s.top2-1:
            s.top2-=1
            s.arr[s.top2]=x

    def pop1(s):
        if s.top1>0:
            x=s.arr[s.top1]
            s.top1-=1
            return x
        return -1
    
    def pop2(s):
        if s.top2<s.size:
            x=s.arr[s.top2]
            s.top2+=1
            return x
        return -1
    
ts = twostacks(5)
ts.push1(2)
ts.push1(3)
ts.push2(4)
print(ts.pop1(), end=' ')
print(ts.pop2(), end=' ')
print(ts.pop2(), end=' ')
    

    