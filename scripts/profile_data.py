import pandas as pd
from ydata_profiling import ProfileReport

def cargar_datos(path):
    """Carga el dataset desde un archivo CSV."""
    return pd.read_csv(path)

def resumen_general(df):
    """Devuelve resumen estadístico y estructura del DataFrame."""
    return {
        "dimensiones": df.shape,
        "columnas": df.columns.tolist(),
        "tipos": df.dtypes.to_dict(),
        "resumen": df.describe(include='all')
    }

def valores_nulos(df):
    """Devuelve el número y porcentaje de valores nulos por columna."""
    total = df.isnull().sum()
    porcentaje = (total / len(df)) * 100
    return pd.DataFrame({'nulos': total, '%': porcentaje}).sort_values(by='%', ascending=False)

def distribucion_variable(df, columna):
    """Devuelve la distribución de frecuencias de una columna."""
    return df[columna].value_counts(dropna=False)

def correlaciones(df):
    """Devuelve la matriz de correlación."""
    return df.corr(numeric_only=True)

if __name__ == "__main__":
    df = cargar_datos("data/ReBoot_Student_Stress_Factors.csv")
    print("📊 Resumen general:")
    print(resumen_general(df))

    print("\n📉 Valores nulos:")
    print(valores_nulos(df))

    print("\n🔗 Matriz de correlación:")
    print(correlaciones(df))

    # Genera informe visual completo
    profile = ProfileReport(df, title="ReBoot Student Stress Profile", explorative=True)
    profile.to_file("reports/EDA_Report.html")
    print("✅ Informe EDA guardado en reports/EDA_Report.html")
