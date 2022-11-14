class Calculator:
    buff = dict()

    def __init__(self, mas):
        self.calc(mas)

    def calc(self, code):
        for s in code:
            #print(s)
            try:
                if "=" in s:
                    if s.count("=") > 1:
                        raise SyntaxError
                    name, expr = s.split('=')
                    #print(name, expr)
                    if name.isidentifier():
                        res = self.calcul(expr)
                        self.buff["_" + name] = res
                        #print(self.buff, 'assisgn')
                    else:
                        raise AttributeError
                else:
                    print(self.calcul(s))
            except AttributeError:
                print("Assignment error")
            except SyntaxError:
                print('Syntax error')
            except TypeError:
                print('Syntax error')
            except NameError:
                print('Name error')
            except Exception:
                print('Runtime error')

    def calcul(self, expr):
        op = "+-*/%()"
        if "**" in expr or "//" in expr or "." in expr:
            raise SyntaxError
        st = 0
        new_expr = ''
        for i, ch in enumerate(expr):
            if ch in op:
                if name := expr[st:i]:
                    #print(name)
                    if name.isidentifier():
                        #print('wtf')
                        name = "_" + name
                        if ch == "(":
                            raise SyntaxError
                        if name not in self.buff:
                            #print(name, 'wtf')
                            #print(self.buff)
                            raise NameError
                    elif not name.isdigit():
                        raise SyntaxError
                    new_expr += name
                    #print(new_expr)
                new_expr += ch
                st = i + 1
        #print(new_expr)
        if name := expr[st:]:
            if name.isidentifier():
                name = "_" + name
            new_expr += name
        #print(new_expr)
        res = eval(new_expr.replace('/', '//'), self.buff)
        return res


code = []
while s := input():
    if s.startswith('#') or not s:
        continue
    code.append(s.replace(' ', ''))
Calculator(code)
