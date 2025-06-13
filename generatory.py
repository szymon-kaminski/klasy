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
