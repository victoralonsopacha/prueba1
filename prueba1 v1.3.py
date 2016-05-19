#	PROGRAMA INGRESOS DE NUMERo

def ingresoNumeros():
	num =1
	cont=0
	resp =0
	while num>0:
		num=int(input("Ingrese un numero: "))
		if num!=0:
			resp= resp + num
			cont=cont+1
	
	print("El promedio es: " + str(resp/cont))
		
	

#	FUNCION QUE CALCULA DOS VECTORES CON VALORES INGRESADOS POR TECLADO
def sumaVector():
	vector1 =[0, 0 ,0]

	for i in range(1,3):
		vector1[0]= vector1[0] + int(input("Ingrese el valor de X" + str(i)+ ": "))
		vector1[1]= vector1[1] + int(input("Ingrese el valor de Y" + str(i)+ ": "))
		vector1[2]= vector1[2] + int(input("Ingrese el valor de Z" + str(i)+ ": "))

	print("El valor de X1 + X2= " + str(vector1[0]))
	print("El valor de Y1 + Y2= " + str(vector1[1]))
	print("El valor de Z1 + Z2= " + str(vector1[2]))


ingresoNumeros()
sumaVector()