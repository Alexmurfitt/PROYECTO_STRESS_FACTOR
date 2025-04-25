# Makefile - Proyecto ReBoot Student Stress Factors
# Compatible con el entorno STRESSFACTOR

ENV_DIR = /home/reboot-student/STRESSFACTOR
PYTHON = $(ENV_DIR)/bin/python
PIP = $(ENV_DIR)/bin/pip
JUPYTER = $(ENV_DIR)/bin/jupyter
STREAMLIT = $(ENV_DIR)/bin/streamlit

install:
	$(PIP) install -r requirements.txt

start-jupyter:
	$(JUPYTER) lab

profile-data:
	$(PYTHON) scripts/profile_data.py

run-streamlit:
	$(STREAMLIT) run scripts/dashboard.py

clean:
	find . -type d -name "__pycache__" -exec rm -r {} +
