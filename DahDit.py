class morse:

    def __init__(self, s=''):
        if not s or ' ' in s:
            self.sep = ','
            self.end = '.'
            s = s.split(" ")
        else:
            self.sep = ' '
            self.end = ''

        n = len(s)
        if n == 2:
            self.dot = s[0]
            self.end_dot = s[0]
            self.dash = s[1]
        elif n == 3:
            self.dot, self.end_dot, self.dash = s
        elif n == 4:
            self.dot, self.end_dot, self.dash, self.end = s
        else:
            self.dot = 'di'
            self.end_dot = 'dit'
            self.dash = 'dah'

        self.prev = None
        self.buff = self.end

    def __neg__(self):
        if self.sep != ' ':
            self.buff = ' ' + self.dash + self.buff
        else:
            self.buff = self.dash + self.buff

        self.prev = '-'

        return self

    def __pos__(self):
        tmp = self.dot
        if self.prev == "~" or not self.prev:
            tmp = self.end_dot

        if self.sep != ' ':
            tmp = ' ' + tmp
        self.buff  = tmp + self.buff

        self.prev = '+'

        return self

    def __invert__(self):
        self.buff = self.sep + self.buff

        self.prev = '~'

        return self

    def __str__(self):
        return self.buff.strip()