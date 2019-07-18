def copy_properties(src):
    def _copy(dst):
        dst.__name__ = src.__name__
        dst.__doc__ = src.__doc__
        dst.__qualname__ =  src.__qualname__
        return dst
    return _copy

def logger(fn):
    @copy_properties(fn)#@_copy-->wrapper-->_copy(wrapper)-->return wrapper
    def wrapper(*args,**kwargs):
        '''This is a function'''
        print("before")
        ret  = fn(*args,**kwargs)
        print("after")
        return ret
    copy_properties(fn,wrapper)
    return wrapper

@logger #add=logger(add)
def add(x,y):
    '''
    function
    :param x: int
    :param y: int
    :return: int
    '''
    return x+y

print(add(4,5),add.__doc__)