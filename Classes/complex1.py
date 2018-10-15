import math

class Complex:
    'This is for Complex Numbers'
    def __init__(self, real = 0 ,img = 0):
        if(type(real) not in (int,float) or type(img) not in (int,float)):
            raise Exception('These are not numbers')
        self.__real = real
        self.__img = img

    def GetReal(self):
        return self.__real

    def GetImg(self):
        return self.__img

    def GetModulus(self):
        return math.sqrt(self.GetReal()*self.GetReal() + self.GetImg()* self.GetImg())

    def GetPhi(self):
        return math.atan2(self.GetImg(),self.GetReal())

    def SetReal(self,Val):
        if type(val) not in (int,float):
            raise Exception("Error for type in Set real")
        self.__real = Val

    def SetImg(self,Val):
        if type(val) not in (int,float):
            raise Exception("Error for type in Set IMG")
        self.__img = Val

    def __str__(self):
        return (str(self.GetReal()) + '+' + str(self.GetImg()) + 'i')
    def __add__(self, other):
        return Complex(self.GetReal() + other.GetReal(),self.GetImg()+ other.GetImg())

try:
    c = Complex(-3,4)
    d = Complex(-1,2)
    print (c + d)
except Exception as e:
    print(e)
