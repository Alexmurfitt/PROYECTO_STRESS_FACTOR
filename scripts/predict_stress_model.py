from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
import pandas as pd
import streamlit as st

# Cargar los datos
df = pd.read_csv("reports/cluster_analysis_with_clusters.csv")

# Definir las variables predictoras (X) y el objetivo (y)
features = ['anxiety_level', 'self_esteem', 'depression', 'sleep_quality', 'bullying', 'social_support']
X = df[features]
y = df['stress_level']

# Dividir los datos en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear y entrenar el modelo de regresión logística
model = LogisticRegression(max_iter=1000, random_state=42)
model.fit(X_train, y_train)

# Hacer predicciones
y_pred = model.predict(X_test)

# Evaluar el modelo
accuracy = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)

# Mostrar los resultados en Streamlit
st.markdown(f"### Precisión del modelo: {accuracy * 100:.2f}%")
st.write("### Matriz de confusión:", cm)
