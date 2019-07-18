import datetime
import  time



def count_time(t):
    def logger(fn):
        def _logger(*args,**kwargs):

            start = datetime.datetime.now()
            ret = fn(*args,**kwargs)
            duration = (datetime.datetime.now() - start).total_seconds()
            if duration >t:
                print(fn.__name__,duration)
            return ret
        return _logger
    return logger




@count_time(6)#logger(6)(add1)-->
def add1(x,y):
    time.sleep(3)
    return x+y



print(add1(9,5))