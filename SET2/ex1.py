def generate_fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    fib_list = [0, 1]
    while len(fib_list) < n:
        fib_list.append(fib_list[-1] + fib_list[-2])
        
    return fib_list

n_numere = int(input("Dati marimea sirului"))

rezultat = generate_fibonacci(n_numere)
print(f"Primele {n_numere} numere sunt: {rezultat}")