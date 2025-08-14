
def migracion():
    import sqlite3
    import pandas as pd
    from colorama import init, Fore, Back
    import matplotlib.pyplot as plt
    init(autoreset=True) 
    init()
    # Conectarse a la base de datos
    conn = sqlite3.connect("challengue.db")

    # Consulta SQL
    query = """
    SELECT "contract" AS contract, churn, COUNT(*) AS total
    FROM telecomX
    GROUP BY "contract", churn
    ORDER BY "contract", churn;
    """
    # Ejecutar la consulta
    df = pd.read_sql_query(query, conn)
    print ("")
    print (Fore.LIGHTBLUE_EX + 100*"*")
    print (Fore.LIGHTBLUE_EX+ "DISTRIBUCIÒN DE CHURN POR TIPO DE CONTRATO".center(100))
    print (Fore.LIGHTBLUE_EX + 100*"*")
    print ("")
    # Pivotear correctamente usando nombres reales
    pivot_df = df.pivot(index='contract', columns='churn', values='total').fillna(0)
    pivot_df.columns = ['No_Churn', 'Churn']
    pivot_df['Total'] = pivot_df['No_Churn'] + pivot_df['Churn']
    pivot_df['Churn_Rate (%)'] = (pivot_df['Churn'] / pivot_df['Total']) * 100

    # Mostrar resultado
    print(pivot_df.round(2))
    print ("")
    # Cerrar conexión
    conn.close()

    # Crear gráfico de barras
    plt.figure(figsize=(8, 5))
    plt.bar(pivot_df.index, pivot_df['Churn_Rate (%)'], color=['#FF6F61', '#6BAED6', '#74C476'])

    # Etiquetas y título
    plt.title('Tasa de Churn por Tipo de Contrato', fontsize=14)
    plt.xlabel('Tipo de Contrato', fontsize=12)
    plt.ylabel('Churn (%)', fontsize=12)
    plt.ylim(0, 50)  # Ajustar según tus datos
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Mostrar valores encima de las barras
    for i, value in enumerate(pivot_df['Churn_Rate (%)']):
        plt.text(i, value + 1, f'{value:.1f}%', ha='center', fontsize=10)

    # Mostrar gráfico
    plt.tight_layout()
    plt.show()
    print("Presiona Enter para continuar...")