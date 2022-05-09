lista=[]
suma=0
n=int(input("Ingrese la cantidad: "))
for i in range(n):
    nota=int(input("Ingrese la nota: "))
    lista.append(nota)
    suma=suma+lista[i]
promedio=suma/n        
print(f"La suma es {suma}")
print(f"El promedio es {promedio}")
print(lista)