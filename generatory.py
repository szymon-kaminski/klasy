def licz_od_1_do(n):
    for i in range(1, n + 1):
        yield i

for liczba in licz_od_1_do(5):
    print(liczba)

# Przykład 2:
print()
def parzyste_do(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

gen = parzyste_do(10)
for x in gen:
    print(x)

#####################################################
#####################################################
print()
def czy_pierwsza(x):
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5)+1):
        if x % i == 0:
            return False
    return True

def liczby_pierwsze_do(n):
    for liczba in range(2, n + 1):
        if czy_pierwsza(liczba):
            yield liczba

for liczba in liczby_pierwsze_do(100):
    print(liczba)
    
