class Point2D:
    tipo='Topografia'
    def __init__(self, x, y):
        #variables de instancia
        #disponibles en toda la clase con self.variable
        self.x=None
        self.y=None

        self.setX(x)
        self.setY(y)

    #setter--> Comprueban datos de entrada
    def setX(self,x)->float:
        self.x=self._checkValue(x)
        return self.x
    #setter
    def setY(self,y)->float:
        self.y=self._checkValue(y)
        return self.y
    
    def printCoordinates(self):
        a=10 #variables locales. Solo viven aquí
        b=20
        c=a+b
        print(f"({self.x}, {self.y})")

    def translate(self, dx, dy)->list:
        self.x =self.x + dx
        self.y = self.y + dy
        return self.getAsList()
    
    def getAsList(self)->list:
        return [self.x, self.y]
    
    def getAsDict(self)->dict:
        return {'x':self.x, 'y': self.y}
    
    
    #método privado. Empieza por __
    def _checkValue(self, value):
        try:
            value=float(value)
        except Exception:
            raise Exception('The text is not convertible in to number')
        if value<0:
            raise Exception("Negative values are not allowed")
        return value

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
class Point3D(Point2D):
    def __init__(self, x, y, z):
        self.z=None
        super().__init__(x, y)
        #no usar __ para los métodos privados
        #usar solo _
        self.z=self._checkValue(z)
    def getAsList(self):
        l = super().getAsList()
        l.append(self.z)
        return l
        
    def getAsDict(self):
        d=super().getAsDict()
        d['z']=self.z
        return d
        return {**super().getAsDict(),'z':self.z}

"""
Define a class called TwoPointOperator.
The constructor receives two points 2d and has tree methods:
    sum() --> returns a point with the x and y as the 
        sum of the x and y of the two points.
    substract() --> returns a point 2d with the x and y of 
        the pt1 - x e y of the pt2
    average() --> Returns a point 2d with the average of the 
        coordinates of both points
"""  
class TwoPointOperator():
    def __init__(self, pt1:Point2D, pt2:Point2D):
        self.pt1=pt1
        self.pt2=pt2
    def sum(self)->Point2D:
        return Point2D(self.pt1.x + self.pt2.x, self.pt1.y + self.pt2.y)
    def substract(self)->Point2D:
        return Point2D(self.pt1.x - self.pt2.x, self.pt1.y - self.pt2.y)
    def average(self)->Point2D:
        ptSum:Point2D = self.sum()
        return Point2D(ptSum.x/2, ptSum.y/2)

if __name__=="__main__":
#    p=Point3D(1,2,3) 
#    print(p.getAsDict())  
#    print(p.getAsList())  
    pt1=Point2D(50,50)
    pt2=Point2D(20,30)
    po=TwoPointOperator(pt1,pt2)
    s=po.sum()
    s.printCoordinates()
    subs=po.substract()
    subs.printCoordinates()
    avg=po.average()
    avg.printCoordinates()
    
