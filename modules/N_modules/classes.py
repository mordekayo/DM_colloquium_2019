class Natural (list):
    def __init__ (self, n = 0, **kwargs):
        self.n = n
        super().__init__(**kwargs)
    
    
    def append (self, x):
        self.n += 1
        super().append(x)
    
    def pop(self, i):
        if self.n > 0:
            self.n -= 1
        super().pop(i)
        