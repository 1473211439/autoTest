a=[1,2,3]
b=a[0:2]
print(b)
import  time;
d={
    1:'a',
    2:'b'
}
for key,v in dict.items(d):
    print(key,v)
    time.sleep(1)

print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
time.sleep(1)
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
