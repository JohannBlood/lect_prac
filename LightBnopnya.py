import itertools
import sys
# from time import time


# def find_all(depth, key0, val0):    # функция ищет все возможные последовательности перекодировок
#     if depth > 3:
#         return
#     global codes
#     for i, j in itertools.permutations(cd, 2):
#         if key0 and key0[-1][-1] == i:
#             continue
#         # if not key0 and i == 'koi8_r':
#         #     continue
#         try:
#             val = val0.decode(i).encode(j)
#             key = key0 + ((i, j),)
#             if key not in codes:
#                 codes.append(key)
#             find_all(depth + 1, key, val)
#         except UnicodeDecodeError:
#             continue
#         except UnicodeEncodeError as E:
#             continue



# def correct(seq):
#     buf = headtail
#     try:
#         buf = buf.encode(seq[-1][-1])
#         # print(buf)
#     except UnicodeEncodeError:
#         # if seq[0][0] == 'cp855':
#         #     print('wtf')
#         return False
#     for j, i in seq[::-1]:
#         buf = buf.decode(i, errors="ignore").encode(j, errors="ignore")
#         # print(buf)
#     buf = buf.decode("koi8-r", errors="ignore")
#     # print(buf)
#     if buf == "ПРОЦКНЦ;":
#         for k in range(len(b)):
#             b[k] = b[k].encode(seq[-1][-1])
#             for j, i in seq[::-1]:
#                 b[k] = b[k].decode(i, errors="ignore").encode(j, errors="ignore")
#             b[k] = b[k].decode("koi8-r", errors="ignore")
#         print('\n'.join(b))
#         return True
#     return False


alphabet = "!\"(),:;%АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЫЬЭЮЯ".encode("koi8-r")
cd = [
    'cp037', 'cp1006', 'cp1250', 'cp1251', 'cp1253', 'cp1254', 'cp1255', 'cp1256',
    'cp1257', 'cp1258', 'cp437', 'cp720', 'cp737', 'cp775', 'cp850', 'cp852', 'cp855',
    'cp864', 'cp866', 'cp869', 'cp874', 'cp875', 'hp_roman8', 'iso8859_10', 'iso8859_16',
    'iso8859_4', 'iso8859_5', 'koi8_r', 'latin_1', 'mac_croatian', 'mac_greek', 'mac_iceland', 'mac_latin2'
]
b = sys.stdin.read().rstrip()
# t0 = time()
headtail = b[:4] + b[-4:]
if 'KM' in headtail or '×{´F' in headtail:
    b = b.split('%')
else:
    b = b.split('\n')
# print(b, 'saas')
# b = bytes.fromhex(b).decode().split('%')
# print(b)
# b = list(map(lambda x: x.decode('utf-8'), b))
# print(b)
if headtail == 'ПРОЦКНЦ;':
    print('\n'.join(b))
    sys.exit()

#   Кодировки длины 1
codes = dict()  # Список всех возможных последовательностей перекодировок длины 1
for i, j in itertools.permutations(cd, 2):
    # if key0 and key0[-1][-1] == i:
    #     continue
    # if not key0 and i == 'koi8_r':
    #     continue
    try:
        val = alphabet.decode(i).encode(j)
        key = ((j, i),)
        codes[key] = val
        if headtail.encode(i).decode('koi8-r') == 'ПРОЦКНЦ;':
            for seq in b:
                print(seq.encode(i).decode('koi8-r'))
            sys.exit()
    except UnicodeDecodeError:
        continue
    except UnicodeEncodeError as E:
        continue
# for seq in codes:
#     if correct(seq):
#         sys.exit()
#   Кодировки длины 2
codes1 = dict()
for el, value in codes.items():
    for i, j in itertools.permutations(cd, 2):
        if el[0][0] == i:
            continue
        # if key0 and key0[-1][-1] == i:
        #     continue
        # if not key0 and i == 'koi8_r':
        #     continue
        try:
            val = value.decode(i).encode(j)
            key = ((j, i),) + el
            codes1[key] = val
            if headtail.encode(i).decode(el[0][0]).encode(el[0][1]).decode('koi8-r') == 'ПРОЦКНЦ;':
                for seq in b:
                    print(seq.encode(i).decode(el[0][0]).encode(el[0][1]).decode('koi8-r'))
                sys.exit()
        except UnicodeDecodeError:
            continue
        except UnicodeEncodeError:
            continue
# for seq in codes1:
#     if correct(seq):
#         sys.exit()
#   Кодировки длины 3
for el, value in codes1.items():
    for i, j in itertools.permutations(cd, 2):
        if el[0][0] == i:
            continue
        # if key0 and key0[-1][-1] == i:
        #     continue
        # if not key0 and i == 'koi8_r':
        #     continue
        try:
            val = value.decode(i).encode(j)
            key = el + ((i, j),)
            ((v1, v2), (v3, v4)) = el
            if headtail.encode(i).decode(v1).encode(v2).decode(v3).encode(v4).decode('koi8-r') == 'ПРОЦКНЦ;':
                for num in range(len(b)):
                    b[num] = b[num].encode(i).decode(v1).encode(v2).decode(v3).encode(v4).decode('koi8-r')
                print('\n'.join(b))
                # print(time() - t0)
                sys.exit()
        except UnicodeDecodeError:
            continue
        except UnicodeEncodeError:
            continue
# for seq in codes:
#     if correct(seq):
#         sys.exit()

