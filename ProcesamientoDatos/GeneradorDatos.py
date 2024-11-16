import pandas as pd
import random
from faker import Faker
import numpy as np
import uuid
import os

fake = Faker()

def generar_usuarios(n=100):
    usuarios = []
    for _ in range(n):
        usuario = {
            "usuario_id": round(random.uniform(10000000, 1999999999)),
            "nombre": fake.name(),
            "direccion": fake.address(),
            "telefono": round(random.uniform(301000000, 321999999)),
            "metodo_pago": random.choice(['Tarjeta', 'Efectivo']),
            "promedio_calificacion": round(random.uniform(3.0, 5.0), 1)
        }
        usuarios.append(usuario)
    return pd.DataFrame(usuarios)

# Generar datos de conductores
def generar_conductores(n=50):
    conductores = []
    for _ in range(n):
        conductor = {
            "conductor_id": round(random.uniform(10000000, 1999999999)),
            "nombre": fake.name(),
            "telefono": round(random.uniform(301000000, 321999999)),
            "calificacion_promedio": round(random.uniform(3.0, 5.0), 1),
            "vehiculo": random.choice(["Honda", "Renault", "Chevrolet", "Hyundai", "Nissan"]),
        }
        conductores.append(conductor)
    return pd.DataFrame(conductores)

# Generar datos de viajes
def generar_viajes(n=500):
    viajes = []
    for _ in range(n):
        viaje = {
            "viaje_id": str(uuid.uuid4()),
            "usuario_id": random.choice(usuarios["usuario_id"]),
            "conductor_id": random.choice(conductores["conductor_id"]),
            "origen": fake.address(),
            "destino": fake.address(),
            "fecha": fake.date_this_year(),
            "hora": fake.time(),
            "distancia_km": round(random.uniform(2.0, 50.0), 2),
            "tiempo_minutos": round(random.uniform(5, 120), 0),
            "costo": round(random.uniform(5000, 2000000)),
            "calificacion_usuario": round(random.uniform(3.0, 5.0), 1)
        }
        viajes.append(viaje)
    return pd.DataFrame(viajes)

if not os.path.exists('./datos'):
    os.makedirs('./datos')

print("Directorio: ", os.getcwd())
# Generar los datos
usuarios = generar_usuarios(10000)
conductores = generar_conductores(120)
viajes = generar_viajes(150000)

# Guardar los datos en un archivo Excel
usuarios.to_excel(r'C:\Users\Quintero Pinto\Documents\Datos\Proyectos de Programacion\Big-Data\ProcesamientoDatos\datos\usuarios.xlsx', index=False)
conductores.to_excel(r'C:\Users\Quintero Pinto\Documents\Datos\Proyectos de Programacion\Big-Data\ProcesamientoDatos\datos\conductores.xlsx', index=False)
viajes.to_excel(r'C:\Users\Quintero Pinto\Documents\Datos\Proyectos de Programacion\Big-Data\ProcesamientoDatos\datos\viajes.xlsx', index=False)


    

print("Archivos Excel generados correctamente.")
