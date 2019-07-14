#
#
#
# def counter():
#     i = 0
#     while True:
#         i += 1
#         yield i
# def inc(c):
#     return next(c)
#
#
# c = counter()
# print(inc(c))
# print(inc(c))
#

def inc():
    def counter():
        i = 0
        while True:
            i += 1
            yield i
    c = counter()
    return lambda : next(c)
foo = inc()
print(foo())
print(foo())