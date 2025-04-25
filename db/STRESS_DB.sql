-- Crear base de datos
DROP DATABASE IF EXISTS reboot_stress_factors;
CREATE DATABASE reboot_stress_factors;
USE reboot_stress_factors;

-- Crear tabla principal
CREATE TABLE student_stress_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    
    -- PSICOLÓGICO
    anxiety_level TINYINT,         -- 1–20
    self_esteem TINYINT,           -- 1–30
    depression TINYINT,            -- 1–20
    mental_health_history BOOLEAN, -- 0 = No, 1 = Sí

    -- FISIOLÓGICO
    headache TINYINT,              -- 0–5
    blood_pressure ENUM('Low', 'Normal', 'High'),
    sleep_quality TINYINT,         -- 1–5
    breathing_problem TINYINT,     -- 0–5

    -- AMBIENTAL
    noise_level TINYINT,           -- 1–5
    living_conditions TINYINT,     -- 1–5
    safety TINYINT,                -- 1–5
    basic_needs TINYINT,           -- 1–5

    -- ACADÉMICO
    academic_performance TINYINT,  -- 1–5
    study_load INT,                -- Horas semanales
    teacher_student_relationship TINYINT,  -- 1–5
    future_career_concerns TINYINT,        -- 1–5

    -- SOCIAL
    social_support TINYINT,        -- 1–5
    peer_pressure TINYINT,         -- 1–5
    extracurricular_activities TINYINT,     -- 0–5
    bullying TINYINT,              -- 0–5

    -- RESULTADO
    stress_level TINYINT           -- 1 = Bajo, 2 = Medio, 3 = Alto
);
