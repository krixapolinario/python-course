def raiz(i):
    raiz = i ** 0.5
    if len(str(raiz)) > 3 and str(raiz)[2] != 0:
        return None
    return int(raiz)
num=int(input('Informe o numero:'))
print(raiz(num))
