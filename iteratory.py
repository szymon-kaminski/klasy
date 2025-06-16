class Licznik:
    def __init__(self, n):
        self.n = n
        self.aktualna = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.aktualna <= self.n:
            wartosc = self.aktualna
            self.aktualna += 1
            return wartosc
        else:
            raise StopIteration

for liczba in Licznik(5):
    print(liczba)

########################################################
########################################################
print()
print("Parzyste do N")

class ParzysteDoN:
    def __init__(self, n):
        self.n = n
        self.aktualna = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.aktualna <= self.n:
            wartosc = self.aktualna
            self.aktualna += 2
            return wartosc
        else:
            raise StopIteration
        
for liczba in ParzysteDoN(10):
    print(liczba)