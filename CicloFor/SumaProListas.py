
suma=0
Lista=[]
numero=int(input("Inngrese la cantidad de numeros: "))
for i in range(numero):
    num=int(input(f"Ingrese un numero {i}: "))
    Lista.append(num)
    suma=suma+num
promedio=suma/numero
print(Lista)
print(f"La suma es {suma}")
print(f"El promedio es: {promedio}")

f=1
n=int(input("Ingrese la cantidad: "))
for j in range(1,n+1):
    f=f*j
print(f)