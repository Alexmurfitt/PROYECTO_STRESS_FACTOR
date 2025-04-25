import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from lime.lime_tabular import LimeTabularExplainer
import shap

# Cargar el archivo con los clústeres
df = pd.read_csv("/home/reboot-student/code/labs/0_ReBoot_Stress_Project/reports/cluster_analysis_with_clusters.csv")

# Título de la aplicación
st.title("🧠 ReBoot – Análisis Exploratorio del Estrés Estudiantil")

# Estadísticas descriptivas
st.markdown(f"### Total de estudiantes en el dataset: {len(df)}")
st.markdown(f"### Promedio de ansiedad: {df['anxiety_level'].mean():.2f}")
st.markdown(f"### Estudiantes con historial de salud mental: {df['mental_health_history'].sum()}")

# Psicológico: self_esteem por debajo del promedio
avg_self_esteem = df['self_esteem'].mean()
students_below_avg = len(df[df['self_esteem'] < avg_self_esteem])
st.markdown(f"### Estudiantes con `self_esteem` por debajo del promedio: {students_below_avg}")

# Psicológico: porcentaje de depresión por encima del umbral clínico
threshold_depression = 15  # Definir el umbral clínico
high_depression = len(df[df['depression'] > threshold_depression])
depression_percentage = (high_depression / len(df)) * 100
st.markdown(f"### Porcentaje de estudiantes con depresión más allá del umbral clínico: {depression_percentage:.2f}%")

# Fisiológico: estudiantes con frecuencia de dolor de cabeza ≥ 4
headache_freq = len(df[df['headache'] >= 4])
st.markdown(f"### Estudiantes con dolor de cabeza frecuente (≥ 4): {headache_freq}")

# Fisiológico: media de la presión arterial
mean_blood_pressure = df['blood_pressure'].mean()
st.markdown(f"### Media de la presión arterial: {mean_blood_pressure:.2f}")

# Fisiológico: estudiantes con calidad de sueño 1 o 2
poor_sleep_quality = len(df[df['sleep_quality'] <= 2])
st.markdown(f"### Estudiantes con calidad de sueño baja (1 o 2): {poor_sleep_quality}")

# Factores ambientales: estudiantes con ruido nivel ≥ 4
high_noise = len(df[df['noise_level'] >= 4])
st.markdown(f"### Estudiantes con nivel de ruido alto (≥ 4): {high_noise}")

# Factores académicos: estudiantes con rendimiento académico bajo (academic_performance < 3)
low_academic_performance = len(df[df['academic_performance'] < 3])
st.markdown(f"### Estudiantes con rendimiento académico bajo (< 3): {low_academic_performance}")

# Factores sociales: estudiantes con apoyo social alto (social_support ≥ 4)
high_social_support = len(df[df['social_support'] >= 4])
st.markdown(f"### Estudiantes con apoyo social alto (≥ 4): {high_social_support}")

# Mostrar tabla de estudiantes filtrados
st.dataframe(df)

# Preparar los datos para entrenamiento del modelo
X = df[['anxiety_level', 'self_esteem', 'depression', 'sleep_quality', 'bullying']]
y = df['stress_level']

# Dividir los datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Modelos de clasificación
models = {
    "Decision Tree": DecisionTreeClassifier(),
    "Random Forest": RandomForestClassifier(),
    "SVM": SVC(probability=True)  # Cambiar aquí
}

# Entrenar y evaluar los modelos
for name, model in models.items():
    model.fit(X_train.values, y_train)  # Usar .values para convertir a matriz
    y_pred = model.predict(X_test.values)  # Usar .values para convertir a matriz
    accuracy = accuracy_score(y_test, y_pred)
    print(f'{name} accuracy: {accuracy * 100:.2f}%')

    # Explicabilidad con SHAP (si el modelo es Random Forest)
    if name == "Random Forest":
        explainer = shap.TreeExplainer(model)
        shap_values = explainer.shap_values(X_test)
        
        # Verificar si tenemos valores SHAP para cada clase
        if isinstance(shap_values, list):  # Si el modelo es multiclase
            for i in range(len(shap_values)):
                st.write(f"### Visualización SHAP para la clase {i}")
                shap.summary_plot(shap_values[i], X_test, plot_type="bar")  # Visualización por clase
        else:  # Si es un clasificador binario o regresión
            st.write(f"### Visualización SHAP para la clase única")
            # Si estás usando plot_type="bar" y quieres guardar el gráfico:
            shap.summary_plot(shap_values, X_test, plot_type="bar", show=False)
            plt.savefig("shap_summary_plot.png")  # Guarda el gráfico como imagen


    # Explicabilidad con LIME
    explainer_lime = LimeTabularExplainer(
        training_data=X_train.values,
        training_labels=y_train.values,
        mode="classification",
        feature_names=X_train.columns,
        class_names=["Low", "Medium", "High"],
        discretize_continuous=True
    )
    instance = X_test.iloc[0].values.reshape(1, -1)
    explanation = explainer_lime.explain_instance(instance[0], model.predict_proba)

    # Visualización de LIME en Streamlit
    explanation_html = explanation.as_html()
    st.components.v1.html(explanation_html, height=500)

