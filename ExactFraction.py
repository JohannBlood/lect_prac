from fractions import Fraction


x = input().split(', ')
s = Fraction(x[0])
w = Fraction(x[1])
a = list(map(Fraction, x[3:4 + x[2]]))
b = list(map(Fraction, x[5 + x[2]:]))
f_a = lambda x: sum(a[i] * x ** i for i in range(len(a)))
f_b = lambda x: sum(b[i] * x ** i for i in range(len(b)))
print(f_a(w) / f_b(w) == s)