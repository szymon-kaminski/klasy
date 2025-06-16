def dekorator(funkcja):
    def opakowanie():
        print("Coś przed funkcją")
        funkcja()
        print("Coś po funkcji")
    return opakowanie

@dekorator
def przywitaj():
     print("Cześć!")

przywitaj()

###################################################
###################################################
print()
print("Przykład mierzenie czasu")

import time

def czas_dzialania(funkcja):
    def opakowanie(*args, **kwargs):
        start = time.time()
        wynik = funkcja(*args, **kwargs)
        koniec = time.time()
        print(f"Czas wykonania: {koniec - start:.4f}s")
        return wynik
    return opakowanie

@czas_dzialania
def licz_do_miliona():
    suma = sum(range(1000000))
    return suma

licz_do_miliona()

##################################################
print()
def dodawanie(funkcja):
    def opakowanie(*args, **kwargs):
        print("start")
        wynik = funkcja(*args, **kwargs)
        print("Wynik:", wynik)
        print("koniec")
        return wynik
    return opakowanie

@dodawanie
def dodaj(a, b):
    return a + b

wynik = dodaj(7, 12)

