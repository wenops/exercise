


pre = 0
cur = 1

print(pre,cur)

def fib(n,pre=0,cur=1):
    pre,cur= cur ,pre + cur
    print(cur,end=' ')
    if n == 2:
        return
    fib(n-1,pre,cur)

# fib(5)

# def fib2(n):
#     res += n
#     print(res)
#     if n == 2:
#         return
#     fib2(n-1)
#
# fib2(5)
#n的阶乘
def func(num):
    if num ==1:
        return 1
    else:
        return num * func(num -1)
# a = func(6)
# print(a)
#1234 4321
lst = str(1234)
def reversal(x):
    if x == -1:
        return ''
    else:
        return lst[x] + reversal(x-1)


# lst = str(1234)
# print(reversal(len(lst)-1))

#猴子吃桃
def peach(day=9,sum=1):
    sum = 2 * (sum + 1)
    day -= 1
    if day ==0 :
        return sum
    return peach(day,sum)

#print(peach())

sum = 1
for i in range(1,10):
    sum = 2*(sum+1)

print(sum)