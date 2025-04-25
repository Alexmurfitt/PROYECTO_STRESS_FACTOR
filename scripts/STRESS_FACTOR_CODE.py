import os

# Nombre base del proyecto
project_name = "ReBoot_Stress_Project"

# Carpetas a crear
folders = [
    "data",                # Datos originales y transformados
    "notebooks",           # Análisis exploratorio y modelado
    "scripts",             # Scripts Python auxiliares
    "models",              # Modelos predictivos
    "db",                  # Scripts y backups de base de datos
    "reports",             # Informes PDF / Markdown / LaTeX
    "references",          # Libros, artículos y teorías clave
    "docker"               # Archivos para contenerización
]

# Ruta base del proyecto (en el directorio actual)
base_path = os.path.join(os.getcwd(), project_name)

# Crear las carpetas
def crear_estructura_proyecto(base_path, folders):
    if not os.path.exists(base_path):
        os.mkdir(base_path)
    for folder in folders:
        ruta = os.path.join(base_path, folder)
        os.makedirs(ruta, exist_ok=True)
        print(f"✅ Carpeta creada: {ruta}")

# Ejecutar
crear_estructura_proyecto(base_path, folders)

print("\n🎯 Estructura del proyecto creada con éxito.")
