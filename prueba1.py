#	PROGRAMA INGRESOS DE NUMERo

def ingresoNumeros():
	num =1
	cont=0
	resp =0
	while num>0:
		num=int(input("Ingrese un numero: "))
		resp= resp + num
		cont=cont+1
	print("El promedio es: " + str(resp/cont))


ingresoNumeros()