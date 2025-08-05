class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def sum(self,p):
        return Point((self.x+p.x),(self.y+p.y))

    def print_pint(self):
        print(f"X is {self.x} and Y is {self.y}")    

    def __add__(self,p):
        return Point((self.x+p.x),(self.y+p.y))
p1 = Point(3,2)
p2 = Point(6,3)

p = p1.sum(p2)
p.print_pint()

# p3 = p1+p2 we can't do

p3 = p1+p2 # We overloaded the + Operator by wrting __add__function
p3.print_pint()