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
    subtotal=Precio*Cant
    print("El subtotal es", subtotal)
    D=int(input("Ingrese forma de pago: 1 si es efectivo(-10%), 2 si es credito"))
    if D==1:
        TotalD= subtotal *0,10
        print("El total es", TotalD)
    else:
        print("El total es", subtotal)

else:
    print("No hay clientes")


