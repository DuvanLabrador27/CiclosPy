#Hacer un ejercicio de votacion, Fico-->1, petroGay-->2
def presidenteElecciones():
    numeroDeVotantes=int(input("Ingrese la cantidad de votantes: "))
    print("Fico Hermoso -->1")
    print("PetroGay-->2")
    cont=0
    contador=0
    for i in range(1,numeroDeVotantes+1):
        votos=int(input(f"VOTO#{i}, Ingrese el numero del candidato: "))
        while (votos<1 or votos>2):
            print("Opcion incorrecta!!")
            votos=int(input(f"VOTO#{i}, Ingrese el numero del candidato: "))
        if votos==1:
            cont+=1
        elif votos==2: 
            contador+=1
    print(f"El numero de votos para el candidado Fico es: {cont} ")
    
    print(f"El numero de votos para el candidado PetroGay es: {contador}")
presidenteElecciones()