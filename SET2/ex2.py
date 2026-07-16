def este_prim(numar):
    if numar <= 1:
        return False
    
    for i in range(2, int(numar ** 0.5) + 1):
        if numar % i == 0:
            return False 
            
    return True

def filtreaza_numere_prime(lista):
    lista_prime = []
    
    for numar in lista:
        if este_prim(numar):
            lista_prime.append(numar)
            
    return lista_prime

intrare_utilizator = input("Dati numerele separate prin spatiu: ")

numerele_mele = [int(x) for x in intrare_utilizator.split()]

rezultat = filtreaza_numere_prime(numerele_mele)

print(f"Lista inițială: {numerele_mele}")
print(f"Numerele prime găsite: {rezultat}")