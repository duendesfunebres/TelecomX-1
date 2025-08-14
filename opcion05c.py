def promedio():
    import sqlite3
    import pandas as pd
    import matplotlib.pyplot as plt
    import os
    from colorama import init, Fore

    init(autoreset=True)

    print("\n" + Fore.LIGHTBLUE_EX + "*" * 100)
    print(Fore.LIGHTBLUE_EX + 'Tasa de churn por método de pago'.center(100))
    print(Fore.LIGHTBLUE_EX + "*" * 100 + "\n")

    # Conectarse a la base de datos
    conn = sqlite3.connect("challengue.db")

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
    # Crear gráfico con matplotlib
    plt.figure(figsize=(10, 6))
    plt.barh(df_churn_rate['paymentMethod'], df_churn_rate['churn_rate'], color='skyblue')
    plt.title("Churn Rate by Payment Method", fontsize=16)
    plt.xlabel("Churn Rate (%)", fontsize=12)
    plt.ylabel("Payment Method", fontsize=12)
    plt.gca().invert_yaxis()  # Para que el más alto aparezca arriba
    plt.tight_layout()
    plt.show()
    # Definir carpeta de salida
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    plot_path = os.path.join(output_dir, "churn_rate_by_payment_method.png")

    # Guardar gráfico
    plt.savefig(plot_path)
    plt.close()

