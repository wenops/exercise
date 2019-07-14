#coding=utf-8



#20个被7整除的整数
# count = 0
# for i in range(0,1000,7):
#     print(i)
#     count+=1
#     if count >=20:
#         break
#
# lst = [(i+1)**2 for i in range(10)]
# print(lst)
#
# lst2= [(x,y) for x in 'abcde' for y in range(3)]
# print(lst2)



# def counter():
#     c = [0]
#     def inc():
#         c[0] += 1
#         return c[0]
#     return inc
#
#
# foo =  counter()#函数的对象 对象的引用
# #inc()#不可见  调用摆错
# print(foo(),foo())
# c = 100
# print(foo())

def counter():
    c = 10
    def inc():
        z  = c+10
        #c +=10 赋值即定义 定义变量时候将使用局部变量不会使用外部变量 使用内部变量的时候还未赋值就会报错
        return z
    return inc


foo =  counter()#函数的对象 对象的引用
#inc()#不可见  调用摆错
print(foo(),foo())
c = 100
print(foo())

