# Programa que suma los multiplos de tres o cinco hasta 1000

a=range(0,1001,3)
b=range(0,1001,5)
c=set(a)|set(b)

d=sum(c)

print d
