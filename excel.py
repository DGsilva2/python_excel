import pandas as pd 
import matplotlib.pyplot as plt

df = pd.DataFrame()
#criando a partir de lista
data = [1,2,3,4]
df = pd.DataFrame(data)

#criando a partir de listas de listas
rows = [[1,2],
        [3,4],
        [5,6]]
df = pd.DataFrame(rows)

#criando a partir de dicionario
dict_data = {'nome':['douglas', 'fabiano', 'rayan'], 
             'sobrenome':['silva', 'araujo', 'david']}

df = pd.DataFrame(dict_data)
 
#criado a partir de uma lista de dicionario
list_dicts =[{'nome':'douglas', 'sobrenome': 'silva'},
              {'nome':'rayan', 'sobrenome': 'david'},
              {'nome':'fabiano', 'sobrenome': 'araujo'}]
df = pd.DataFrame(list_dicts)

#ESTILIZANDO PLANILHA 
import numpy as np 

df_tempo = pd.DataFrame(np.random.rand(10,2)*5,
                        index=pd.date_range(start='2023-01-01', periods=10),
                        columns=['PORTO ALEGRE', 'SAO PAULO'])

df_tempo.style.format(decimal=',', precision=3) #colocando virgula

df_tempo.style.format_index(str.upper, axis=1)

#dando titulo a planilha 
df_tempo.style.set_caption("condiçoes de tempo")

#adicionando gradiente (formatação condicional)
df_tempo.style.background_gradient(axis=None, vmin=1, vmax=5, cmap='YlGnBu')

def condicao_chuva(v):
    if v > 2.75:
        return 'chuva forte'
    elif v < 1:
        return 'seco'
    else:
        return 'chuvisco'
    
df_tempo.style.format(condicao_chuva)

def embeleza(style):
    style.format(condicao_chuva)
    style.background_gradient(axis=None, vmin=1, vmax=5, cmap='YlGnBu')
    return style

df_tempo.style.pipe(embeleza)

