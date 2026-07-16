import math

def cmmdc_trei(a, b, c):
    return math.gcd(math.gcd(a, b), c)

def gaseste_drepte_unice(puncte):
    drepte_unice = set()
    n = len(puncte)
    
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = puncte[i]
            x2, y2 = puncte[j]

            if x1 == x2 and y1 == y2:
                continue
                
            a = y1 - y2
            b = x2 - x1
            c = x1 * y2 - x2 * y1
            
            numitor_comun = cmmdc_trei(a, b, c)
            a //= numitor_comun
            b //= numitor_comun
            c //= numitor_comun
            
            if a < 0 or (a == 0 and b < 0):
                a, b, c = -a, -b, -c
                
            drepte_unice.add((a, b, c))
            
    return list(drepte_unice)

puncte_test = [(0, 0), (1, 1), (2, 2), (0, 2)]
rezultat = gaseste_drepte_unice(puncte_test)

print("Dreptele unice găsite (a, b, c):")
for dreapta in rezultat:
    print(f"Forma {dreapta} -> {dreapta[0]}x + {dreapta[1]}y + {dreapta[2]} = 0")