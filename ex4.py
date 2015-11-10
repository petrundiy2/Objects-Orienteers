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
m=0
k=0
n=0
for u in range(len(T)):
    for v in range(len(T)):
        for b in range(len(T)):
            if u!=v and u!=b and v!=b:
                k+=((int(T[u])-int(T[v]))**2+(int(E[u])-int(E[v]))**2)**0.5+((int(T[u])-int(T[b]))**2+(int(E[u])-int(E[b]))**2)**0.5+((int(T[v])-int(T[b]))**2+(int(E[v])-int(E[b]))**2)**0.5
                if k>m:
                    m=k
                k=0
print(m)
