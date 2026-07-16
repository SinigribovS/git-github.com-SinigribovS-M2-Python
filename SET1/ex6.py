def camel_to_snake(text: str) -> str:

    if not text:
        return ""
        
    rezultat = []
    
    for i, char in enumerate(text):

        if char.isupper() and i > 0:
            
            rezultat.append('_')
        
        rezultat.append(char.lower())
        
    return "".join(rezultat)


test_text = "AcestaEsteUnExemplu"
print(f"Din '{test_text}' obținem: {camel_to_snake(test_text)}")
