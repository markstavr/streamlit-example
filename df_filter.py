import streamlit as st
import pandas as pd
import numpy as np
np.random.seed(0)
df = pd.DataFrame(np.round(np.random.randn(5, 1),3), columns=list('A'))
# Настройка заголовка и текста 
st.title("DATAFRAME FILTER")
#st.dataframe(df)

def df_flt(sel_val, df):
  if sel_val == 'Все':
    return df
  else:
    s1=df['A']==sel_val
    return df[s1]

st.sidebar.title("Filter")
lst = ['Все']; lst= lst + list(df['A'].drop_duplicates().sort_values().values)
#lst= df['A'].drop_duplicates().sort_values().values
#sel_val=st.sidebar.multiselect('выберите значения', lst,  'Все')
sel_val=st.sidebar.selectbox('выберите значения', lst,  'Все')
st.sidebar.write('Выбрано:', sel_val, type(sel_val))
#st.dataframe(df_flt(sel_val, df))
