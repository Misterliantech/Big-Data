import pyodbc
import pandas as pd

# Datos de conexión
server = 'localhost'  # por ejemplo, 'localhost' o '192.168.1.100'
database = 'Taxis'
username = 'Quintero'
password = 'Clave123'

# Conexión a la base de datos SQL Server
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                      f'SERVER={server};'
                      f'DATABASE={database};'
                      f'UID={username};'
                      f'PWD={password};'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()

# Cargar los archivos Excel en DataFrames de Pandas
usuarios_df = pd.read_excel('C:\\Users\\Quintero Pinto\\Documents\\Datos\\Proyectos de Programacion\\Big-Data\\ProcesamientoDatos\\datos\\usuarios.xlsx')
conductores_df = pd.read_excel('C:\\Users\\Quintero Pinto\\Documents\\Datos\\Proyectos de Programacion\\Big-Data\\ProcesamientoDatos\\datos\\conductores.xlsx')
viajes_df = pd.read_excel('C:\\Users\\Quintero Pinto\\Documents\\Datos\\Proyectos de Programacion\\Big-Data\\ProcesamientoDatos\\datos\\viajes.xlsx')

# Crear las tablas (si no existen)
cursor.execute('''
IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='usuarios' AND xtype='U')
BEGIN
    CREATE TABLE usuarios (
        usuario_id INT PRIMARY KEY,
        nombre NVARCHAR(255),
        direccion NVARCHAR(255),
        telefono NVARCHAR(50),
        metodo_pago NVARCHAR(50),
        promedio_calificacion FLOAT
    )
END
''')

cursor.execute('''
IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='conductores' AND xtype='U')
BEGIN
    CREATE TABLE conductores (
        conductor_id INT PRIMARY KEY,
        nombre NVARCHAR(255),
        telefono NVARCHAR(50),
        calificacion_promedio FLOAT,
        vehiculo NVARCHAR(50)
    )
END
''')

cursor.execute('''
IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='viajes' AND xtype='U')
BEGIN
    CREATE TABLE viajes (
        viaje_id INT PRIMARY KEY,
        usuario_id INT,
        conductor_id INT,
        origen NVARCHAR(255),
        destino NVARCHAR(255),
        fecha DATE,
        hora TIME,
        distancia_km FLOAT,
        tiempo_minutos INT,
        costo INT,
        calificacion_usuario FLOAT,
        FOREIGN KEY (usuario_id) REFERENCES usuarios(usuario_id),
        FOREIGN KEY (conductor_id) REFERENCES conductores(conductor_id)
    )
END
''')

# Insertar los datos de los DataFrames en SQL Server

# Insertar los usuarios
for index, row in usuarios_df.iterrows():
    cursor.execute('''
        INSERT INTO usuarios (usuario_id, nombre, direccion, telefono, metodo_pago, promedio_calificacion)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', row['usuario_id'], row['nombre'], row['direccion'], row['telefono'], row['metodo_pago'], row['promedio_calificacion'])

# Insertar los conductores
for index, row in conductores_df.iterrows():
    cursor.execute('''
        INSERT INTO conductores (conductor_id, nombre, telefono, calificacion_promedio, vehiculo)
        VALUES (?, ?, ?, ?, ?)
    ''', row['conductor_id'], row['nombre'], row['telefono'], row['calificacion_promedio'], row['vehiculo'])

# Insertar los viajes
for index, row in viajes_df.iterrows():
    cursor.execute('''
        INSERT INTO viajes (viaje_id, usuario_id, conductor_id, origen, destino, fecha, hora, distancia_km, tiempo_minutos, costo, calificacion_usuario)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', row['viaje_id'], row['usuario_id'], row['conductor_id'], row['origen'], row['destino'], row['fecha'], row['hora'], row['distancia_km'], row['tiempo_minutos'], row['costo'], row['calificacion_usuario'])

# Confirmar los cambios y cerrar la conexión
conn.commit()

# Cerrar la conexión
conn.close()

print("Datos cargados exitosamente en la base de datos SQL Server.")
