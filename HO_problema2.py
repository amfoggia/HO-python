# Dado un set de datos, obtener un grafico tipo scatter de X en funcion de Y
# Se hace un ajuste lineal

# Importamos librerias
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as pp

# Datos a graficar y ajustar
datos_x=[]
datos_y=[]
fileId=open("tabla.dat")
for line in fileId:
	l = line.split(",")
	datos_x.append(float(l[0]))
	datos_y.append(float(l[1]))
#print datos_x,datos_y
fileId.close


# Definimos la funcion con la cual ajustar y hacemos el ajuste
def fitLineal(y,a,b):
	return a*y+b
def otra(y):
        return 0.86599663*y+17.79571199

#ruido=np.random.normal(-1,1)*np.amax(datos_y)*1e-3
fitParams, fitCovariances=curve_fit(fitLineal,datos_x,datos_y)
sigma=[fitCovariances[0,0],fitCovariances[1,1]]

print 'Los parametros del ajuste son',fitParams
print 'La matriz de covarianza es:', fitCovariances


# Graficamos los datos
pp.xlabel("datos_x")
pp.ylabel("datos_y")
#pp.scatter(datos_x,datos_y)
#pp.plot(datos_x,fitLineal(datos_x,0.86599663,17.79571199))
pp.plot(datos_x,otra(datos_x))
pp.show()