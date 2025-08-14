def conbinacion():
    import sqlite3
    import pandas as pd
    from colorama import init, Fore
    import matplotlib.pyplot as plt

    init(autoreset=True)
    print("")
    print(Fore.LIGHTBLUE_EX + "*" * 100)
    print(Fore.LIGHTBLUE_EX + "Churn por combinación de servicios".center(100))
    print(Fore.LIGHTBLUE_EX + "*" * 100)
    print("")

    # Conectarse a la base de datos
    conn = sqlite3.connect("challengue.db")

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

    # Gráfico de barras
    plt.figure(figsize=(10, 6))
    plt.bar(df_churn_rate['serviceCombo'], df_churn_rate['churn_rate'], color='#FF6F61')
    plt.ylabel('Tasa de Churn (%)')
    plt.title('Tasa de Churn por Combinación de Servicios')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()


