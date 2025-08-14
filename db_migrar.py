import sqlite3 as sql
import pandas as pd
import json


def createdb():
    conn= sql.connect ("challengue.db")
    conn.commit()
    conn.close()


def create_tabla ():
    conn = sql.connect('challengue.db')
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS telecomX (
	"customerId"	TEXT NOT NULL UNIQUE,
	"churn"	BOOLEAN NOT NULL,
	"gender"	TEXT NOT NULL,
	"seniorCitizen"	INTEGER NOT NULL,
	"partner"	BOOLEAN NOT NULL,
	"dependents"	BOOLEAN NOT NULL,
	"tenure"	INTEGER NOT NULL,
	"phoneService"	BOOLEAN NOT NULL,
	"multipleLines"	BOOLEAN NOT NULL,
	"internetService"	TEXT NOT NULL,
	"onlineSecurity"	BOOLEAN NOT NULL,
	"onlineBackup"	BOOLEAN NOT NULL,
	"deviceProtection"	BOOLEAN NOT NULL,
	"techSupport"	BOOLEAN NOT NULL,
	"streamingTV"	BOOLEAN NOT NULL,
	"streamingMovies"	BOOLEAN NOT NULL,
	"contract"	TEXT NOT NULL,
	"paperlessBilling"	BOOLEAN NOT NULL,
	"paymentMethod"	BLOB NOT NULL,
	"charges.Monthly"	DECIMAL NOT NULL,
	"charges.Total"	DECIMAL NOT NULL,
	PRIMARY KEY("customerId")
    )
    """)
    conn.commit()
    
# Obtener estructura de la tabla
    cursor.execute("PRAGMA table_info(telecomX)")
    columnas = cursor.fetchall()
    # Convertir a DataFrame
    df_columnas = pd.DataFrame(columnas, columns=["cid", "nombre", "tipo", "notnull", "valor_defecto", "pk"])
    # Mostrar solo columnas relevantes y renombrarlas
    df_columnas = df_columnas[["nombre", "tipo", "notnull", "pk"]]
    df_columnas.columns = ["Nombre", "Tipo", "¿NOT NULL?", "¿Clave Primaria?"]

    print(df_columnas.to_string(index=False))
    conn.close()
create_tabla()

