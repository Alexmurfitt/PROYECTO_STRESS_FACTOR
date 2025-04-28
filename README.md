ls# 📊 ReBoot – Student Stress Factors

Análisis avanzado de los factores que influyen en el estrés estudiantil mediante ciencia de datos, teorías psicológicas, sociológicas y neurocientíficas, e interpretación de modelos de machine learning.

---

## 🧠 Objetivo del Proyecto

Identificar, explicar y predecir los niveles de estrés en estudiantes a partir de variables psicológicas, fisiológicas, ambientales, académicas y sociales, utilizando:

- 📊 Análisis exploratorio de datos (EDA)
- 🤖 Modelos predictivos avanzados
- 📈 Visualización interactiva y explicabilidad de modelos
- 🧪 Interpretación neurocientífica y sociológica del fenómeno del estrés académico

---

## 📂 Estructura del Proyecto

```
ReBoot_Stress_Project/
├── BOOKS/              # Referencias teóricas (Handbook, Stress de G. Fink, etc.)
├── data/               # Dataset principal (.csv)
├── db/                 # Scripts SQL (estructura de base de datos)
├── docker/             # Configuración para despliegue Docker
├── models/             # Modelos optimizados guardados (.pkl)
├── notebooks/          # Análisis en Jupyter Notebooks
├── references/         # Marco teórico y citas científicas
├── reports/            # Informes automáticos y análisis de clústeres
├── scripts/            # Código fuente Python
├── streamlit_app.py    # Aplicación Streamlit interactiva
├── requirements.txt    # Lista de dependencias
└── README.md           # Este documento
```

---

## 📈 Tecnologías Utilizadas

- **Lenguaje**: Python 3.12

- **Librerías principales**:
  - Pandas, NumPy
  - Seaborn, Matplotlib, Plotly
  - Scikit-learn, XGBoost, LightGBM
  - SHAP, LIME (explicabilidad)
  - Statsmodels (regresión OLS)
  - Streamlit (visualización web)

- **Control de versiones**: Git + GitHub

---

## 🧪 Análisis Realizados

### 1. Exploración de Datos (EDA)
- 📊 Regresión lineal OLS (`R² = 0.749`)
- 🚨 Identificación de 239 estudiantes en riesgo crítico
- 🌳 Árbol de decisión básico (precisión: 89%)
- 🔎 Interpretación de variables clave mediante SHAP

### 2. Optimización de Modelos
- 🌲 Random Forest optimizado con GridSearchCV
- 🔧 Parámetros óptimos: `max_depth=15`, `min_samples_split=2`
- ✅ Precisión validada: 88.86%

### 3. Modelado Predictivo y Explicabilidad
- 📊 Comparativa entre: Decision Tree, Random Forest, SVM, XGBoost, LightGBM
- 🔥 Explicaciones avanzadas:
  - SHAP values (importancia global)
  - LIME (explicación local de predicciones)
- 🎯 Precisión media: 89–90%

### 4. Análisis de Correlaciones
- 🔥 Heatmap de correlaciones (coeficiente de Pearson)
- 📈 Variables más relacionadas con el estrés:
  - Ansiedad (+0.74)
  - Bullying (+0.75)
  - Autoestima (–0.76)
  - Calidad de sueño (–0.75)

### 5. Visualización Interactiva
- 🌐 Aplicación en Streamlit con:
  - Filtros dinámicos por ansiedad, autoestima, calidad de sueño y clústeres
  - Predicción personalizada explicada con LIME
  - Gráficos avanzados: violin plots, histogramas, scatterplots, SHAP summary plots

---

## 🧬 Variables Clave del Dataset

| Factor        | Variables principales |
|---------------|------------------------|
| Psicológico   | anxiety_level, self_esteem, depression |
| Fisiológico   | sleep_quality, blood_pressure, headache |
| Académico     | academic_performance, study_load, future_career_concerns |
| Social        | bullying, peer_pressure, social_support |
| Resultado     | stress_level (1 = bajo, 2 = medio, 3 = alto) |

---

## 🔬 Fundamento Científico

Basado en los modelos teóricos y neurobiológicos más reconocidos:

- **Modelo Transaccional del Estrés** (Lazarus y Folkman, 1984):  
  ➔ La percepción de amenaza y recursos personales define la respuesta de estrés.

- **Teoría Cognitiva de la Depresión** (Aaron Beck):  
  ➔ Pensamientos negativos y baja autoestima como factores de vulnerabilidad.

- **Psicología Positiva y Resiliencia** (Seligman, 2000):  
  ➔ La autoestima, el apoyo social y la percepción de competencia reducen la vulnerabilidad al estrés.

- **Neurociencia del Estrés**:
  - **Sapolsky (2004)**: Activación del eje HPA; daño en hipocampo, amígdala y corteza prefrontal.
  - **McEwen (1998)**: Concepto de carga alostática (daño acumulado por estrés crónico).
  - **Lisa Feldman Barrett (2017)**: Construcción cerebral de las emociones y reconfiguración por estrés.

- **Sociología del Estrés**:
  - **Pearlin (1981)**: Estrés derivado de condiciones sociales adversas (pobreza, falta de apoyo).
  - **Durkheim, OMS**: El apoyo social protege frente al malestar psicológico.
  - **Giddens (1991)**: Factores cruzados (género, clase social) median la experiencia de estrés.

**Referencias científicas utilizadas**:
- Gonzaga, L. R. V., & Lovato, L. (2022). *Handbook of Stress and Academic Anxiety*. Springer.
- Fink, G. (Ed.). (2016). *Stress: Concepts, Cognition, Emotion, and Behavior*. Academic Press.
- Lazarus, R. & Folkman, S. (1984). *Stress, Appraisal, and Coping*.
- Sapolsky, R. (2004). *Why Zebras Don't Get Ulcers*.
- McEwen, B. (1998). *Protective and damaging effects of stress mediators*.
- Beck, A. T. (1976). *Cognitive Therapy and the Emotional Disorders*.
- Seligman, M. (2000). *Positive Psychology*.
- OMS, WHO Mental Health Atlas.
- Giddens, A. (1991). *Modernity and Self-Identity*.

🔎 Ejemplos relevantes:
- "El estrés sostenido activa el eje HPA, afectando la función prefrontal." (Fink, cap. 1)
- "El apoyo social percibido modula significativamente el impacto del estrés académico." (Gonzaga & Lovato, cap. 2)
- "Los estresores tienen distribución social, no son aleatorios." (Pearlin, 1981)

---

## ▶️ Ejecución de la Aplicación Streamlit

Para lanzar la app interactiva:
streamlit run streamlit_app.py

