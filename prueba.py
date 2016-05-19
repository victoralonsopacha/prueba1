print("1.- Suma de vectores");
print("2.- promedio de valores numericos");
print("3.- Invertir el contenido de un archivo");
opcion=int(input("Ingrese la opcion que desea realizar:\n"))
texto3="";
texto1="";
texto2="";

def leer():
    abrir=open('archivo.txt','r')
    return abrir.readlines()
    abrir.close();
print("DIVICION EN TRES:")
palabra=str(leer())
print(palabra[2:18])
texto1=palabra[2:18]
print(palabra[24:32])
texto2=palabra[24:32]
texto3=palabra[38:42]
print(texto3)
print("\n")
    

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
    
      
if opcion==3:
    
    crearArchivo()
    guardar(texto1,texto2,texto3)
    text1=str(invertir(texto1))
    text2=str(invertir(texto2))
    text3=str(invertir(texto3))
    print("AL REVES:")
    print(text1)
    print(text2)
    print(text3)
    guardarReves(text1,text2,text3)
    print("\nrevisa los archivos.txt")

