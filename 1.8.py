def palindrom(numar):
    text_numar = str(numar)

    text_inversat = text_numar[::-1]

    if text_numar == text_inversat:
        return True
    else:
        return False

print(palindrom(121))
print(palindrom(1234))
print(palindrom(1331))