import streamlit as st
import sqlite3
import plotly.express as px
import matplotlib.pyplot as plt
import pandas as pd
import warnings
from wordcloud import WordCloud
warnings.filterwarnings('ignore')

db_path = 'data/database/patient_education.db'

@st.cache_data
def load_data():
    with sqlite3.connect(db_path) as conn:
        patients = pd.read_sql_query('SELECT * FROM patients;',conn)
        modules = pd.read_sql_query('SELECT * FROM module_results;', conn)
    merged = modules.merge(patients, on = 'patient_id', how = 'left')
    merged['delta'] = merged['post_score'] - merged['pre_score']
    return patients, modules, merged
patients, modules, merged = load_data()

#side bars

st.sidebar.header('Filters')
selected_modules = st.sidebar.selectbox('Select Module', sorted(modules['module_number'].dropna().unique()))
selected_sex = st.sidebar.multiselect('Select Sex', options = patients['sex'].dropna().unique(), 
                                      default= list(patients['sex'].dropna().unique()))
selected_disease = st.sidebar.multiselect('Select Disease', options = patients['disease'].dropna().unique(),
                                          default = list(patients['disease'].dropna().unique()))

filtered = merged[
    (merged['module_number'] == selected_modules) &
    (merged['sex'].isin(selected_sex)) &
    (merged['disease'].isin(selected_disease))
]

#visualizations
st.subheader('Average Pre vs Post Quiz Scores')
avg_scores = filtered[['pre_score','post_score']].mean()
fig1 = px.bar(x=['Pre Score', 'Post Score'], y = avg_scores, title = 'Average Scores', color = ['Pre Score','Post Score'], 
              color_discrete_sequence=['blue','orange'], labels = {'x':'Score Type', 'y':'AVerage'})
st.plotly_chart(fig1)

st.subheader('Score Improvement Distribution')
fig2 = px.histogram(filtered, x = 'delta', nbins = 5, title = 'Score improvement (post - pre)')
st.plotly_chart(fig2)

st.subheader('Feedback Analysis')
feedback_by_sex = filtered.groupby('sex')['feedback_score'].mean().reset_index()
fig3 = px.bar(feedback_by_sex, x = 'sex', y = 'feedback_score', color = 'sex',
               color_discrete_sequence = ['blue','orange'],
               title = 'Average feedback by Sex')
st.plotly_chart(fig3)

st.subheader('Feedback Word Cloud')
feedback_text = ' '.join(filtered['feedback'].dropna())
if feedback_text:
    wordcloud = WordCloud(width = 800, height = 400, background_color = 'white').generate(feedback_text)
    plt.imshow(wordcloud, interpolation = 'bilinear')
    plt.axis('off')
    st.pyplot(plt)
else:
    st.write('no feedback avalable for selected filters.')


#display filtered data
st.subheader('Filtered Data Table')
st.dataframe(filtered)
