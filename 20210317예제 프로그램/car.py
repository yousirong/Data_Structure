class Car:
    def __init__(self, color, speed, gear):  # 초기화 (객체가 생성되면 수행) 
        self.color = color
        self.speed = speed
        self.gear = gear
        
    def speedUp(self, s):   # 속도 증가
        self.speed += s
        
    def speedDown (self, s):  # 속도 감소
        self.speed -= s

    def getColor(self): # 색을 반환
        return self.color
    
    def getSpeed(self): # 현재 속도를 반환
        return self.speed
    
    def getGear(self): # 현재 기어 상태를 반환
        return self.gear

myCar = Car('red', 20, 1) # __init__ 호출

myCar.speedUp(30)
print(myCar.getColor())
print(myCar.getSpeed())
