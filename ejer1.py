from datetime import datetime

def calcular_dias():
    formato = "%d-%m"
    
    # Ingresar las fechas sin año
    fecha1 = datetime.strptime(input("Ingrese la primera fecha (dd-mm): ") + f"-{datetime.now().year}", formato + "-%Y")
    fecha2 = datetime.strptime(input("Ingrese la segunda fecha (dd-mm): ") + f"-{datetime.now().year}", formato + "-%Y")
    
    return abs((fecha2 - fecha1).days)

dias = calcular_dias()
print(f"Días entre las fechas: {dias}")
