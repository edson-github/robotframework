def one_argument(arg, /):
    return arg.upper()


def three_arguments(a, b, c, /):
    return '-'.join([a, b, c])


def with_normal(posonly, /, normal):
    return f'{posonly}-{normal}'


def defaults(required, optional='default', /):
    return f'{required}-{optional}'


def types(first: int, second: float, /):
    return first + second


def kwargs(x, /, **y):
    return f"{x}, {', '.join('%s: %s' % item for item in y.items())}"
