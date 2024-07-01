import os

registro = []

marca = ["Toyota", "Ford", "Chevrolet"]

titulo = """
+-----------------------------------------------------------------------------------------------------+
|   MARCA       AÑO     KILOMETRAJE     COSTO DE REPARACION       IMPUESTO DE SERVICIO      TOTAL     |           |                                                           |
+-----------------------------------------------------------------------------------------------------+
"""

menu = """
1. Registrar vehiculo
2. Listar todos los registros
3. Imprimir orden de reparacion
4. Salir\n
"""

def registrarVehiculo():
    while True:
        try:
            ingreso = []
            print("""
Para registrar un vehiculo se requiere de los siguientes datos 
Marca
Año de fabricacion 
Kilometraje
Costo de reparacion estimado en clp            
\n""")
            marca = input("Ingrese la marca del vehiculo\n").capitalize().strip()
            año   = int(input("Ingrese el año de fabricacion del vehiculo\n"))
            kilometraje = int(input("Ingrese el kilometraje del vehiculo\n"))
            costo = int(input("Ingrese el costo aproximado de la reparacion\n"))
            impuesto = costo*0.08
            total = costo + impuesto
            if len(marca) > 0 and año > 0 and kilometraje > 0 and costo > 0:
                ingreso.append([marca,año,kilometraje,costo,impuesto,total])
                registro.append(ingreso)
                break
        except ValueError:
            print("Error de registro, reintente...")


def listarVehiculos():
    print(titulo)
    for registros in registro:
        print(registros)

def imprimir():
    pass

while True:
    try:
        opc = int(input(menu)) 
        if opc in (1,2,3,4):
            os.system("cls")
            if opc == 1:
                registrarVehiculo()
            elif opc == 2:
                listarVehiculos()
            elif opc == 3:
                imprimir()
            elif opc == 4:
                exit()    
        
    except ValueError:
        print("Seleccione una opcion valida...")            
