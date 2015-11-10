N=int(input())
class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    def __mul__(self, other):
        return Point(self.x*other.x,self.y*other.y)
    def __sub__(self, other):
        return Point(self.x-other.x,self.y-other.y)
T=[]
E=[]
for u in range(N):
    A=Point(int(input()),int(input()))
    T+=str(A.x)
    E+=str(A.y)
i=0
j=0
for x in range(len(T)):
    i+=int(T[x])
    j+=int(E[x])
print(i/N,j/N)
