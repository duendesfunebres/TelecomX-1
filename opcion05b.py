def promedio():
    import sqlite3 
    import pandas as pd
    import matplotlib.pyplot as plt
    from colorama import init, Fore, Back
    init(autoreset=True) 
    init()
    # Conexión a la base de datos
    conn = sqlite3.connect("challengue.db")
    print ("")
    print (Fore.LIGHTBLUE_EX + 100*"*")
    print (Fore.LIGHTBLUE_EX+ " AGRUPAMIENTO DE CHURN SEGUN RANGOS DE TENURE".center(100))
    print (Fore.LIGHTBLUE_EX + 100*"*")
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

    # Gráfico
    plt.figure(figsize=(10, 6))
    plt.bar(df_churn_by_range['tenure_range'], df_churn_by_range['churn_rate'], color='#4C72B0')
    plt.title('Tasa de Churn por Rangos de Tenure')
    plt.xlabel('Rango de Tenure (meses)')
    plt.ylabel('Tasa de Churn (%)')
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Leyenda dentro del gráfico
    legend_text = "Churn = % de clientes que se dieron de baja en cada rango"
    plt.text(
        1.02, 0.5, legend_text,
        transform=plt.gca().transAxes,
        fontsize=9,
        verticalalignment='center',
        bbox=dict(facecolor='white', edgecolor='gray', boxstyle='round,pad=0.5')
    )

    plt.tight_layout()
    plt.show()