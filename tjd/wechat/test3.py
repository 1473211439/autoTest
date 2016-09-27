h = 0
leap = 1
from math import sqrt
from sys import stdout
import datetime
for m in range(101,201):
    k = int(sqrt(m + 1))
    for i in range(2,k + 1):
        if m % i == 0:
            leap = 0
            break
    if leap == 1:
        print('%-4d' % m)
        h += 1
        if h % 10 == 0:
            print('')
    leap = 1
print('The total is %d' % h)

print(5**3)

print(datetime.date.today().strftime('%d/%m/%Y'))

my=datetime.date(1999,12,21)
print(my.strftime('%Y/%m/%d'))
n=my+datetime.timedelta(days=1)
print(n.strftime('%Y/%m/%d'))
n=n.replace(year=2017)
print(n.strftime('%Y/%m/%d'))
