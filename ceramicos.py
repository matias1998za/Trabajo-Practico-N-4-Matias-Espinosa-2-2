F=int(input("Ingrese 1  si hay cliente, 2 si no hay"))
if F==1:
    L=int(input("Ingresar largo de habitacion"))
    A=int(input("Ingresar ancho de habitacion"))
    ETN=L*A
    LC=int(input("Ingresar largo de ceramico"))
    AC=int(input("Ingresar ancho de ceramico"))
    ETM=LC*AC
    Cantcera=ETN/ETM
    print("La cantidad de ceramicos necesarios es", Cantcera)
    Cant=Cantcera/10
    print("La cantidad de cajas necesarias son:", Cant)
    Precio=int(input("Ingresar el precio por caja"))
    Preciototal=Precio*Cant
    print("El precio total es", Preciototal)
else:
    print("No hay clientes")
