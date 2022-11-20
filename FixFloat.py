import sys


def fix(n):
    def decorator(f):
        def res(*args, **kwargs):
            args = map(lambda x: round(x, n) if isinstance(x, float) else x, args)
            for key, value in kwargs.items():
                if isinstance(value, float):
                    kwargs[key] = round(value, n)
            ans = f(*args, **kwargs)
            return round(ans, n) if isinstance(ans, float) else ans
        return res
    return decorator


exec(sys.stdin.read())
