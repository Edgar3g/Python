xs = range(10)

ys = (x ** 2 for x in xs)

def prime_gererator():

    yield 2

    ps = []
    c = 1

    def up_to_square(y, xs):

        for x in xs:

            if y <= x ** 0.5:
                yield y
            
            else:
                return
    
    while True:

        c += 2

        if not any((c % p == 0 for p in up_to_square(c, ps))):
            ps.append(c)
            yield c

import itertools

primes = list(itertools.islice(prime_generator,100000))