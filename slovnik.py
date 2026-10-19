# Slovník

kontakty = {
    "jmeno": "Jan",
    "prijmeni": "Novák",
    "vek": "30",
    "mesto": "Praha",
    "email": "jan.novak@email.com",
    "telefon": "123456789"
}

#proměny

print(f"Původní kontakty: {kontakty}")
print(f"Jméno: {kontakty['jmeno']}")

kontakty["vek"] = "66"
print(kontakty["vek"])

kontakty["mesto"] = "Ostrava"
print(kontakty)

telefon = kontakty.get("telefon")
print("Telefoní číslo:", telefon)
