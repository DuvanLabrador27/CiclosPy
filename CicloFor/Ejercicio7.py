menu="""
Bienvenido al registro de usuarios, llene los campos que usted prefiera a continuación seleccinando un numero
entre el 1-4:

[1] Digitar su nombre
[2] Digitar su edad
[3] Digitar su CC
[4] Digite su correo
"""
print(menu)
opcion=int(input("Ingrese la opción: "))
if opcion==1:
    nombre=input("Ingrese el nombre: ")
    print(f"Hola nombre que registro es {nombre}")
elif opcion==2:
    edad=int(input("Ingrese la edad: "))
    print(f"Hola, laedad que registro es {edad}")
elif opcion==3:
    cc=int(input("Ingrese la cc: "))
    print(f"Hola, la cc que registro es {cc}")
elif opcion==4:
    email=input("Ingrese el email: ")
    if email.find("@")>=0 and email.find(".")>=0:
        print(f"Tu email es valido {email}")
    else:
        print("El email no es valido, intenta de nuevo")
else:
   while opcion>=5:
        print("Error, operacion incorrecta, intentalo de nuevo!!")
        opcion=int(input("Ingrese la opción: "))
print(menu)

if opcion==1:
    nombre=input("Ingrese el nombre: ")
    print(f"Hola nombre que registro es {nombre}")
elif opcion==2:
    edad=int(input("Ingrese la edad: "))
    print(f"Hola, laedad que registro es {edad}")
elif opcion==3:
    cc=int(input("Ingrese la cc: "))
    print(f"Hola, la cc que registro es {cc}")
elif opcion==4:
    email=input("Ingrese el email: ")
    if email.find("@")>=0 and email.find(".")>=0:
        print(f"Tu email es valido {email}")
    else:
        print("El email no es valido, intenta de nuevo")
