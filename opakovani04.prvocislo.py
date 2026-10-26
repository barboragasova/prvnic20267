for i in range(2,10):
    for x in range (2, i):
        print(f"Kontroluji číslo {i} dělitelné {x}")
        if i % x == 0:      #modulo, zbytek pro dělení
            print(f"{i} se rovná {x} * {i//x}, takže není prvočíslo")
            break
    else:
        print(f"{i} je PRVOČÍSLO")