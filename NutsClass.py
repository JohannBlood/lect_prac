class Nuts:

    def __init__(self, *args):
        pass

    def __str__(self):
        return self.__class__.__name__

    def __iter__(self):
        return iter(self.__class__.__name__)

    def __getattr__(self, item):
        return item

    def __getitem__(self, item):
        return item

    def __setattr__(self, key, value):
        self.__dict__[key] = key

    def __setitem__(self, key, value):
        return self

    def __delitem__(self, key):
        pass

    def __delattr__(self, item):
        pass