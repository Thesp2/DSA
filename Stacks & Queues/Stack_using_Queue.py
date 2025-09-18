from collections import deque
class mystack:
    def __init__(self):
        self.q=deque()

    def push(self,x:int)->None:
        self.q.append(x)

    def pop(self)->int:
        for i in range(len(self.q)-1):
            self.push(self.q.popleft())
        return self.q.popleft()
    
    def top(self):
        return self.q[-1]
    
    def empty(self):
        return len(self.q)==0

s = mystack()

n = int(input("How many elements to push? "))
for _ in range(n):
    x = int(input("Enter element: "))
    s.push(x)

print("\nTop element:", s.top())
print("Pop element:", s.pop())
print("Top after pop:", s.top() if not s.empty() else "Stack is empty")
print("Is stack empty?", s.empty())