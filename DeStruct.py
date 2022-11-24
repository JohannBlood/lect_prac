import base64, sys


a = sys.stdin.buffer.read().strip()
# print(a)
a = base64.b85decode(a)
# print(a)
head = []
pos = 0
while el := int.from_bytes(a[pos:pos + 1], byteorder='big', signed=True):
    head.append(el)
    pos += 1
pos += 1
res = []
# print(f'sum={(len(a) - pos) // sum(map(abs, head))}')
for j in range((len(a) - pos) // sum(map(abs, head))):
    for i in head:
        # print('i =', i, 'pos=', pos)
        # print(a[pos: pos + abs(i)])
        if i > 0:
            # print(int.from_bytes(a[pos: pos + abs(i)], byteorder='big', signed=False))
            res.append(int.from_bytes(a[pos: pos + abs(i)], byteorder='big', signed=False))
        else:
            # print(int.from_bytes(a[pos: pos + abs(i)], byteorder='big', signed=True))
            res.append(int.from_bytes(a[pos: pos + abs(i)], byteorder='big', signed=True))
        pos += abs(i)

print(sum(res))
