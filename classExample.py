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
- Redefine the methos translate to translate also the z.


"""


