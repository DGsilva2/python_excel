import streamlit as st
from pathlib import Path
import pandas as pd
 
pasta_datasets = Path(__file__).parent / 'datasets'
caminho_vendas = pasta_datasets / 'vendas.csv'
df_vendas = pd.read_csv(caminho_vendas, sep=';', decimal=',')

st.dataframe(df_vendas)
