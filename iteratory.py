class Licznik:
    def __init__(self, n):
        self.n = n
        self.aktualna = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.aktualna <= self.n:
            wartość = self.aktualna
            self.aktualna += 1
            return wartość
        else:
            raise StopIteration

for liczba in Licznik(5):
    print(liczba)