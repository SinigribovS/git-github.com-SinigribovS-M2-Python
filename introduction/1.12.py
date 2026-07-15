def slicing_minmax(lista:list[float | int]):

    slice = len(lista)//2

    prima_jumatate=lista[:slice]
    a_doua_jumatate=lista[slice:]

    max_prima= max(prima_jumatate) if prima_jumatate else None
    min_a_doua=min(a_doua_jumatate) if a_doua_jumatate else None

    return {"prima_jumatate":{
        "Valori":prima_jumatate,
        "Max":max_prima
    },"a_doua_jumatate":{
        "Valori":a_doua_jumatate,
        "Min":min_a_doua
    }
    }

text_introdus = input('Dati lista: ')
text_curat = text_introdus.replace(',',' ')
elemente_text= text_curat.split()
listamea=[int(x.strip()) for x in elemente_text]
print(slicing_minmax(listamea))



