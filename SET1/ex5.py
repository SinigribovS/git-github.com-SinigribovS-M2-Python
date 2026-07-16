def has_special_characters(text: str) -> bool:
    
    special_chars = {'\r', '\t', '\n', '\a', '\b', '\f', '\v'}
    
    return any(char in special_chars for char in text)

test_curat = "Bună! Ce mai faci?"
test_cu_tab = "Salut!\tCe mai faci?" 
test_cu_linie_noua = "Linie noua\npe bune!" 

print(f"'{test_curat}' are caracterele speciale -> {has_special_characters(test_curat)}") 

print(f"'{test_cu_tab}' are caracterele speciale -> {has_special_characters(test_cu_tab)}") 

print(f"'{test_cu_linie_noua}' are caracterele speciale -> {has_special_characters(test_cu_linie_noua)}") 