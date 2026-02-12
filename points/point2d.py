class Point2D:
    tipo='Topografia'
    def __init__(self, x, y):
        #variables de instancia
        #disponibles en toda la clase con self.variable
        self.setX(x)
        self.setY(y)

    #setter--> Comprueban datos de entrada
    def setX(self,x):
        self.x=self.__checkValue(x)
    #setter
    def setY(self,y):
        self.y=self.__checkValue(y)

    def printCoordinates(self):
        a=10 #variables locales. Solo viven aquí
        b=20
        c=a+b
        print(f"({self.x}, {self.y})")

    def translate(self, dx, dy):
        self.x =self.x + dx
        self.y = self.y + dy
    
    def getAsList(self):
        return [self.x, self.y]
    
    def getAsDict(self):
        return {'x':self.x, 'y': self.y}
    
    
    #método privado. Empieza por __
    def __checkValue(self, value):
        try:
            value=float(value)
        except Exception:
            raise Exception('The text is not convertible in to number')
        if value<0:
            raise Exception("Negative values are not allowed")
        return value