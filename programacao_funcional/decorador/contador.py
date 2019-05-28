def fabrica_de_contador():
    _contador = 0

    def contar():
        nonlocal _contador
        _contador +=1
        return _contador

    return contar

contador = fabrica_de_contador()
contador_2 = fabrica_de_contador()
print(contador())
print(contador())
print(contador())
print(contador_2())
print(contador_2())
print('')
print('')
print('Fabrica com variável global')

_contador = 0

def fabrica_de_contador2():
    def contar():
        global _contador
        _contador +=1
        return _contador

    return contar

contador = fabrica_de_contador2()
contador_2 = fabrica_de_contador2()
print(contador())
print(contador())
print(contador())
print(contador_2())
print(contador_2())