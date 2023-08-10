def gcd(a, b):
    if (a % b == 0):
        return b
    else:
        return gcd(b, a%b)

class Fraction:
    def __init__(self,numer = 0, denom = 1):
        self.numer = numer
        self.denom = denom
        if self.denom < 0:
            self.numer *= -1
            self.denom *= -1        
        self.reduce();

    def printFraction(self):
        print(self.numer,"/",self.denom)

    def reduce(self):
        g = gcd(abs(self.numer), abs(self.denom))
        self.numer //= g
        self.denom //= g    
    
    def add(self, f):
        result = Fraction()
        result.denom = self.denom * f.denom
        result.numer = self.numer*f.denom + self.denom*f.numer
        if result.denom < 0:
            result.numer *= -1
            result.denom *= -1 
        if result.numer == 0:
            result.denm = 1
        else:
            result.reduce()
        return result

f1 = Fraction(5,-4)  # 5/-4
f2 = Fraction(3,4)   # ¾

f3 = f1.add(f2)

f3.printFraction()
f1.printFraction()
