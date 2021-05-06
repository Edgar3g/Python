def multiplicar(a, b, *outros):

    r = a *b

    for cada in outros:
        r *= cada
    
    return r

print(multiplicar(1,2,3,4))