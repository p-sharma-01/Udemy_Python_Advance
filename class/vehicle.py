class Vehicle:
    def __init__(self):
        self.no_of_tyres=4
        
    def move(self):
        print("I move on road using my tyres.")
class Car(Vehicle):
    def __init__(self):
        super().__init__()
    def drive(self):
        print("I drive my car.")
car=Car()
car.drive()
car.move()
print(car.no_of_tyres)
