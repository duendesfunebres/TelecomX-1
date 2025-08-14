def eliminacion():
    import sqlite3

    # Conectamos a la base de datos existente
    archivo = 'challengue.db'
    conn = sqlite3.connect(archivo)
    cursor = conn.cursor()

    # Obtenemos los nombres de todas las tablas
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tablas = cursor.fetchall()

    # Eliminamos todos los registros de cada tabla
    for tabla in tablas:
        nombre_tabla = tabla[0]
        try:
            cursor.execute(f"DELETE FROM {nombre_tabla};")
            print (f'Registros eliminados de la tabla {nombre_tabla} , presiones "ENTER" para continuar')
        except Exception as e:
            print(f"Error al eliminar registros de '{nombre_tabla}': {e}")

    # Guardamos los cambios y cerramos la conexión
    conn.commit()
    conn.close()

