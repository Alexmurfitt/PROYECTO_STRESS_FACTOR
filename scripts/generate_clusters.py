from sklearn.cluster import KMeans
import pandas as pd

# Cargar los datos originales (usamos el archivo CSV original)
df = pd.read_csv("data/ReBoot_Student_Stress_Factors.csv")

# Seleccionar las características para realizar el clustering
features = ['anxiety_level', 'self_esteem', 'depression', 'sleep_quality', 'bullying']

# Crear el modelo KMeans con 3 clústeres
kmeans = KMeans(n_clusters=3, random_state=42)

# Calcular los clústeres y agregarlos al DataFrame
df["cluster"] = kmeans.fit_predict(df[features])

# Guardar el DataFrame actualizado en el nuevo archivo CSV
output_path = "reports/cluster_analysis_with_clusters.csv"
df.to_csv(output_path, index=False)

print(f"✅ El archivo con los clústeres fue guardado en: {output_path}")
