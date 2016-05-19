
def promedio():
    suma=1
    contador=0
    result=0
    while suma != 0:
        suma=int(input('ingrese un numero a sumar:'))
        result=result+suma
        contador=contador+1
        promedio=result/contador
        print ('el promedio es:')
        print(promedio)
    
promedio()
    

    
