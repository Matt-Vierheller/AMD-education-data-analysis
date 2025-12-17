from extract import load_raw_module_data
from transform import clean_patient_data, transform_module_data
from load import create_tables, load_patients, load_module_results
import pandas as pd

def run_pipeline():
    print('Loading raw module CSV files...')
    module_data = load_raw_module_data(raw_path = '/Users/mattvierheller/Desktop/Project_Portfolio/patient-education-data-pipeline/etl/data/raw')
    
    if 1 not in module_data:
        raise KeyError('module1.csv must exist and contain patient demographics(id, age, sex, va_l, va_r, disease).')
    
    print('Cleaning patients table from module 1...')
    patients_df = clean_patient_data(module_data[1])

    print('Transforming module-level data into long format...')
    modules_df = transform_module_data(module_data)

    print('Creating database tables (if it does not exists)...')
    create_tables()

    print('Loading patients into the database...')
    load_patients(patients_df)

    print('Loading module results into the database...')
    load_module_results(modules_df)

    print('ETL pipeline completed successfully!')

if __name__ == '__main__':
    run_pipeline()