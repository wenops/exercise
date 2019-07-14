


def logger(fn):
    def _logger(*args,**kwargs):
        print("before")
        ret = fn(*args,**kwargs)
        print("after")
        return ret
    return _logger

@logger#add1 = logger(add1)
def add1(x,y):
    return x+y

# add1 = logger(add1)
print(add1(2,3))