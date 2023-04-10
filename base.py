import pandas as pd
import altair as alt
import streamlit as st

df = pd.read_excel('/content/drive/MyDrive/Relatorios_20231/desempenho/77.10.04.xlsx')
df = df[df['PROVA1'].notna()]
df["Curso"] =  df['CODTURMA'].str.split('-').str[0]
DictCurso = {'EPR':'Engenharia de Produção',
             'CEC':'Ciências Econômicas',
             'DTO':'Direito',
       'ADM':'Administração',
        'ECO':'Engenharia de Computação'
}
df['Curso'] = df['Curso'].apply(lambda x: DictCurso [x])

df["Turno"] =  df['CODTURMA'].str.split('-').str[2]
DictTurno = {'N':'Noturno',
             'D':'Diurno',
             'RER':'RER'
}
df['Turno'] = df['Turno'].apply(lambda x: DictTurno [x])

#Gráfico 1
#linhas
linhan = pd.DataFrame({'y': [6, 6], 'x':[0.0, 1.1]})
linhaf = pd.DataFrame({'y': [0, 10], 'x':[0.75, 0.75]})
linha_horizontal = alt.Chart(linhan).mark_line(color = 'red').encode(
    x= alt.Y('x',scale=alt.Scale(domain=(0, 1.0),clamp=False)),
    y= alt.Y('y',scale=alt.Scale(domain=(0, 10),clamp=False)))
linha_vertical = alt.Chart(linhaf).mark_line(color = 'red').encode(
    x= alt.Y('x',scale=alt.Scale(domain=(0, 1.0),clamp=False)),
    y= alt.Y('y',scale=alt.Scale(domain=(0, 10),clamp=False)))


