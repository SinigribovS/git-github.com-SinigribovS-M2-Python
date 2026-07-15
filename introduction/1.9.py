def prim(numar):
    if numar <= 1:
        return False

    for i in range(2, int(numar ** 0.5) + 1):
        if numar % i == 0:
            return False

    return True

print(prim(11))
print(prim(4))
print(prim(21))