mas_x, mas_y, mas_z = [], [], []
while a := input():
    x, y, z = eval(a)
    mas_x.append(x)
    mas_y.append(y)
    mas_z.append(z)
print((max(mas_y) - min(mas_y)) * (max(mas_x) - min(mas_x)) * (max(mas_z) - min(mas_z)))