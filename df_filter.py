import streamlit as st
import pandas as pd
import numpy as np
np.random.seed(0)
df = pd.DataFrame(np.round(np.random.randn(5, 1),3), columns=list('A'))
# Настройка заголовка и текста 
st.title("Пример фильтрации Pandas DataFrame")
# отбор с использованием selectbox
def df_flt(sel_val, df):
  if sel_val == 'Все':
    return df
  else:
    s1=df['A']==sel_val
    return df[s1]
st.sidebar.title("Filter selectbox")
lst = ['Все']; lst= lst + list(df['A'].drop_duplicates().sort_values().values)
sel_val=st.sidebar.selectbox('выберите значения', lst, 0)
st.sidebar.write('Выбрано:', sel_val)
st.caption("DataFrame Filter selectbox")
st.dataframe(df_flt(sel_val, df))
# отбор с использованием multiselect
st.sidebar.title("Filter multiselect")
sel_val_ms =st.sidebar.multiselect('выберите значения', lst,  'Все')
st.sidebar.write('Выбрано:', sel_val_ms)
def df_flt_ms(sel_val_lst, df):
  if 'Все' in sel_val_lst or len(sel_val_lst)==0:
    return df
  else:
    s1=df['A'].isin(sel_val_lst)
    return df[s1]
st.caption("DataFrame Filter multiselect")
st.dataframe(df_flt_ms(sel_val_ms, df))
