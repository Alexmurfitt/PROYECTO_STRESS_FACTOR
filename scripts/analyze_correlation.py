# Importar las librerías necesarias
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar el dataset
df = pd.read_csv('../data/ReBoot_Student_Stress_Factors.csv')

# Análisis inicial
print("Primeras filas del dataset:")
print(df.head())

# Información general sobre el dataset
print("\nInformación general del dataset:")
df_info = df.info()

# Estadísticas descriptivas
print("\nEstadísticas descriptivas del dataset:")
df_describe = df.describe()

# Revisar valores nulos
print("\nValores nulos por columna:")
missing_data = df.isnull().sum()

# Revisar registros duplicados
print("\nRegistros duplicados en el dataset:")
duplicate_data = df.duplicated().sum()

# Calcular la matriz de correlación
correlation_matrix = df.corr()

# Mostrar la matriz de correlación
print("\nMatriz de correlación:")
print(correlation_matrix)

# Visualizar la matriz de correlación como un heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="coolwarm", cbar=True, vmin=-1, vmax=1)
plt.title('Matriz de Correlación de Variables')
plt.show()

# Guardar la matriz de correlación en un archivo CSV
correlation_matrix.to_csv('reports/correlation_matrix.csv', index=True)
print("\nLa matriz de correlación ha sido exportada a 'reports/correlation_matrix.csv'.")
