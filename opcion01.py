def  extraccion():
    import pandas as pd 
    from colorama import init, Fore, Back
    import json
    init(autoreset=True) 
    init()

    # Cargar JSON desde archivo
    with open('TelecomX.json', 'r', encoding='utf-8') as f:
        datos = json.load(f)
        print (Fore.BLUE + f'INFORMACIÓN DE DATOS "TELECOMX.JSON"'.center(100))
        print ("")
        print (Fore.LIGHTBLUE_EX + 100*"*")
        print (Fore.BLUE + " ESTRUCTURA".center(100))
        print (Fore.LIGHTBLUE_EX + 100*"*")
        print ("")


        def buscar_campos_vacios(data, path=""):
            vacios = []
            if isinstance(data, dict):
                for k, v in data.items():
                    nueva_ruta = f"{path}.{k}" if path else k
                    vacios.extend(buscar_campos_vacios(v, nueva_ruta))
            elif isinstance(data, list):
                for i, item in enumerate(data):
                    nueva_ruta = f"{path}[{i}]"
                    vacios.extend(buscar_campos_vacios(item, nueva_ruta))
            else:
                if str(data).strip() == "":
                    vacios.append(path)
            return vacios

        # Contadores
        total_vacios = 0

        for cliente in datos:
            vacios = buscar_campos_vacios(cliente)
            total_vacios += len(vacios)


        # Función recursiva que maneja campos de nivel superior y anidados
        def recolectar_tipos(diccionario, prefijo=""):
            tipos = []
            for clave, valor in diccionario.items():
                ruta = f"{prefijo}{clave}"
                if isinstance(valor, dict):
                    tipos.extend(recolectar_tipos(valor, prefijo=ruta + "."))
                else:
                    tipos.append({"Campo": ruta, "Tipo de dato": type(valor).__name__})
            return tipos
        
        # Obtener primer registro y recolectar todos sus campos
        tipos_datos = recolectar_tipos(datos[0])
        # Crear DataFrame y mostrarlo ordenado
        df_tipos = pd.DataFrame(tipos_datos)
        print(df_tipos.sort_values("Campo").reset_index(drop=True).to_string(index=False))
        
        print ("")
        print (Fore.LIGHTBLUE_EX + 100*"*")
        print (Fore.BLUE + "ESTADÍSTICAS".center(100))
        print (Fore.LIGHTBLUE_EX + 100*"*")
        print ("")


        # R esultados generales
        print(Fore.LIGHTBLUE_EX + f"🔍 Total de campos vacíos: {total_vacios}")
        print(Fore.LIGHTBLUE_EX + f"🔍 Cantidad de registros totales: {len(datos)}")
