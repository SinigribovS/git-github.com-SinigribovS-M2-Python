def sublista_intre_min_max(lista: list[float | int]):
    if not lista:
        return []
    
    valoare_min = min(lista)
    valoare_max = max(lista)
    
    idx_min = lista.index(valoare_min)
    idx_max = lista.index(valoare_max)
    
    start_idx = min(idx_min, idx_max)
    end_idx = max(idx_min, idx_max)
    
    return lista[start_idx : end_idx + 1]

text_introdus = input('Dati lista (cu spații sau virgule): ')
text_curat = text_introdus.replace(',', ' ')
elemente_text = text_curat.split()
listamea = [int(x.strip()) for x in elemente_text]

print("Sublista rezultată este:", sublista_intre_min_max(listamea))