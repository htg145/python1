# 상속: 부모 클래스 의 속성과 메소드 를 자식 클래스 가 물려 받음
# super: 부모 클래스, Sub: 자식 클래스
# 메소드 오버 라이딩
# 다중 상속

# class Animal:  # 부모 클래스
#     def __init__(self, name):
#         self.name = name # 공통 속성
#     def eat(self):
#         print(f"{self.name}가 밥을 먹습 니다.")
# class Dog(Animal):  # 자식 클래스
#         def bark(self):
#             print(f"{self.name}가 멍멍 짖습 니다.")

# super() # 슈퍼 클래스 부모를 호출 하는것

# 메소드 오버 라이딩
# 부모 클래스 의 메소드 를 자식 클래스 에서 재정의(Overriding)하는 것
# 같은 이름의 메소드 를 자식 클래스 에서 다시 정의 하여 동작을 변경 하는 것

# 다중 상속
# 두 개 이상의 부모 클래스 로 부터 속성과 메소드 를 상속 받는 것
# 즉, 자식 클래스 가 여러 부모 클래스 로 부터 기능을 물려 받을 수 있음

# 상속

# class Parent:
#     def introduce(self):
#         print("저는 부모 입니다.")
#
# class Child(Parent):
#     def introduce(self):
#         print("저는 자식 입니다.")
#
# child = Child()
# child.introduce()

# class Car:
#     def __init__(self, model, price):
#         self.model = model
#         self.price = price
#
#     def drive(self):
#         print(f"{self.model}가 앞으로 전진 합니다.")
#
# class ElecCar(Car):
#     def __init__(self, model, price, energy_efficiency):
#         super().__init__(model, price)
#         self.energy_efficiency = energy_efficiency
#
#     def drive(self):
#         super().drive() # 부모 클래스 의 메소드 를 그대로 호출
#         print(f"{self.model}가 전기로 전진 합니다.") # 오버 라이딩 됨
#
# ev6 = ElecCar("ev6", "5000", "60kwh")
# ev6.drive()

# 다단계 상속

# class GrandParent:
#     def introduce(self):
#         print("우리는 할머니 할아버지")
#
# class Parent(GrandParent):
#     def introduce(self):
#         super().introduce()
#         print("우리는 엄마 아빠")
#
# class child(Parent):
#     def introduce(self):
#         super().introduce()
#         print("우리는 자식")
#
# child = child()
# child.introduce()

# child.work()
# child.study()

# 다중 상속

# class Father:
#     def drive(self):
#         print("운전을 잘함")
#
# class Mother:
#     def cook(self):
#         print("요리를 잘함")
#
# class Child(Father, Mother):
#     def study(self):
#         print("공부를 잘함")
#
# child1 = Child()
# child1.drive()
# child1.cook()
# child1.study()

# class Animal:
#     def breathe(self):
#         print("숨을 쉴 수 있어요")
#
# class Swimmer:
#     def swim(self):
#         print("헤엄을 칠 수 있어요")
#
# class Fish(Animal, Swimmer):
#     pass
#
# nimo = Fish()
# nimo.swim()
# nimo.breathe()

# class GrandParent:
#     def smart(self):
#         print("똑똑 해요")
#
# class Father:
#     def doctor(self):
#         print("나는 의사")
#
# class Mother:
#     def rich(self):
#         print("나는 부자")
#
# class Child(GrandParent, Father, Mother):
#     pass
#
# child = Child()
# child.rich()
# child.smart()
# child.doctor()

# class A:
#     def introduce(self):
#         print("나는 A")
#
# class B:
#     def introduce(self):
#         print("나는 B")
#
# class C:
#     def introduce(self):
#         print("나는 C")
#
# class Child(A, B, C):
#     def introduce(self):
#         print(Child.mro())
#         super().introduce() # MRO 에 따라 첫 번째 순서 대로 정의
#         super(A, self).introduce()
#         C.introduce(self)
#
# child = Child()
# child.introduce()

# MRO 개념
# => 메소드 결정 순서

# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#
#     def start(self):
#         print(f"{self.brand}의 {self.model}가 시동을 겁니다.")
#
#     def stop(self):
#         print(f"{self.brand}의 {self.model}가 정지 합니다.")
#
# class ElectricCar(Car):
#     def __init__(self, brand, model, battery_capacity):
#         super().__init__(brand, model)
#         self.battery_capacity = battery_capacity
#
#     def charge(self):
#         print(f"{self.brand}의 {self.model}가 배터리 를 충전 합니다.")
#
# class GasolineCar(Car):
#     def __init__(self, brand, model, fuel_tank_capacity):
#         super().__init__(brand, model)
#         self.fuel_tank_capacity = fuel_tank_capacity
#
#     def refuel(self):
#         print(f"{self.brand}의 {self.model}가 연료를 주유 합니다.")
#
# class HybridCar(ElectricCar, GasolineCar):
#     def __init__(self, brand, model, battery_capacity, fuel_tank_capacity):
#         ElectricCar.__init__(self, brand, model, battery_capacity)
#         GasolineCar.__init__(self, brand, model, fuel_tank_capacity)
#
#     def switch_mode(self, mode):
#         if mode == "electric":
#             print(f"{self.brand}의 {self.model}가 전기 모드로 전환 됩니다.")
#         elif mode == "gasoline":
#             print(f"{self.brand}의 {self.model}가 내연 기관 모드로 전환됨.")
#
# hybrid_car = HybridCar("Toyota", "Prius", 100, 50)
# hybrid_car.start()
# hybrid_car.charge()
# hybrid_car.refuel()
# hybrid_car.switch_mode("electric")
# hybrid_car.stop()

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start(self):
        print(f"{self.brand}의 {self.model}가 시동을 겁니다.")

    def stop(self):
        print(f"{self.brand}의 {self.model}가 정지 합니다.")

class ElectricCar:
    def __init__(self, battery_capacity):
        self.battery_capacity = battery_capacity

    def charge(self):
        print(f"배터리 를 충전 합니다.")

class GasolineCar:
    def __init__(self, fuel_tank_capacity):
        self.fuel_tank_capacity = fuel_tank_capacity

    def refuel(self):
        print(f"연료를 주유 합니다.")

class HybridCar(Car, ElectricCar, GasolineCar):
    def __init__(self, brand, model, battery_capacity, fuel_tank_capacity):
        Car.__init__(self, brand, model)
        ElectricCar.__init__(self, battery_capacity)
        GasolineCar.__init__(self, fuel_tank_capacity)

    def switch_mode(self, mode):
        if mode == "electric":
            print(f"{self.brand}의 {self.model}가 전기 모드로 전환 됩니다.")
        elif mode == "gasoline":
            print(f"{self.brand}의 {self.model}가 내연 기관 모드로 전환됨.")

    def charge(self):
        ElectricCar.charge(self)

    def refuel(self):
        GasolineCar.refuel(self)

hybrid_car = HybridCar("Toyota", "Prius", 100, 50)
hybrid_car.start()
hybrid_car.charge()
hybrid_car.refuel()
hybrid_car.switch_mode("electric")
hybrid_car.stop()

# mro 문제가 생김

# 내가 원하는 답
# 차
# 전기차(차), 내연 기관차(차)
# 하이 브리드 (전기차, 내연 기관차)
# __init__

# mro 문제 고치기 어렵다. 다중 상속을 했을때 mro 문제 발생

# mro 하이 브리드 - 전기차 - 내연 기관 - 차 - 객체 # 전기차 를 찍었 는데 내연 기관 이라고 뜬다
# 해결법 : 전기차, 내연 기관 상속 없애









