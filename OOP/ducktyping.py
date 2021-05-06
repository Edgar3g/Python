class Inicial:

    def __init__(self, v):
        self.value = v
    
    def __add__(self, other = 5):
        soma = self.value + other.value
        return soma

class Contador:

    def __init__(self):
        self.final = 10
    
    def __iter__(self):

        class iterador:

            def __init__(self, o):
                self.o = o
                self.atual = 0;
            
            def __next__(self):

                if self.atual < self.o.final:
                    self.atual += 1;

                    return self.atual - 1
                else:
                   # raise StopAsyncIteration()
                   pass
        
        return iterador(self)

print([x for x in Contador()])