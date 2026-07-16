def count_occurrences(sub_string: str, main_string: str) -> int:

    if not sub_string or not main_string:
        return 0
        
    count = 0
    start = 0
    
    while True:
        pos = main_string.find(sub_string, start)
        
        if pos != -1:
            count += 1
            start = pos + 1
        else:
            break
            
    return count

print(f"In string sunt {count_occurrences("ana", "anana")} suprapuneri")