# 📊 ReBoot – Student Stress Factors

Este proyecto analiza en profundidad los factores que influyen en el estrés de estudiantes a partir de un dataset multidimensional, integrando ciencia de datos, teorías psicológicas, sociológicas y neurocientíficas, y modelos explicativos basados en machine learning. 

---

## 🧠 Objetivo del Proyecto
Identificar, explicar y predecir los niveles de estrés en estudiantes a partir de variables psicológicas, fisiológicas, ambientales, académicas y sociales, utilizando análisis exploratorio, modelos predictivos y visualización interactiva.



## 📂 Estructura del Proyecto
```
ReBoot_Stress_Project/
├── BOOKS/                         # Referencias teóricas (incluye libro de Fink)
├── data/                          # Dataset principal en CSV
├── db/                            # Scripts SQL (estructura de base de datos)
├── docker/                        # Configuración Docker (opcional)
├── models/                        # Modelos optimizados guardados (pkl)
├── notebooks/                     # Jupyter Notebooks con todo el análisis
├── references/                    # Marco teórico y notas científicas
├── reports/                       # Reportes y exportaciones de clústeres
├── scripts/                       # Código fuente Python del análisis
├── streamlit_app.py               # Aplicación interactiva
├── requirements.txt              # Dependencias del proyecto
└── README.md                     # Este documento
```

## 📈 Tecnologías Utilizadas
- Python 3.12
- Pandas, NumPy, Seaborn, Matplotlib, Plotly
- Scikit-learn, XGBoost, LightGBM
- SHAP, LIME (explicabilidad de modelos)
- Streamlit (visualización interactiva)
- Statsmodels (regresión lineal OLS)
- Git + GitHub

---

## 🧪 Análisis Realizados

### 1. Exploración de Datos (`EDA_ReBoot_Stress.ipynb`)
- Regresión lineal OLS (R² = 0.749)
- Árbol de decisión (89% de precisión)
- Valores SHAP interpretando cada variable
- Identificación de 239 estudiantes en riesgo crítico

### 2. Optimización de Modelos (`model_optimization.ipynb`)
- Random Forest con `GridSearchCV`
- Mejores parámetros: `max_depth=15`, `min_samples_split=2`
- Precisión validada: **88.86%**

### 3. Modelado Predictivo y Explicabilidad (`models_predictive_analysis.ipynb`)
- Comparativa entre: Decision Tree, Random Forest, SVM, XGBoost, LightGBM
- Modelos explicados con SHAP y LIME
- Precisión promedio: **89-90%**

### 4. Análisis de Correlación (`analyze_correlation.py`)
- Heatmap con Pearson correlations
- Variables más correlacionadas con el estrés: ansiedad (+0.74), bullying (+0.75), autoestima (–0.76), sueño (–0.75)

### 5. Visualización Interactiva (`streamlit_app.py`)
- Filtros por ansiedad, autoestima, sueño, clúster
- Predicción por estudiante con interpretación LIME
- Gráficos interactivos: violines, histogramas, scatter, SHAP

## 🧬 Variables Clave del Dataset
- Psicológicas: `anxiety_level`, `self_esteem`, `depression`
- Fisiológicas: `sleep_quality`, `blood_pressure`, `headache`
- Académicas: `academic_performance`, `study_load`, `future_career_concerns`
- Sociales: `bullying`, `peer_pressure`, `social_support`
- Resultado: `stress_level` (1 = bajo, 2 = medio, 3 = alto)



## 🔬 Fundamento Científico
Este proyecto está basado en teorías avanzadas de psicología, neurociencia y sociología, y en el libro:

**George Fink (Ed.). (2016). _Stress: Concepts, Cognition, Emotion, and Behavior_. Academic Press.**

### Citas destacadas del libro:
- "El estrés sostenido activa el eje HPA... disfunción prefrontal." (Fink, cap. 1)
- "Los factores sociales influyen en la exposición a estresores..." (Avison, cap. 10)
- "Los estresores tienen distribución social, no son aleatorios." (Pearlin)
- "Coping: conjunto de respuestas cognitivas y conductuales..." (cap. sobre coping)


## ▶️ Ejecución de la app Streamlit

streamlit run streamlit_app.py
```


