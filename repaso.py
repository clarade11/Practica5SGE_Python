#cuantas vocales hay en una frase
frase="Habia una niña"
vocales=0
if "a" or "e" or "i" or "o" or "u" in frase:
    print("Hay vocales")
    tupla=tuple(map(str, frase))
    print(tupla)
    for letra in tupla:
        if letra=="a":
            vocales+=1
        if letra=="e":
            vocales+=1
        if letra=="i":
            vocales+=1
        if letra=="o":
            vocales+=1
        if letra=="u":
            vocales+=1
    print(vocales)
    
#OTRO MODO
n=input("Introduzca una palabra :")
c=0
list=("a","e","i","o","u")
for x in n:
    if x.lower() in list:
        c=c+1
print("Hay "+str(c)+" vocales en la palabra "+n)

    
