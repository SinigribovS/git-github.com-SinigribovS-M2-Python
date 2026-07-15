def medii(lista_numere: list[float | int]):
    if not lista_numere:
        return "Lista este goală", None

    cel_mai_mic = min(lista_numere)
    cel_mai_mare = max(lista_numere)

    media_aritmetica = (cel_mai_mic + cel_mai_mare) / 2

    if cel_mai_mic < 0 or cel_mai_mare < 0:
        return "Nu putem calcula media geometrică (avem numere negative)!", exit
    else:
        media_geometrica = (cel_mai_mic * cel_mai_mare) ** 0.5

    return media_aritmetica, media_geometrica

numerele_mele = [2, 8, 15, 32]
print(medii(numerele_mele))