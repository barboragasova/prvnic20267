python_devs = {"Pepa", "Honza", "Marek", "Jirka", "Karel", "Romana", "Petr"}
java_devs = {"Romana", "Petr", "Karel", "Lucie", "Mařka"}

# operace sjednocení (NEBO)
vsichni_devs = python_devs | java_devs
print("Všichni vývojáři (sjednocení):", vsichni_devs)
print(20*"=")

#operace průniku(A)

polygon_devs = python_devs & java_devs
print("Vývojáři, kteří ovládají oba jazyky (průnik):", polygon_devs)

# operace rozdíl (-)

vsichni_devs = python_devs - java_devs
print("Všichni vývojáři (rozdíl):", vsichni_devs)
print(20*"=")