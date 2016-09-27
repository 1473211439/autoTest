import math;
# 题目：有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if(i!=k and i!=j and j!=k):
                # print("the number is %d%d%d" % (i,j,k))
                print(i,j,k);


for i in range(10000):
    #转化为整型值
    x = int(math.sqrt(i + 100))
    y = int(math.sqrt(i + 268))
    if(x * x == i + 100) and (y * y == i + 268):
        print("the num is :",i)


l = []
for i in range(3):
    x = int(input('integer:\n'))
    l.append(x)
l.sort()
# print("__:",l)


def fib(n):
    a,b=1,1
    for i in range(n-1):
        a,b=b,a+b
    return a
print('fib',fib(10))







i = int(input('净利润:'))
arr = [1000000,600000,400000,200000,100000,0]
rat = [0.01,0.015,0.03,0.05,0.075,0.1]
r = 0
for idx in range(0,6):
    if i>arr[idx]:
        r+=(i-arr[idx])*rat[idx]
        print((i-arr[idx])*rat[idx])
        i=arr[idx]
print(r)