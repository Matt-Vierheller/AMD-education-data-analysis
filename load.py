import sqlite3
import pandas as pd
import os

database_path = 'data/database/patient_education.db'

def create_tables(path = database_path):
    os.makedirs(os.path.dirname(path), exist_ok = True)
    conn = sqlite3.connect(path)
    cur = conn.cursor()

    cur.execute('''
                CREATE TABLE IF NOT EXISTS patients(
                patient_id TEXT PRIMARY KEY,
                age INT,
                sex TEXT,
                va_l REAL,
                va_r REAL,
                disease TEXT
                );
                ''')
    cur.execute('''
                CREATE TABLE IF NOT EXISTS module_results(
                result_id INTEGER PRIMARY KEY AUTOINCREMENT,
                patient_id TEXT,
                module_number INT,
                pre_score REAL,
                post_score REAL,
                feedback TEXT,
                feedback_score REAL,
                completed INTEGER,
                FOREIGN KEY(patient_id) REFERENCES patients(patient_id)
                );
                ''')

    conn.commit()
    conn.close()

def load_patients(df, path = database_path):
    conn = sqlite3.connect(path)
    #replace patients table with new data
    df.to_sql('patients', conn, if_exists = 'append', index = False)
    conn.close()

def load_module_results(df, path = database_path):
    conn = sqlite3.connect(path)
    df.to_sql('module_results', conn, if_exists = 'append', index = False)
    conn.close()
