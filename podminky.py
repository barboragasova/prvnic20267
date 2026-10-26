cislo = 0
if cislo > 0:
    print("Hodnota čísla je kladná.")
elif cislo < 0:
    print("Hodnota čísla je záporná.")
else:
    print("Hodnota čísla je nula.")

# jiná varianta (1)

vek = 20
if vek >= 16 and vek < 18:
    print("Jsi mladistvý.")
else:
    print("Jsi plnoletý.")

# jiná varianta (2)

body = 90
chceme_ho = False

if body >= 80:
    if chceme_ho:
        print("Má dost bodů.")
        print("Jooo chceme ho.")
    else:
        print("Má dost bodů.")
        print("ALE NECHCEMEHO - SORRY.")
else:
    print("Nemá dost bodů. - SMŮLA")

# jiná varianta (3)

cislo = 5
# % MODULO, vrací zbytek po dělení
if cislo %2 == 0:
    print("Číslo je sudé.")
else:
    print("Číslo je liché.")

print(7 % 2)

# jiná varianta (4)

nakupni_kosik = []
if nakupni_kosik:
    print("Košík není prázdný.")
else:
    print("Košík je prázdný.")

# jiná varianta (5)

povolene_ovoce = ["jablko", "banán", "pomeranč"]
moje_ovoce = "jablko"
if moje_ovoce in povolene_ovoce:
    print(f"{moje_ovoce.capitalize()} je povolené ovoce.")
else:
    print(f"{moje_ovoce.capitalize()} není na seznamu povoleného ovoce.")