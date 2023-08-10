#  class Calculator
#  data members (attributes) : numCalculator, result, memValue
#  member functions (methods)
#        __init__
#        clear()
#        add(num)
#        currentVal()

class Calculator:
    numCalculators = 0 
    def __init__(self):
        self.result = 0
        self.memValue = 0
        Calculator.numCalculators += 1
        
    def __del__(self): # 소멸자
        Calculator.numCalculators -= 1

   
    def clear(self):
        self.result = 0  # how

    def add(self, num):  
        self.result += num  # how
        return self.result
    
    def currentVal(self):
        return self.result  #how

a = Calculator() # Calculator 인스턴스 만듦
b = Calculator()
print(Calculator.numCalculators)
a.add(30)
print(a.currentVal())
b = a.add(20)
print(b)
print(Calculator.numCalculators)


