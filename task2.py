class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self):
        return f'{self.a}{"-" if self.b < 0 else "+"}{abs(self.b)}'

    def __add__(self, other):
        if isinstance(other, Complex):
            return Complex(self.a + other.a, self.b + other.b)
        if isinstance(other, (int, float)):
            return Complex(self.a + self.b)
        raise NotImplementedError

    def __sub__(self, other):
        if isinstance(other, Complex):
            return Complex(self.a - other.a, self.b - other.b)
        if isinstance(other, (int, float)):
            return Complex(self.a - self.b)
        raise NotImplementedError

    def __mul__(self, other):
        if isinstance(other, Complex):
            return Complex(self.a * other.a, self.b * other.b)
        if isinstance(other, (int, float)):
            return Complex(self.a * self.b)
        raise NotImplementedError

    def __truediv__(self, other):
        if isinstance(other, Complex):
            return Complex(self.a / other.a, self.b / other.b)
        if isinstance(other, (int, float)):
            return Complex(self.a / self.b)
        raise NotImplementedError


c1 = Complex(10, 5)
c2 = Complex(10, -5)
print(c1, c2)
print(c1 + c2)
print(c1 - c2)
print(c1 * c2)
print(c1 / c2)





