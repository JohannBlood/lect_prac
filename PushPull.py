class Pushpull:
    pos = 0

    def __init__(self, p=0):
        Pushpull.pos = p

    @staticmethod
    def push(n=1):
        Pushpull.pos += n

    @staticmethod
    def pull(n=1):
        Pushpull.pos -= n

    def __str__(self):
        if self.pos > 0:
            return f">{self.pos}>"
        elif self.pos < 0:
            return f"<{-self.pos}<"
        return f"<{self.pos}>"

    def __iter__(self):
        if self.pos > 0:
            return iter(list(range(0, self.pos)))
        else:
            return iter([-i for i in range(0, -self.pos)])