import math 

def largest_divisor(*numere):
    if not numere:
        return None
    
    num_list = list(numere)

    result = num_list.pop(0)

    while len(num_list) > 0 :
        next_number = num_list.pop(0)
        result = math.gcd(result, next_number)

    return result

teste = [
    {"nume": "Fără parametri", "intrari": (), "asteptat": None},
    {"nume": "Un singur număr", "intrari": (7,), "asteptat": 7},
    {"nume": "Prime între ele", "intrari": (8, 9), "asteptat": 1},
    {"nume": "Cazul normal", "intrari": (12, 18, 24), "asteptat": 6},
    {"nume": "Numere negative", "intrari": (-12, -18, 24), "asteptat": 6},
    {"nume": "Cu numărul zero", "intrari": (0, 12, 18), "asteptat": 6},
    {"nume": "Doar zerouri", "intrari": (0, 0, 0), "asteptat": 0},
    {"nume": "Numere identice", "intrari": (5, 5, 5), "asteptat": 5},
    {"nume": "Numere mari", "intrari": (100000, 150000), "asteptat": 50000},
]

for i, test in enumerate(teste, 1):
    rezultat_obtinut = largest_divisor(*test["intrari"])
    succes = rezultat_obtinut == test["asteptat"]
    rez = "YES" if succes else "NO"
    
    print(f"Testul {i} [{test['nume']}]: {rez}")
    print(f"   In: {test['intrari']}")
    print(f"   Out: {rezultat_obtinut} | Așteptat: {test['asteptat']}\n")

print("Toate testele au fost finalizate!")