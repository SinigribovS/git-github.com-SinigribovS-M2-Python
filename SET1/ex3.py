import re 

def word_counter(text:str) -> int:

    if not text:
        return 0
    words = re.findall(r'\w+', text)

    return len(words)

test1 = "salut!!!,,,     ce... mai,,,faci???"
test2 = "Rezolvam 100 de probleme in Python!"

print(f"Test1: -> {word_counter(test1)} cuvinte") 

print(f"Test cu numere: -> {word_counter(test2)} cuvinte") 