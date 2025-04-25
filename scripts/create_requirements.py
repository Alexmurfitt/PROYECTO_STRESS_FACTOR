# scripts/create_requirements.py

requirements = """
pandas
numpy
scikit-learn
statsmodels
seaborn
matplotlib
plotly
jupyterlab
notebook
pgmpy
shap
lime
pycaret
ydata-profiling
streamlit
mysql-connector-python
python-dotenv
"""

with open("requirements.txt", "w") as f:
    f.write(requirements.strip())

print("✅ Archivo requirements.txt creado en el directorio actual.")

