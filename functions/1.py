def sum(*cs):
    s = 0;

    for c in cs:
        s += c
    return s

def apply(function,  arguments):
    return function(*arguments)

def apply_one(function):
    return lambda *cs: function(1, *cs)

r = apply(apply_one(sum), [2,3,4,5])
print(r)