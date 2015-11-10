N=int(input())
class Point:
        def __init__(self, x = 0, y = 0):
            self.x = x
            self.y = y
        def __add__(self, other):
            return Point(self.x + other.x, self.y + other.y)
        def __mul__(self, other):
            return Point(self.x*other.x,self.y*other.y)
m=0
O=Point(0,0)
for x in range(N):
    A=Point(int(input()),int(input()))
    if A.x*A.x+A.y*A.y>m:
        m=A.x*A.x+A.y*A.y
        O=A
print(O.x,O.y)
