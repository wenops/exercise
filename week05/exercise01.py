
def sort(iterator,key=lambda x,y,reverse=True: x > y if reverse else x < y):
    ret = []
    for x in iterator:
        for i,y in enumerate(ret):
            #flag = x > y if reverse else x < y
            if key(x,y):
                ret.insert(i,x)
                break
        else:
            ret.append(x)
    return ret
# lst = [1,2,5,4,2,3,5,6]
# print(sort(lst,lambda x,y,reverse=False: x > y if reverse else x < y))

def add(x):
    def inc(y):
        return x+y
    return inc

print(add(1)(2))