


def foo(xyz=None,x=1,y=2):
    if xyz is None:
        xyz = []
    xyz.append(1)
    return xyz

a = foo(['1','2'])
print(a)