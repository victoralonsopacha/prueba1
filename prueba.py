print("1.- Suma de vectores");
print("2.- promedio de valores numericos");
print("3.- Invertir el contenido de un archivo");
opcion=int(input("Ingrese la opcion que desea realizar"))
texto3="";
texto1="";
texto2="";

def leer():
    abrir=open('archivo.txt','r')
    return abrir.readlines()
    abrir.close();

palabra=str(leer())
print(palabra[2:18])
texto1=palabra[2:18]
print(palabra[24:32])
texto2=palabra[24:32]
texto3=palabra[38:42]
print(texto3)
    

def crearArchivo():
    nuevo=open("archivo1.txt",'w')
    nuevo.close();
    nuevo1=open("archivo2.txt",'w')
    nuevo1.close();
    nuevo2=open("archivo3.txt",'w')
    nuevo2.close();

def guardar(texto1,texto2,texto3):
    text1=open("archivo1.txt",'a')
    text1.write(texto1)
    text1.close()
    text2=open("archivo2.txt",'a')
    text2.write(texto1)
    text2.close()
    text3=open("archivo3.txt",'a')
    text3.write(texto1)
    text3.close()
      
if opcion==3:
    crearArchivo()
    guardar(texto1,texto2,texto3)
