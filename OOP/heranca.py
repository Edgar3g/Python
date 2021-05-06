class A:

    def __init__(self):
        self.msg = "Olá Edgar !, tudo Bem ?"
    
class B(A):
    def ola(self):
        print(self.msg)

class C(B):
    def __init___(self):
        A.__init__(self)

c = C()
c.ola()