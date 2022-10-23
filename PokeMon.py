players = dict()
cards = dict()
while a := input():
    a = a.split(' / ')
    if a[0].isnumeric():
        cards[int(a[0])] = cards.get(int(a[0]), set()) | {a[1]}
    else:
        players[a[0]] = players.get(a[0], set()) | {int(a[1])}
for i, j in players.items():
    s = set()
    for m in j:
        s |= cards[m]
    players[i] = len(s)
res = []
for i, j in sorted(players.items(), key=lambda x: x[1], reverse=True):
    if j == max(players.values()):
        res.append(i)
    else:
        break
print(*sorted(res), sep='\n')
