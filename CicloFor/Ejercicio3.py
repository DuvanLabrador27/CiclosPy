
def divisor():
    numero=int(input("Ingrese el divisor: "))
    cont=0
    for dividendo in range(1,numero+1):
        if numero%dividendo==0:
            cont+=1
            print(f"El numero que esta dividendo si es divisor {dividendo}")
    
    print(f"Hay {cont} divsores")
divisor()