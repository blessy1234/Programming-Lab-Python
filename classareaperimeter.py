class rectangle():
    def __init__(self,breadth,length):
        self.breadth=breadth
        self.length=length
    def area(self):
        return self.breadth*self.length
    def perimeter(self):
        return (2*(self.breadth*self.length))
a=int(input("Enter length of 1 rectangle: "))
b=int(input("Enter breadth of 1 rectangle: "))
c=int(input("Enter length of 2 rectangle: "))
d=int(input("Enter breadth of 2 rectangle: "))
obj=rectangle(a,b)
obj1=rectangle(c,d)
print("Area of 1 rectangle:",obj.area(),"and","perimeter of rectangle:",obj.perimeter())
print("Area of 2 rectangle:",obj1.area(),"and","perimeter of rectangle:",obj1.perimeter())
if obj.area()==obj1.area():
    print("both rectangle are same :",obj.area())
elif obj.area()>obj1.area():
    print(" rectangle  one is greater than second  :",obj.area())
else:
    print("second rectangle is greater :",obj1.area())

