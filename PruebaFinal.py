print("1.- Suma de vectores");
print("2.- promedio de valores numericos");
print("3.- Invertir el contenido de un archivo");
opcion=int(input("Ingrese la opcion que desea realizar:\n"))
texto3="";
texto1="";
texto2="";

def leer():
    abrir=open('archivo.txt','r')
    return abrir.read(7168)
    abrir.close();
    

def crearArchivo():
    nuevo=open("archivo1.txt",'w')
    nuevo.close();
    nuevo1=open("archivo2.txt",'w')
    nuevo1.close();
    nuevo2=open("archivo3.txt",'w')
    nuevo2.close();
    nuevoReves1=open("archivo1invertido.txt",'w')
    nuevoReves1.close();
    nuevoReves2=open("archivo2invertido.txt",'w')
    nuevoReves2.close();
    nuevoReves3=open("archivo3invertido.txt",'w')
    nuevoReves3.close();



def guardar(texto1,texto2,texto3):
    print("DIVICION EN TRES:")
    palabra=str(leer())
    print(palabra[0:17])
    texto1=palabra[0:17]
    print(palabra[17:32])
    texto2=palabra[17:32]
    texto3=palabra[38:42]
    print(texto3)
    print("\n")
    text1=open("archivo1.txt",'a')
    text1.write(texto1)
    text1.close()
    text2=open("archivo2.txt",'a')
    text2.write(texto2)
    text2.close()
    text3=open("archivo3.txt",'a')
    text3.write(texto3)
    text3.close()

def  invertir(texto):
    return texto[::-1]

def guardarReves(text1,text2,text3):
    reves1=open("archivo1invertido.txt",'a')
    reves1.write(text1)
    reves1.close()
    reves2=open("archivo2invertido.txt",'a')
    reves2.write(text2)
    reves2.close()
    reves3=open("archivo3invertido.txt",'a')
    reves3.write(text3)
    reves3.close()

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
        
    

#   FUNCION QUE CALCULA DOS VECTORES CON VALORES INGRESADOS POR TECLADO
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
    print("DIVICION EN TRES:")
    palabra=str(leer())
    print(palabra[0:17])
    texto1=palabra[0:17]
    print(palabra[17:32])
    texto2=palabra[17:32]
    texto3=palabra[38:42]
    print(texto3)
    print("\n")
    text1=str(invertir(texto1))
    text2=str(invertir(texto2))
    text3=str(invertir(texto3))
    print("AL REVES:")
    print(text1)
    print(text2)
    print(text3)
    guardarReves(text1,text2,text3)
    print("\nrevisa los archivos.txt")

