#CALCULAR LA SUMA DE DE LOS CUADRADOS DE N NUMEROS,
#  TENIENDO EN CUENTA QUE DEBEN SER POSITIVOS
n=int(input("Ingrese el numero: "))
while n<=0:
    print("Numero incorreco, debe ser un valor positivo!! ")
    n=int(input("Ingrese el numero: "))
suma=0
for i in range(1,n+1):
    numero=i**2
    suma=suma+numero
print(f"La suma es: {suma}")

"""
n=3
i**2 
Cuando i=1
1*1=1

suma vale=1

Cuando i=2
2*2=4

suma vale =5

Cuando i=3
3*3=9

suma vale=14

"""