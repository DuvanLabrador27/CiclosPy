
def capturarDatos():
    global Lista
    Lista=[]
    numero_cantidad=int(input("Ingrese la cantidad de datos: "))
    for i in range(numero_cantidad):
        n=input("Ingrese el numero: ")
        Lista.append(n)

def mostrarDatos():
     print(Lista)

def agregarElemento():
    elemento=int(input("Ingrese el elemento que desea agregar: "))
    indice=int(input("Ingrese el indice: "))
    longitud=len(Lista)
    longitud=int(longitud)
    if indice>longitud or indice<0:
        print(f"El indice debe estar entre 0 y {longitud}")  
    else:
        Lista.insert(indice,elemento)
        print("El elemento a sido agg")
        print(Lista)

def eliminar():
    indice=int(input("Ingrese la posicion del elemento que desea eliminar: "))
    longitud=len(Lista)
    longitud=int(longitud)
    if indice>longitud or indice<0:
        print(f"El indice debe estar entre 0 y {longitud}")
    else:
        del Lista[indice]
        print("Elemento eliminado")
        print(Lista)

def modificar():
    indice=int(input("Ingrese la posicion del elemento que desea modificar: "))
    elemento=int(input("Ingrese el nuevo elemento: "))
    longitud=len(Lista)
    longitud=int(longitud)
    
    if indice>longitud or indice<0:
        print(f"El indice debe estar entre 0 y {longitud}")
    else:
        Lista[indice]=elemento
        print("Elemento modificado")
        print(Lista)

def menu():
    print("""
        1. Capturar Datos
        2. Mostrar Datos
        3. Agregar un elemento 
        4. Eliminar un elemento
        5. Modificar un elemento
        0. Salir!!
    
    """)
    opcion=1
    
    while opcion!=0:
        opcion=int(input("Ingrese la opcion: "))
        if opcion==1:
            capturarDatos()
        elif opcion==2:
            mostrarDatos()
        elif opcion==3:
            agregarElemento()
        elif opcion==4:
            eliminar()
        elif opcion==5:
            modificar()
        elif opcion==0:
            print("Gracias por usar nuestro sistema!!")
        else:
            print("Opcion Incorrecta, vuelva a intentar")

menu()



