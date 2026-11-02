def scitani(a, b):
    return a + b

soucet =scitani(5, 7)
print("Součet je:", soucet)

soucet2 = scitani(a=15, b=10)
print("Součet je:", soucet)

def delen(a, b):
    if b == 0:
        return "Nelze dělit nulou!"
    else:
        return a / b
print("Dělení je:", delen(a = 10, b = 0))
