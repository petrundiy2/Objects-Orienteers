class Point():
    def __init__(self,x=0,y=0):
        self.x = str(x)
        self.y = str(y)
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    def __str__(self):
        return self.x  + self.y
A=Point(0,0)
print(A)
