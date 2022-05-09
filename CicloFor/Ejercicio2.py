#Calcular la suma de todos los n numeros enteros ingresados
#La suma de los pares
#La suma de losimpares

n=int(input("Ingrese la cantidad de numeros: "))
sumaPar=0
sumaImpar=0
cont=0
conta=0
suma=0


for i in range(1,n+1):
    n2=int(input("Ingrese otro numero: "))
    suma=suma+n2
    if(n2%2==0):
        sumaPar=sumaPar+n2
        cont+=1
    else:
        sumaImpar=sumaImpar+n2
        conta+=1
print(f"Hay {cont} numeros pares")
print(f"La suma de los numeros pares es {sumaPar}")
print(f"Hay {conta} numeros Impares")
print(f"La suma de los numeros Impares es {sumaImpar}")
print(f"La suma es: {suma}")
