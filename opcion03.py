def migracion():
    import sqlite3
    from colorama import init, Fore, Back
    init(autoreset=True) 
    init()

    print ("")
    print (Fore.LIGHTBLUE_EX + 100*"*")
    print (Fore.LIGHTBLUE_EX + " SE MIGRARAN TODOS LOS DATOS DE TELECOMX.JSON A TELECOMX.DB A UN FORMATO NORMALIZADO".center(100))
    print (Fore.LIGHTBLUE_EX + 100*"*")
    print (Fore.LIGHTBLUE_EX + 'Serán transferidos respetando su tipo de datos en cada columnna) '.center(100))
    print (Fore.LIGHTBLUE_EX + '(Los contenidos "NAN", serán migrados como "NULL", para no afectar la contabilidad de cantidades ) '.center(100))
    print (Fore.LIGHTBLUE_EX + 100*"*")
    print ("")
    print ("")
    input("Presiona Enter para continuar...")

    import sqlite3 as sql
    import json

    #JSON original
    with open('TelecomX.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
    

    #Mapeos
    bool_map = {"Yes": True, "No": False}
    contract_map = {"Month-to-month": 0, "One year": 1, "Two year": 2}

    #Función para limpiar y transformar cada registro
    def transform(record):
        try:
            return (
                record["customerID"],
                bool_map.get(record["Churn"], False),
                record["customer"]["gender"],
                int(record["customer"]["SeniorCitizen"]),
                bool_map.get(record["customer"]["Partner"], False),
                bool_map.get(record["customer"]["Dependents"], False),
                int(record["customer"]["tenure"]),  # Si querés usar tenure como contrato, sino cambia
                bool_map.get(record["phone"]["PhoneService"], False),
                bool_map.get(record["phone"]["MultipleLines"], False),
                record["internet"]["InternetService"],
                bool_map.get(record["internet"]["OnlineSecurity"], False),
                bool_map.get(record["internet"]["OnlineBackup"], False),
                bool_map.get(record["internet"]["DeviceProtection"], False),
                bool_map.get(record["internet"]["TechSupport"], False),
                bool_map.get(record["internet"]["StreamingTV"], False),
                bool_map.get(record["internet"]["StreamingMovies"], False),
                record["account"]["Contract"],
                bool_map.get(record["account"]["PaperlessBilling"], False),
                record["account"]["PaymentMethod"],
                float(record["account"]["Charges"]["Monthly"]),
                #float(record["account"]["Charges"]["Total"]) if record["account"]["Charges"]["Total"] not in ["NaN", None, ""] else None
                #float(record["account"]["Charges"]["Total"]) if record["account"]["Charges"]["Total"] not in ["NaN", None, ""] else None
                safe_float(record["account"]["Charges"]["Total"])
            )
        except Exception as e:
            print(f"Error en registro {record['customerID']}: {e}")
            return None
            safe_float(record["account"]["Charges"]["Total"])
    
    def safe_float(value):
        try:
            return float(value)
        except (ValueError, TypeError):
            return None
        
    # Conexión a SQLite
    conn = sql.connect("challengue.db")
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM telecomX")
    cantidad_filas = cursor.fetchone()[0]
    if cantidad_filas == 0:
        # Insertar datos
        for record in data:
            row = transform(record)
            if row:
                cursor.execute("""
                INSERT OR IGNORE INTO telecomX VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, row)

        cant = cursor.execute ("SELECT COUNT(*) FROM telecomX;")
        conn.commit()
        conn.close()
        print ("")
        print (Fore.LIGHTBLUE_EX + 100*"*")
        print (Fore.LIGHTBLUE_EX + 'DATOS MIGRADOS EXITOSAMENTE (presione "ENTER para volver al  menù")'.center(100))
        print (Fore.LIGHTBLUE_EX + 100*"*")
        #input("Presiona Enter para continuar...")
    else:
        print ("La base de datos ya tiene cargado todos los registros del archivo TelecomX.json")