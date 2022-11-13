class MroChecker:
    queue = {}

    def __init__(self):
        while s := input():
            if s.startswith('class'):
                name = s[6: s.find(':')]
                if '(' in name:
                    cur = name[:name.find('(')]
                    prev = [x.strip() for x in name[name.find('(') + 1: -1].split(',')]
                    try:
                        n_q = self.mklst([self.queue[x].copy() for x in prev] + [prev])
                    except KeyError:
                        print("No")
                        break
                    if n_q:
                        self.queue[cur] = [cur] + n_q
                    else:
                        print("No")
                        break
                else:
                    self.queue[name] = [name]
        else:
            print("Yes")

    @staticmethod
    def my_extend(lists):
        res = []
        for i in lists:
            res.extend(i)
        return res

    def mklst(self, deps):
        res = []
        fl = False
        while pars := self.my_extend(deps):
            fl = False
            for i in pars:
                if fl:
                    break
                for j in deps:
                    if i in j and i != j[0]:
                        break
                else:
                    res.append(i)
                    fl = True
                    for j in deps:
                        if i in j:
                            j.pop(0)
            else:
                if not fl:
                    return None
        return res

MroChecker()