import pandas as pd
import mysql.connector
from mysql.connector import Error

# Configura tu conexión MySQL
config = {
    'host': 'localhost',
    'user': 'root',
    'password': '0000',  # 👈 Reemplaza con tu contraseña real
    'database': 'reboot_stress_factors'
}

# Ruta del CSV
csv_path = 'data/ReBoot_Student_Stress_Factors.csv'

# Cargar CSV en DataFrame
df = pd.read_csv(csv_path)

# Reemplazar valores numéricos de blood_pressure por etiquetas
blood_pressure_map = {1: 'Low', 2: 'Normal', 3: 'High'}
df['blood_pressure'] = df['blood_pressure'].map(blood_pressure_map)

conn = None

# Conectar y exportar
try:
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    insert_query = """
    INSERT INTO student_stress_data (
        anxiety_level, self_esteem, depression, mental_health_history,
        headache, blood_pressure, sleep_quality, breathing_problem,
        noise_level, living_conditions, safety, basic_needs,
        academic_performance, study_load, teacher_student_relationship, future_career_concerns,
        social_support, peer_pressure, extracurricular_activities, bullying,
        stress_level
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    for _, row in df.iterrows():
        values = (
    row['anxiety_level'],
    row['self_esteem'],
    row['depression'],
    row['mental_health_history'],
    row['headache'],
    row['blood_pressure'],
    row['sleep_quality'],
    row['breathing_problem'],
    row['noise_level'],
    row['living_conditions'],
    row['safety'],
    row['basic_needs'],
    row['academic_performance'],
    row['study_load'],
    row['teacher_student_relationship'],
    row['future_career_concerns'],
    row['social_support'],
    row['peer_pressure'],
    row['extracurricular_activities'],
    row['bullying'],
    row['stress_level']  # o 'str_level', según tu CSV
)

        cursor.execute(insert_query, values)

    conn.commit()
    print(f"✅ {cursor.rowcount} registros insertados correctamente.")
except Error as e:
    print("❌ Error al conectar o insertar en MySQL:", e)
finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
