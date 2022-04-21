import streamlit as st
import pandas as pd
import numpy as np
np.random.seed(0)
df = pd.DataFrame(np.round(np.random.randn(5, 1),3), columns=list('A'))
# Настройка заголовка и текста 
st.title("GПример фильтрации Pandas DataFrame")
#st.dataframe(df)

def df_flt(sel_val, df):
  if sel_val == 'Все':
    return df
  else:
    s1=df['A']==sel_val
    return df[s1]
# отбор с использованием selectbox
st.sidebar.title("Filter")
lst = ['Все']; lst= lst + list(df['A'].drop_duplicates().sort_values().values)
#lst= df['A'].drop_duplicates().sort_values().values
sel_val=st.sidebar.selectbox('выберите значения', lst, 0)
st.sidebar.write('Выбрано:', sel_val, type(sel_val))
st.dataframe(df_flt(sel_val, df))
# отбор с использованием multiselect
sel_val_ms =st.sidebar.multiselect('выберите значения', lst,  'Все')
st.sidebar.write('Выбрано:', sel_val_ms, type(sel_val))
st.dataframe(df_flt(sel_val_ms, df))
