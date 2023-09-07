fp=open('D:/A.1','a+')
print('hello',file=fp)
fp.close()
#转义字符
import keyword
print(keyword.kwlist)
fp='妈妈'
print(fp)
print(id(fp))
print(11%2)
a,b,c=20,2,3
print(a,b,c)
a,b=10,30
print(a>b)
print(4<<2)