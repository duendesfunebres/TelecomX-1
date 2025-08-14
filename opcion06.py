def informe():

    import sqlite3 as sql
    import pandas as pd
    from colorama import init, Fore, Back
    import matplotlib.pyplot as plt
    import locale
    def limpiar (): #funciòn llamad para limpiar pantallas
        from os import system
        system ("cls")

    init(autoreset=True) 
    init()
    print ("")
    print (Fore.LIGHTBLUE_EX + 150*"*")
    print (Fore.LIGHTBLUE_EX+ "INFORME FINAL SOBRE DISTRIBUCIÓN DE CHURN".center(150))
    print (Fore.LIGHTBLUE_EX + 150*"*")
    print ("")

    # Conectarse a la base de datos
    conn = sql.connect("challengue.db")
    # Consulta SQL
    query = """
    SELECT "contract" AS contract, churn, COUNT(*) AS total
    FROM telecomX
    GROUP BY "contract", churn
    ORDER BY "contract", churn;
    """
    # Ejecutar la consulta
    df = pd.read_sql_query(query, conn)

    # Pivotear correctamente usando nombres reales
    pivot_df = df.pivot(index='contract', columns='churn', values='total').fillna(0)
    pivot_df.columns = ['No_Churn', 'Churn']
    pivot_df['Total'] = pivot_df['No_Churn'] + pivot_df['Churn']
    pivot_df['Churn_Rate (%)'] = (pivot_df['Churn'] / pivot_df['Total']) * 100
    # Conectarse a la base de datos
    conn = sql.connect('challengue.db')
    cursor = conn.cursor()
    locale.setlocale(locale.LC_ALL, 'es_AR.UTF-8')
    cursor.execute('SELECT SUM("charges.Total") AS suma_total FROM telecomX;')
    resultado = cursor.fetchone()
    suma_formateada = locale.format_string("%.2f", resultado[0], grouping=True)
    cursor.execute("SELECT COUNT(customerid) AS suma_total FROM telecomX;")
    # Obtener el resultado
    conteo = cursor.fetchone()
    cursor.execute("SELECT COUNT(customerid) AS churn_count FROM telecomX WHERE churn = 1;")
    # Obtener el resultado
    abandono= cursor.fetchone()
    # Cerrar la conexión
    conn.close()
    # Mostrar resultado

    # Cerrar conexión
    conn.close()

    print(f"▶️  DATOS SOBRE LOS CUALES SE REALIZARON LAS ESTADÌSTICAS :")
    print ("")
    print(f"✅  Total de clientes analizados: {conteo [0]}")
    print(f"✅  Total facturaciòn socios activos: ${suma_formateada}")
    print(f"✅  Totla clientes que se desvincularon: {abandono [0]}")
    print ("")
    print (100*"*")
    print ('presione "ENTER" para continuar...')
    input()
    limpiar()
    #**********************************************************************************************************
    print ("")
    print (Fore.LIGHTGREEN_EX + 150*"*")
    print (Fore.LIGHTGREEN_EX+ "DISTRIBUCIÒN DE CHURN POR TIPO DE CONTRATO".center(150))
    print (Fore.LIGHTGREEN_EX + 150*"*")
    print ("")
    print(pivot_df.round(2))
    print ("")
    print (Fore.LIGHTGREEN_EX + 150*"-")
    print(Fore.LIGHTGREEN_EX + '✅  En la grilla inmediato según "tipo de contrato" podemos observar que se dispone de un incremento')
    print(Fore.LIGHTGREEN_EX + '    en clientes que abandonan el servicion sobre contratos del tipo "Month-to-month" donde de 2350 usuarios de ese sistema de contraro,')
    print(Fore.LIGHTGREEN_EX +'    1655 abndonan el servicio con una tasa de  41.32%, inmediatamente le siguen los contrato "One-Year" con una tasa mucho menor de 10.94%')
    print (Fore.LIGHTGREEN_EX + 150*"-")
    print("")
    print ('presione "ENTER" para continuar...')
    input()
    limpiar()
    #***********************************************************************************************************

    # Conexión a la base de datos
    conn = sql.connect("challengue.db")
    print ("")
    print (Fore.LIGHTBLUE_EX + 150*"*")
    print (Fore.LIGHTBLUE_EX+ " AGRUPAMIENTO DE CHURN SEGUN RANGOS DE TENURE".center(150))
    print (Fore.LIGHTBLUE_EX + 150*"*")
    print ("")
    # Consulta con agrupamiento por rangos de tenure
    query = """
    SELECT
        CASE
            WHEN tenure BETWEEN 0 AND 12 THEN '0–12'
            WHEN tenure BETWEEN 13 AND 24 THEN '13–24'
            WHEN tenure BETWEEN 25 AND 36 THEN '25–36'
            WHEN tenure BETWEEN 37 AND 48 THEN '37–48'
            WHEN tenure BETWEEN 49 AND 60 THEN '49–60'
            WHEN tenure BETWEEN 61 AND 72 THEN '61–72'
            ELSE '72+'
        END AS tenure_range,
        COUNT(*) AS total_customers,
        SUM(churn) AS churned,
        ROUND(CAST(SUM(churn) AS FLOAT) / COUNT(*) * 100, 2) AS churn_rate
    FROM telecomX
    GROUP BY tenure_range;
    """
    df_churn_by_range = pd.read_sql_query(query, conn)
    conn.close()

    # Ordenar los rangos manualmente para que el gráfico tenga sentido
    orden_rangos = ['0–12', '13–24', '25–36', '37–48', '49–60', '61–72', '72+']
    df_churn_by_range['tenure_range'] = pd.Categorical(df_churn_by_range['tenure_range'], categories=orden_rangos, ordered=True)
    df_churn_by_range = df_churn_by_range.sort_values('tenure_range')


    print(df_churn_by_range)


    print (Fore.LIGHTGREEN_EX + 150*"-")
    print(Fore.LIGHTGREEN_EX + '✅  Según clientes enmarcados en tenure del rango entre 0 a 12 incrementan el churn en una tasa de 46.01% de un total de 2254 clientes, 1037 migraron')
    print(Fore.LIGHTGREEN_EX + '    mientras el siguiente está en el rango de 13 a 24 con una tasa de 28.13 en un total de 294 del total de 1045 personas,')
    print (Fore.LIGHTGREEN_EX + 150*"-")

    print ('presione "ENTER" para continuar...')
    input()
    limpiar()
    #***********************************************************************************************************************

    print("\n" + Fore.LIGHTMAGENTA_EX + "*" * 150)
    print(Fore.LIGHTMAGENTA_EX + 'Tasa de churn por método de pago'.center(150))
    print(Fore.LIGHTMAGENTA_EX + "*" * 150 + "\n")
    # Conectarse a la base de datos
    conn = sql.connect("challengue.db")
    query_churn_rate = """
    SELECT 
        paymentMethod, 
        COUNT(*) AS total_customers,
        SUM(CASE WHEN churn = 1 THEN 1 ELSE 0 END) AS churned_customers,
        ROUND(100.0 * SUM(CASE WHEN churn = 1 THEN 1 ELSE 0 END) / COUNT(*), 2) AS churn_rate
    FROM telecomX
    GROUP BY paymentMethod
    ORDER BY churn_rate DESC;
    """
    df_churn_rate = pd.read_sql_query(query_churn_rate, conn)
    conn.close()

    # Decodificar BLOB si es necesario
    df_churn_rate['paymentMethod'] = df_churn_rate['paymentMethod'].apply(
        lambda x: x.decode() if isinstance(x, bytes) else x
    )

    print(df_churn_rate)
    print("")
    print (Fore.LIGHTGREEN_EX + 150*"-")
    print(Fore.LIGHTGREEN_EX + '✅  En un estudio sobre  la tasa de churn según la metodología de pago, el análisis')
    print(Fore.LIGHTGREEN_EX + '    resalta que con el método "pago electrónico, mantiene una tasa de 43% de clientes que abandonan el servicio"')
    print(Fore.LIGHTGREEN_EX + '    lLego el porcentaje cae a 18.5% con el pago por correo')
    print (Fore.LIGHTGREEN_EX + 150*"-")

    print ('presione "ENTER" para continuar...')
    input()
    limpiar()
    #*********************************************************************************************

    init(autoreset=True)
    print("")
    print(Fore.LIGHTBLACK_EX + "*" * 100)
    print(Fore.LIGHTBLACK_EX  + "Churn por combinación de servicios".center(100))
    print(Fore.LIGHTBLACK_EX  + "*" * 100)
    print("")

    # Conectarse a la base de datos
    conn = sql.connect("challengue.db")

    # Consulta para calcular tasa de churn por combinación de servicios

    query_churn_rate = """
    SELECT
        serviceCombo,
        COUNT(*) AS total_customers,
        SUM(CASE WHEN churn THEN 1 ELSE 0 END) AS churned,
        ROUND(
            CAST(SUM(CASE WHEN churn THEN 1 ELSE 0 END) AS FLOAT) / COUNT(*) * 100,
            2
        ) AS churn_rate
    FROM (
        SELECT
            churn,
            (
                CASE WHEN onlineSecurity THEN 'OS-' ELSE '' END ||
                CASE WHEN onlineBackup THEN 'OB-' ELSE '' END ||
                CASE WHEN deviceProtection THEN 'DP-' ELSE '' END ||
                CASE WHEN techSupport THEN 'TS-' ELSE '' END ||
                CASE WHEN streamingTV THEN 'STV-' ELSE '' END ||
                CASE WHEN streamingMovies THEN 'SM-' ELSE '' END
            ) AS serviceCombo
        FROM telecomX
    )
    GROUP BY serviceCombo
    ORDER BY churn_rate DESC;
    """

    # Ejecutar consulta y cargar en DataFrame
    df_churn_rate = pd.read_sql_query(query_churn_rate, conn)
    print(df_churn_rate)
    conn.close()
    print(Fore.YELLOW + "\nLeyenda de combinaciones de servicios:")
    print(Fore.YELLOW + "OS  = Online Security")
    print(Fore.YELLOW + "OB  = Online Backup")
    print(Fore.YELLOW + "DP  = Device Protection")
    print(Fore.YELLOW + "TS  = Tech Support")
    print(Fore.YELLOW + "STV = Streaming TV")
    print(Fore.YELLOW + "SM  = Streaming Movies\n")
    conn.close()
    print("")
    print(Fore.LIGHTGREEN_EX + 150*"-")
    print(Fore.LIGHTGREEN_EX + '✅ En el análisis de servicios y convinación de los mismos resulta con mayor afección a a pérdida de cliente, ')
    print(Fore.LIGHTGREEN_EX + '   el servico Streaming Movies dentro de un 62.50% de 192 clientes que abandonan en un totald de 192')
    print(Fore.LIGHTGREEN_EX  + '    lLego el porcentaje cae a 18.5% con el pago por correo')
    print(Fore.LIGHTGREEN_EX  + 150*"-")
    print ('presione "ENTER" para continuar...')
    input()
    limpiar()


    print(Fore.RED+ 150*"-")
    print(Fore.RED + ' CONCLUSIÓN Y RECOMENDACIÓN FINAL'.center(150))
    print(Fore.RED+ 150*"-")
    print(Fore.RED + 'En un  resumen final, los factores de riesgo de périda estan asentuados sobre los siguientes pilares, '.center(150))
    print(Fore.RED + 'tipo de contrato el servico del servicio "Month to Month", rango de tenure de 0 a 12, Método de pago por "Pago'.center(150))
    print(Fore.RED + 'Electrónico" y finalmente servicio de "Streaming Movies"'.center(150))
    print(Fore.RED + 'Se debería hacer un seguimiento exhaustivo a cada propuesta para minimizar la fuga de clientes al mínimo"'.center(150))
    print(Fore.RED + 150*"-")
    input()
    limpiar()

    