# Gráfico interactivo 2D (Ansiedad vs Autoestima)
fig = px.scatter(
    df,
    x="anxiety_level",
    y="self_esteem",
    color=df["stress_level"].astype(str),
    title="Ansiedad vs Autoestima",
    labels={"stress_level": "Estrés"}
)
st.plotly_chart(fig, key="scatter_anxiety_vs_self_esteem")

# Gráfico de violín (distribución de ansiedad por clúster)
fig_violin = px.violin(
    df, y="anxiety_level", color="cluster", box=True, points="all",
    title="Distribución de Ansiedad por Clúster"
)
st.plotly_chart(fig_violin, key="violin_anxiety_by_cluster")

# Histograma de sueño
fig_hist = px.histogram(
    df, x="sleep_quality", color="cluster",
    title="Histograma de Calidad de Sueño por Clúster",
    labels={"sleep_quality": "Calidad de Sueño"}
)
st.plotly_chart(fig_hist, key="histogram_sleep_quality_by_cluster")

# Correlación entre variables
corr = df[['anxiety_level', 'self_esteem', 'depression', 'sleep_quality', 'bullying']].corr()
fig_corr = plt.figure(figsize=(10, 6))
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
st.pyplot(fig_corr)

# 1. Gráfico de distribución de clústeres
df_cluster_dist = df['cluster'].value_counts().reset_index()
df_cluster_dist.columns = ['cluster', 'count']  # Renombrar las columnas a 'cluster' y 'count'

fig_cluster_dist = px.bar(
    df_cluster_dist, 
    x='cluster', 
    y='count', 
    labels={'cluster': 'Clúster', 'count': 'Número de estudiantes'},
    title="Distribución de Estudiantes por Clúster"
)
st.plotly_chart(fig_cluster_dist, key="bar_cluster_distribution")


# 2. Gráfico de Predicciones del Modelo
fig_predictions = px.scatter(
    df, x="anxiety_level", y="self_esteem", color="cluster", size="stress_level", hover_data=["stress_level"],
    title="Predicciones del Modelo de Estrés", labels={"stress_level": "Nivel de Estrés"})
st.plotly_chart(fig_predictions, key="scatter_model_predictions")

# 3. Filtros interactivos (rango de ansiedad)
anxiety_range = st.slider("Selecciona el rango de ansiedad", 1, 20, (1, 20))
df_filtered = df[df['anxiety_level'].between(anxiety_range[0], anxiety_range[1])]

# Filtro para seleccionar un clúster
cluster_select = st.selectbox("Selecciona un clúster", df['cluster'].unique())
df_filtered_cluster = df_filtered[df_filtered['cluster'] == cluster_select]

# Mostrar los datos filtrados
st.markdown(f"### {len(df_filtered_cluster)} estudiantes en el filtro seleccionado.")
st.dataframe(df_filtered_cluster)

# 4. Gráfico de violín para mostrar la distribución de ansiedad en cada clúster
fig_violin_cluster = px.violin(
    df_filtered_cluster, y="anxiety_level", color="cluster", box=True, points="all",
    title="Distribución de Ansiedad por Clúster", labels={"anxiety_level": "Nivel de Ansiedad"})
st.plotly_chart(fig_violin_cluster, key="violin_filtered_anxiety_by_cluster")

# Filtros adicionales
self_esteem_filter = st.slider("Selecciona el rango de autoestima", 1, 30, (1, 30))
depression_filter = st.slider("Selecciona el rango de depresión", 1, 20, (1, 20))
sleep_quality_filter = st.slider("Selecciona el rango de calidad de sueño", 1, 5, (1, 5))

# Filtrar el DataFrame con los filtros seleccionados
df_filtered = df[df['self_esteem'].between(self_esteem_filter[0], self_esteem_filter[1])]
df_filtered = df_filtered[df_filtered['depression'].between(depression_filter[0], depression_filter[1])]
df_filtered = df_filtered[df_filtered['sleep_quality'].between(sleep_quality_filter[0], sleep_quality_filter[1])]

# Mostrar los datos filtrados
st.dataframe(df_filtered)

# Gráfico de violín para visualizar la distribución de ansiedad en función de las variables seleccionadas
fig_violin = px.violin(
    df_filtered, y="anxiety_level", color="cluster", box=True, points="all",
    title="Distribución de Ansiedad por Clúster (Filtrado)",
    labels={"anxiety_level": "Nivel de Ansiedad"}
)
st.plotly_chart(fig_violin)

# Visualizar los resultados de predicción para un estudiante seleccionado
selected_student = st.selectbox("Selecciona un estudiante", df_filtered_cluster.index)
student_data = df_filtered_cluster.loc[selected_student]
st.write(f"Predicción para el estudiante seleccionado: {student_data[['anxiety_level', 'self_esteem', 'depression', 'sleep_quality', 'bullying']]}")

# Si deseas predecir el estrés del estudiante seleccionado
predicted_stress = model.predict(student_data[['anxiety_level', 'self_esteem', 'depression', 'sleep_quality', 'bullying']].values.reshape(1, -1))
st.write(f"Predicción de nivel de estrés: {predicted_stress[0]}")
