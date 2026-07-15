def palindrome_selector(numere):
    rezultat = []
    
    for numar in numere:
        text_numar = str(numar)
        
        are_cifre_pare = len(text_numar) % 2 == 0
        
        este_palindrom = text_numar == text_numar[::-1]
        
        if are_cifre_pare and este_palindrom:
            rezultat.append(numar)
            
    return rezultat


lista_test= [121, 1221, 44, 5, 6776, 12321, 8888]
print(palindrome_selector(lista_test))
