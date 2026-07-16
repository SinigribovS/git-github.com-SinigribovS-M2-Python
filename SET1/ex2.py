def count_vowels(text: str) -> int:
    
    vowels = set("aeiouAEIOU")
    
    return sum(1 for char in text if char in vowels)


test1 = "Hello World!"
test2 = "We love python"
test3 = "XYZ"  

print(f"În '{test1}' avem: {count_vowels(test1)} vocale.")
print(f"În '{test2}' avem: {count_vowels(test2)} vocale.")
print(f"În '{test3}' avem: {count_vowels(test3)} vocale.") 