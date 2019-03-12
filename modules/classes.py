class Natural (list):
    def __init__ (self, n = 0, *args):
        self.n = n
        super().__init__(args)
        

class Integer(Natural):
    def __init__(self, b = 0, n = 0, *args):
        self.b = b
        super().__init__(n, args)


class Rational:
    def __init__(self, m=Integer(), n=Natural(0, 0)):
        self.m = m
        self.n = n
        

class Polinomial (list):
    def __init__(self, m=0, *args):
        self.m = m
        super().__init__(*args)
