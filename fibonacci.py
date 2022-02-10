#############recursividad  fibonacci en una funcion con tantos numeros como pida#############
limite=int(input("Cuantos numeros desea: "))

#funcion
def fibonacciFuncion(numero):
    if(numero==0):
        return 0
    elif(numero==1):
        return 1
    else:
        return (fibonacciFuncion(numero-2)+fibonacciFuncion(numero-1)) 


#parte principal
for n in range(0, limite):
  print(fibonacciFuncion(n))