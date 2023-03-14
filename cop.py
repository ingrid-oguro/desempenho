import pandas as pd
import numpy as np
import streamlit as st
import altair as alt
import pip
pip.main(["install", "openpyxl"])

base = pd.read_excel('/df_dgeral.xlsx')
base_d = pd.read_excel('/disciplina.xlsx')

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

curso = sorted(base.COMPLEMENTO.unique())
curso_selecionado = st.selectbox('Graduação:',curso)
df = base.query('COMPLEMENTO == @curso_selecionado	 ')

g1 = alt.Chart(df).mark_circle(size=100).encode(
        alt.X('Percentual de Frequencia',scale=alt.Scale(zero=False),axis=alt.Axis(format='%', title='Frequência') ),
        alt.Y('Média Final',scale=alt.Scale(zero=False) ,axis=alt.Axis(title='Nota', orient = "left") ),
        tooltip = ['NOME','RA'] ).interactive().properties(width=900,height=400)
#st.altair_chart(g1, use_container_width=True)
st.altair_chart(linha_horizontal + linha_vertical + g1, use_container_width=True)
with st.expander("Ver base"):
    st.dataframe(df.style.format({"CODPERLET": "{:.0f}"}))

#Gráfico 2
curso2 = sorted(base.COMPLEMENTO.unique())
curso_selecionado2 = st.selectbox('Graduação :',curso2)
df2 = base_d.query('COMPLEMENTO == @curso_selecionado2	 ')

aluno = sorted(df2.NOME.unique())
aluno_selecionado = st.selectbox('Aluno :',aluno)
df3 = df2.query('NOME == @aluno_selecionado')

g2 = alt.Chart(df3).mark_bar().encode(
        y=alt.Y('Média Final'),
        x=alt.X('DISCIPLINA', title = None), 
        color=alt.Color('SIT_MATR:N'),
        ).properties(width=260, height=300).facet(
        column=alt.Column('CODPERLET:N', title = None),
        ).resolve_scale(x='independent')

st.altair_chart(g2, use_container_width=True)

with st.expander("Ver base"):
    st.dataframe(df2.style.format({"CODPERLET": "{:.0f}"}))

