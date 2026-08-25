import os

os.environ["LC_ALL"] = "C"
import pandas as pd
import psycopg2

# =========================
# Lectura del dataset
# =========================
df = pd.read_csv("data/dataset.csv")
print("Dataset original")
print(df)

# =========================
# Limpieza de datos
# =========================
# Eliminacion de duplicados
df = df.drop_duplicates()
# Reemplazo de valores nulos
df = df.fillna(0)
print("Dataset limpio")
print(df)

# =========================
# Exportacion de dataset limpio
# =========================
df.to_csv("output/dataset_limpio.csv", index=False)
print("Archivo exportado correctamente")

# =========================
# Conexion PostgreSQL
# =========================
db_host = "127.0.0.1"
db_name = "laboratorio"
db_user = "admin"
db_pass = "admin123"

# Forzar codificacion estricta en el sistema para psycopg2
os.environ["LANG"] = "en_US.UTF-8"
os.environ["LC_ALL"] = "en_US.UTF-8"

conn = psycopg2.connect(host=db_host, database=db_name, user=db_user, password=db_pass)
cursor = conn.cursor()

print("Conexion PostgreSQL exitosa")

# =========================
# Creacion de tabla
# =========================
cursor.execute(""" 
CREATE TABLE IF NOT EXISTS clientes ( 
    id INT, 
    nombre VARCHAR(50), 
    edad INT, 
    ciudad VARCHAR(50) 
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
        VALUES (%s, %s, %s, %s) 
        """,
        (int(row["id"]), row["nombre"], int(float(row["edad"])), row["ciudad"]),
    )

conn.commit()
print("Datos insertados correctamente")

# =========================
# Validacion final
# =========================
cursor.execute("SELECT * FROM clientes")
resultado = cursor.fetchall()
print(f"Total registros: {len(resultado)}")
print("Datos almacenados en PostgreSQL")

for fila in resultado:
    print(fila)

# =========================
# Cierre de conexion
# =========================
cursor.close()
conn.close()
print("Proceso finalizado correctamente")
