import os
import pandas as pd
import sqlite3

# =========================
# Lectura del dataset
# =========================
df = pd.read_csv("data/dataset.csv")
print("Dataset original")
print(df)

# =========================
# Limpieza de datos
# =========================
df = df.drop_duplicates()
df = df.fillna(0)
print("Dataset limpio")
print(df)

# =========================
# Exportacion de dataset limpio
# =========================
os.makedirs("output", exist_ok=True)
df.to_csv("output/dataset_limpio.csv", index=False)
print("Archivo exportado correctamente")

# =========================
# Conexion SQLite (Base de datos local segura)
# =========================
os.makedirs("database", exist_ok=True)
conn = sqlite3.connect("database/laboratorio.db")
cursor = conn.cursor()

print("Conexion SQLite exitosa")

# =========================
# Creacion de tabla
# =========================
cursor.execute(""" 
CREATE TABLE IF NOT EXISTS clientes ( 
    id INT, 
    nombre TEXT, 
    edad INT, 
    ciudad TEXT 
) 
""")

conn.commit()
print("Tabla creada correctamente")

# =========================
# Insercion de registros
# =========================
cursor.execute("DELETE FROM clientes")
conn.commit()

for index, row in df.iterrows():
    cursor.execute(
        """ 
        INSERT INTO clientes (id, nombre, edad, ciudad) 
        VALUES (?, ?, ?, ?) 
        """,
        (
            int(row["id"]),
            str(row["nombre"]),
            int(float(row["edad"])),
            str(row["ciudad"]),
        ),
    )

conn.commit()
print("Datos insertados correctamente")

# =========================
# Validacion final
# =========================
cursor.execute("SELECT * FROM clientes")
resultado = cursor.fetchall()
print(f"Total registros: {len(resultado)}")
print("Datos almacenados en SQLite")

for fila in resultado:
    print(fila)

# =========================
# Cierre de conexion
# =========================
cursor.close()
conn.close()
print("Proceso finalizado correctamente")
