#############IMPRESION############
print("Hola mundo")

###########BUCLE#################
if 0 < 1:
    print("hola bucle!")
    x = 2

##########VARIABLES################
palabra="Hola variable"
numero = 0
x,y,z="hola","pepe","que tal"
print(palabra)
print(numero)

############PARSEOS################
x=str(3)
y=int(5)
parseo=str("HOla")
print(x+" "+parseo)

##############ARRAY################
frutas=["naranja","pera","coco"]


###############FUNCIONES#################
ola="ola"
def mifuncion():
    global ola #con global podemos modificar el valor de la variable para que cambie fuera tambien
    ola = "nombre cambiado"
    print("dentro de funcion")

print("antes de llamarla") 
print(ola)   
mifuncion()
print(ola)
print("funcion llamada")

##############EJERCICIOS###############
#x="sdf"
#print(type(x)) #para ver tipo de dato
#[] list
#{} set
#() tuple
#{:} dict

print(float(x)) #cambiamos el tipo de dato

frase=" hola pepe"
print(len(frase)) #longitud de la frase
print(frase[0]) #leer el caracter que indiquemos
print(frase[1:5]) #leer del caracter 1 al 4
print(frase.strip()) #quitar espacios de blanco alante y atras
print(frase.upper()) #volverlo mayuscula, en minuscula lower
print(frase.replace("h","O")) #cambiar la h por la O


    
    



