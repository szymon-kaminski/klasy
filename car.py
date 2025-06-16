class Vehicle:
    def start(self):
        print("Pojazd rusza.")
    

    def stop(self):
        print("Pojazd zatrzymuje się.")


class Car(Vehicle):
    def __init__(self):
        self.statusy = [
            "Silnik włączony",
            "Samochód rusza",
            "Samochód jedzie",
            "Samochód hamuje",
            "Samochód zatrzymany",
        ]
        self.index = 0


    def start(self):
        super().start()
        print("Silnik uruchomiony")


    @staticmethod
    def information():
        print("Samochód to czterokołowy pojazd przeznaczony do przewozu osób.")

    
    def __iter__(self):
        self.index = 0
        return self
    

    def __next__(self):
        if self.index < len(self.statusy):
            wynik = self.statusy[self.index]
            self.index += 1
            return wynik
        else:
            raise StopIteration
        

def travel_miles(n):
    for i in range(1, n + 1):
        yield f"Przebyto {i} mile."


car = Car()
car.start()
car.stop()
Car.information()

for komunikat in travel_miles(2):
    print(komunikat)

for status in car:
    print(status)


##############################################################################
##############################################################################
print()
print("drugie rozwiązanie")
class Vehicle:
    def start(self):
        print("Vehicle is starting")

    def stop(self):
        print("Vehicle is stopping")


class Car(Vehicle):
    def start(self):
        super().start()
        print("Engine has started")

    @staticmethod
    def information():
        print("A car is a means of personal transport")

    def travel_miles(self):
        current_mile = 0
        while True:
            yield f"Mile {current_mile}"
            current_mile += 1

    def __iter__(self):
        self.travel_statuses = iter(['Starting', 'In progress', 'Finished'])
        return self

    def __next__(self):
        return next(self.travel_statuses)


# Test

car = Car()
car.start()
car.stop()
car.information()

mile_gen = car.travel_miles()
print(next(mile_gen))
print(next(mile_gen))

for status in car:
    print(status)