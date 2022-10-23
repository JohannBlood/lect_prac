from collections import defaultdict
import sys


words1 = defaultdict(int)
words2 = defaultdict(int)

p, b, g, e = input()
punc = ('.', '!', '?')
text = sys.stdin.read().split()
prev = 0

for word in text:
    if word[0] == b and prev == p:
        words1[word] += 1

    if word[0] == g and word[-1] == e:
        words2[word] += 1
        prev = e
    elif word[-1] in punc:
        prev = word[-1]
t1 = max(words1.values()) if words1 else -1
t2 = max(words2.values()) if words2 else -1

a1, a2 = 0, 0

for k, v in words1.items():
    if v == t1:
        a1 = k
        break


for k, v in words2.items():
    if v == t2:
        a2 = k
        break

ans = f"{a1 if a1 != 0 else '...'} {words1[a1] if a1 != 0 else 0} - {a2 if a2 != 0 else '...'} {words2[a2] if a2 != 0 else 0}"
print(ans)
