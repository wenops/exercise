
import datetime
import  time
def time_count(fn):
    def _time_count(*args,**kwargs):
        print("the args{},{}".format(args,kwargs))
        start = datetime.datetime.now()
        ret = fn(*args,**kwargs)
        end =  datetime.datetime.now() - start
        print(fn.__name__,end)
        return ret
    return _time_count

@time_count
def add1(x,y):
    'This is a function'
    time.sleep(5)
    return x+y

print(add1(4,5))