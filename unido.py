print("1.- Suma de vectores");
print("2.- promedio de valores numericos");
print("3.- Invertir el contenido de un archivo");

opcion=int(input("Ingrese la opcion que desea realizar"))

    

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




texto3="";
texto1="";
texto2="";

def leer():
    abrir=open('archivo.txt','r')
    return abrir.readlines()
    abrir.close();
    

def crearArchivo():
    nuevo=open("archivo1.txt",'w')
    nuevo.close();
    nuevo1=open("archivo2.txt",'w')
    nuevo1.close();
    nuevo2=open("archivo3.txt",'w')
    nuevo2.close();

def guardar(texto1,texto2,texto3):
    palabra=str(leer())
    print(palabra[2:18])
    texto1=palabra[2:18]
    print(palabra[24:32])
    texto2=palabra[24:32]
    texto3=palabra[38:42]
    print(texto3)
    text1=open("archivo1.txt",'a')
    text1.write(texto1)
    text1.close()
    text2=open("archivo2.txt",'a')
    text2.write(texto1)
    text2.close()
    text3=open("archivo3.txt",'a')
    text3.write(texto1)
    text3.close()

def sumaVector():
    vector1 =[0, 0 ,0]

    for i in range(1,3):
        vector1[0]= vector1[0] + int(input("Ingrese el valor de X" + str(i)+ ": "))
        vector1[1]= vector1[1] + int(input("Ingrese el valor de Y" + str(i)+ ": "))
        vector1[2]= vector1[2] + int(input("Ingrese el valor de Z" + str(i)+ ": "))

    print("El valor de X1 + X2= " + str(vector1[0]))
    print("El valor de Y1 + Y2= " + str(vector1[1]))
    print("El valor de Z1 + Z2= " + str(vector1[2]))



if opcion==1:
    sumaVector()
elif opcion==2:
    ingresoNumeros()
elif opcion==3:
    crearArchivo()
    guardar(texto1,texto2,texto3)