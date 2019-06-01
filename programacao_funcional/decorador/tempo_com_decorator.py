from functools import wraps
from time import sleep, strftime

from decorator import decorator, getfullargspec

@decorator
def logar(f, fmt='%H:%M:%S', *args, **kwargs):
    print(strftime(fmt))
    return f(*args, **kwargs)

@logar
def mochileiro():
    return 42

@logar(fmt='%d-%m-%Y %H:%M:%S')
def ola(nome):
    return f'Olá {nome}'


if __name__ == '__main__':
    print(getfullargspec(ola))
    print(getfullargspec(mochileiro))
    print(mochileiro())
    print(mochileiro.__name__)
    print(ola('André'))
    print(ola.__name__)
    sleep(1)
    print(mochileiro())
    print(ola('Liciano'))
