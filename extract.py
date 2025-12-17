import pandas as pd
import glob
import os

def load_raw_module_data(raw_path = '/Users/mattvierheller/Desktop/Project_Portfolio/patient-education-data-pipeline/etl/data/raw'):
    '''Load all module CSVs named module1-module7.csv into dict.'''
    pattern = os.path.join(raw_path, 'module*.csv')
    csv_files = glob.glob(pattern)
    module_data = {}

    if not csv_files:
        raise FileNotFoundError(f'No CSV files found with pattern: {pattern}')
    for file in csv_files:
        base = os.path.basename(file)
        #extract module number
        num_part = base.replace('module','').replace('.csv','')
        try:
            module_num = int(num_part)

        except ValueError:
            #skip files that do not match pattern
            continue

        df = pd.read_csv(file)
        df['module_number'] = module_num
        module_data[module_num] = df
    return module_data

