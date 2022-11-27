import sys
import tarfile
from io import BytesIO

s = bytes.fromhex(''.join(sys.stdin.read().replace(' ', '').split('\n')))
bts = BytesIO(s)
file = tarfile.open(fileobj=bts)
res = []
for i in file.getmembers():
    if i.isfile():
        res.append(i)
print(sum(map(lambda x: x.size, res)), len(res))