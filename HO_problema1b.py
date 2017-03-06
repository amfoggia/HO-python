# Este programa suma los numeros impares de la serie de Fibonacci menores a un millon
suma=0
iter_1=1
iter_2=2
a=[1,2]
while suma<=1e6-iter_1:
	suma=iter_1+iter_2
	iter_1=iter_2
	iter_2=suma

	a.append(suma)
	
	
total=0
b=[]
for i in a:
	elem_guard=i%2
	if elem_guard!=0:
		b.append(i)
for i in b:
	total=total+i
	
print total

