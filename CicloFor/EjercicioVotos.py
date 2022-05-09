"""
Hacer un programa que permita digitar el numero de votos que se pueden realizar, tambien que tenga un conteo de votos 
el voto solo es permitido si el email es valido
"""

cont=0
cont2=0
email=input("Ingrese el email: ")
if email.find("@")>=0 and email.find(".")>=0:
    print("Email correcto!!")
    print("Barcelona-->1")
    print("City-->2")
    
    cantidadVotos=int(input("Ingrese la cantidad de votos: "))
    for i in range(1,cantidadVotos+1):
        votos=int(input(f"Voto #{i}, Ingrese el numero del candidato: "))
        while (votos<1 or votos>2):
            print("Opcion incorrecta!!")
            votos=int(input(f"VOTO#{i}, Ingrese el numero del candidato: "))
        if votos==1:
            cont+=1
        elif votos==2:
            cont2+=1
    
else:
    print("Email incorrecto!!")
print(f"El numero de votos para el Barcelona es: {cont} ")
    
print(f"El numero de votos para el city es: {cont2}")

        
        
      
        
        
   
   



       
    
    
    
   
