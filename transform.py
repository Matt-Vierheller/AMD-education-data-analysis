import pandas as pd
def clean_patient_data(df):
    '''Clean patient-level columns from module 1 (demographics).'''
    df = df.copy()
    df.columns = df.columns.str.strip().str.lower()

    rename_map = {
        'patient_id':'patient_id',
        'Age':'age',
        'va_l':'va_l',
        'va_r':'va_r',
        'feedback':'feedback',
        'feedback_score':'feedback_score'
    }
    df = df.rename(columns = rename_map)

    #normalize sex
    if 'sex' in df.columns:
        df['sex'] = df['sex'].astype(str).str.upper()

    #convert VA to numerical data
    #for col in ['va_l','va_r']:
    #    if col in df.columns:
    #        df[col] = pd.to_numeric(df[col], errors = 'coerce')
        #confirm age is numeric
    if 'age' in df.columns:
        df['age'] = pd.to_numeric(df['age'], errors = 'coerce').astype('Int64')
    
    if 'disease' not in df.columns:
        df['disease'] = None

    #create column order
    keep_cols = ['patient_id', 'age','sex','va_l','va_r','disease']
    existing = [c for c in keep_cols if c in df.columns]
    return df[existing]

def transform_module_data(module_dict):
    '''Turn Dict of module DataFrames into a single long table.'''
    frames = []
    expected_cols = ['id','pre_score','post_score','feedback','feedback_score','module_number']
    for module_num, df in module_dict.items():
        df = df.copy()
        #normalize column names
        df.columns = df.columns.str.strip().str.lower()
        if 'id' in df.columns:
            df = df.rename(columns = {'id':'patient_id'})
        elif 'patient_id' not in df.columns:
            raise KeyError(f'Module {module_num} missing patient id column')
        for col in ['pre_score','post_score','feedback','feedback_score']:
            if col not in df.columns:
                df[col] = pd.NA
        
        df['module_number'] = module_num
        df['completed'] = df['post_score'].notna().astype(int)

        frames.append(df[['patient_id','module_number','pre_score','post_score','feedback', 'feedback_score','completed']])
    result = pd.concat(frames, ignore_index = True)
    return result
