def equipos():
    cantidadVotantes=int(input("Ingrese la cantidad de votantes: "))
    print("Peru -->1")
    print("Argentina -->2")

    cont=0
    cont2=0
    for i in range(1,cantidadVotantes+1):
        voto=int(input(f"Asistente numero {i}: "))
        while (voto <1 or voto >2):
            print("Opcion incorrecta!!")
            voto=int(input(f"Asistente numero {i}: "))
        if voto==1:
            cont+=1
        
        elif voto==2:
            cont2+=1
           
    print(f"Hay {cont}votos a peru ")
    print(f"Hay {cont2}votos a argentina ")
equipos()   
