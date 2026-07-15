def diagonala_principala_descrescator(matrice: list[list[float | int]]):
    diagonala = []

    n = len(matrice)
    
    for i in range(n):
        diagonala.append(matrice[i][i])

    diagonala.sort(reverse=True)
    
    return diagonala

matrice_test = [
    [3, 5, 9],
    [1, 8, 2],
    [7, 4, 2]
]

rezultat = diagonala_principala_descrescator(matrice_test)
print("Diagonala sortată descrescător:", rezultat)
