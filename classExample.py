class Example():
    mode="edit"
    def __init__(self, var1:int):
        self.var1=var1

    def metodo1(self):
        print("Method 1 from Example")
        print(self.var1)

class Example2(Example):
    def __init__(self, var1, var2):
        super().__init__(var1)
        self.var2=var2

    def metodo1(self):
        super().metodo1()
        print("Method 1 from Example2")
        print(self.var2)

if __name__=="__main__":
    #e1=Example(1)
    #e1.metodo1()
    e2=Example2(1,2)
    e2.metodo1()


"""
Exercise 1.
Create the class point3d that inherits from Point2d and:
- Initialize the father constructor.
- Add the z coordinate
- Add the setZ setter
- Redefine the methods getAsList and getAsDict to return also the z
- Redefine the method translate to translate also the z.
    To redefine you have to use super.method()
"""

"""
Define a class called TwoPointOperator.
The constructor receives two points 2d and has two methods:
    sum() --> returns a point with the x and y as the 
        sum of the x and y of the two points.
    substract() --> returns a point 2d with the x and y of 
        the pt1 - x e y of the pt2
    average() --> Returns a point 2d with the average of the 
        coordinates of both points
"""


