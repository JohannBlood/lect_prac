a = input()
b = input()
if b in a:
    print('YES')
else:
    if b[0] in a:
        for i in range(1, len(a)):
            if b in a[a.index(b[0])::i]:
                print('YES')
                break
        else:
            print('NO')
    else:
        print("NO")