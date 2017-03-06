# Este programa calcula el factor primo mas grande de algun numero 

numero1= 600851475143  # Numero al que queremos calcularle el factor primo
raiz=numero1**(0.5)  # Solo calculamos los factores hasta este numero (teorema)
numero=int(raiz)+1  # Le sumamos uno para tener el entero mayor

a=range(1,numero+1,1)  # Vamos a dividir la raiz por todos estos numeros a ver cuales son divisores
b=[]
c=[]
d=[]
f=[]
g=[]

for i in a:
	multiplos_2=i%2  
	multiplos_3=i%3
	multiplos_5=i%5
	
	if multiplos_2!=0 and multiplos_3!=0 and multiplos_5!=0:
		b.append(i)  # Descartamos los divisores 2,3,5 y todos sus multiplos

for i in b:
	multiplo=numero1%i
	if multiplo==0:  
		c.append(i)  #Vemos cual de los anteriores son divisores de nustro numero
print c

# Ahora tenemos que ver cual de esos es el mayor primo--> repetimos el codigo anterior
# Estos valores seguro que no son multiplos de 2,3,5
for i in c:
    raiz_2=int(i**(0.5))+1  # Un vector con los numeros a los cuales buscarles los divisores
    l=raiz_2
    d.append(raiz_2)
    for i in d:
        e=range(1,i+1,1)  # Posibles divisores del divisor de nuestro numero
        print raiz_2
        for i in e:
            nuevo_multiplo=raiz_2%i
            if nuevo_multiplo==0:
                f.append(raiz_2/i)
                if len(f)<=2:
                    g.append((raiz_2-1)**2)
print g
	

