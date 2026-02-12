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
    
class Point3D(Point2D):
    def __init__(self, x, y, z):
        self.z=None
        super().__init__(x, y)
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
        

if __name__=="__main__":
    p=Point3D(1,2,3) 
    print(p.getAsDict())  
    print(p.getAsList())  
