a = []
b = 0
d = 0
while c := int(input()):
    if b == 0 or c >= d:
        b += 1
        d = c
    else:
        a.append(b)
        b = 1
        d = c
else:
    a.append(b)
print(max(a))