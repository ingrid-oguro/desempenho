import pickle 
from pathlib import Path
import streamlit as st
import streamlit_authenticator as stauth 
import pandas as pd
from base import *
import pip
pip.main(["install", "openpyxl","streamlit_authenticator"])
# --- Authentication

names = ["Marcelo Dias","Simone Bortoletto","Jose Campos","Fernando Umezu","Fernando Henrique","Rodrigo Aquino"]
usernames = ["marcelo","simone.cruz","jose.campos","fernando.umezu","fernando.henriques","rodrigo.aquino"]

# load hashed passwords

#file_path = Path(__file__).parent / "hashed.pw.pkl"
file_path = Path("hashed_pw.pkl")
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

    credentials = {
        "usernames":{
            usernames[0]:{
                "name":names[0],
                "password":hashed_passwords[0]
                },
            usernames[1]:{
                "name":names[1],
                "password":hashed_passwords[1]
                },
            usernames[2]:{
                "name":names[2],
                "password":hashed_passwords[2]
                },
            usernames[3]:{
                "name":names[3],
                "password":hashed_passwords[3]
                },
            usernames[4]:{
                "name":names[4],
                "password":hashed_passwords[4]
                },
            usernames[5]:{
                "name":names[5],
                "password":hashed_passwords[5]
                }            
            }
        }

authenticator = stauth.Authenticate(credentials,
                                    "sales_dashboard",
                                    "abcdef",
                                    cookie_expiry_days=0)

#authenticator = stauth.Authenticate(credentials, "app_home", "auth", cookie_expiry_days=30)
name, authentication_status, username = authenticator.login("Login","main")

if authentication_status == False:
    st.error("Username/password is incorrect")

if authentication_status == None:
    st.warning("Enter username and password")

if authentication_status:
    
    with st.sidebar:
        st.write("Bem vindo, "+name+".")
    authenticator.logout("Logout","sidebar")

    st.title("Nota e Frequência por aluno.")
    #GERAL
    if username == "marcelo":
        curso = sorted(df.Curso.unique())
        curso_selecionado = st.selectbox('Graduação:',curso)
        df1 = df.query('Curso == @curso_selecionado	')

    #GERAL
    if username == "simone.cruz":
        curso = sorted(df.Curso.unique())
        curso_selecionado = st.selectbox('Graduação:',curso)
        df1 = df.query('Curso == @curso_selecionado	')

    #ECONOMIA
    elif username == "fernando.umezu":
        curso = ['Ciências Econômicas']
        curso_selecionado = st.selectbox('Graduação:',curso)
        df1 = df.query('Curso == @curso_selecionado	')  

    #ADM
    elif username == "jose.campos":
        curso = ['Administração']
        curso_selecionado = st.selectbox('Graduação:',curso)
        df1 = df.query('Curso == @curso_selecionado	')

    #DTO
    elif username == "fernando.henriques":
        curso = ['Direito']
        curso_selecionado = st.selectbox('Graduação:',curso)
        df1 = df.query('Curso == @curso_selecionado	')


    #ECO
    elif username == "rodrigo.aquino":
        curso = ['Engenharia de Computação']
        curso_selecionado = st.selectbox('Graduação:',curso)
        df1 = df.query('Curso == @curso_selecionado	')
    
    #botão disciplina
    disciplinas = sorted(df1.DISCIPLINA.unique())
    disciplinas_selecionada = st.selectbox('Disciplina:',disciplinas)
    df1 = df1.query('DISCIPLINA == @disciplinas_selecionada')

    #botão provas
    provas = [
                # 'MED_FINAL',
                'PROVA1',
                # 'PROVA2','NC1','EXCJ1',
                # 'PROVA3','PROVA4','NC2','EXCJ2','ATIV1',
                # 'ATIV2','ATIV3','ATIV4','ATIV5','EXA_FINAL'
                ]
    disciplinas_selecionada = st.selectbox('Provas:',provas)
    #df1 = df1.query('DISCIPLINA == @disciplinas_selecionada')

    g1 = alt.Chart(df1).mark_circle(size=100).encode(
            alt.X('FREQ',scale=alt.Scale(zero=False),axis=alt.Axis(format='%', title='FREQ') ),
            alt.Y('PROVA1',scale=alt.Scale(zero=False) ,axis=alt.Axis(title='Nota', orient = "left") ),
            tooltip = ['NOME','RA','PROVA1' , alt.Tooltip('FREQ:Q', format='.1%')]).interactive().properties(width=900,height=400)

    st.altair_chart(linha_horizontal + linha_vertical + g1, use_container_width=True)
    # with st.expander("Ver base"):
    #     st.dataframe(df1.style.format({"CODPERLET": "{:.0f}"}))
        
    a = df.groupby(['RA',  'NOME','Curso'])['PROVA1'].mean()
    b = a.to_frame()
    c = b.reset_index()
    d = c.sort_values(by=['PROVA1'], ascending=False)


    with st.expander("Ver base"):
        st.dataframe(d.style.format({"RA": "{:.0f}"}),width=800, height=400)

    #Gráfico 2

    # curso2 = sorted(df.Curso.unique())
    # curso_selecionado2 = st.selectbox('Graduação :',curso2)
    # df2 = df.query('Curso == @curso_selecionado2	 ')

    aluno = sorted(df1.NOME.unique())
    aluno_selecionado = st.selectbox('Aluno :',aluno)
    df3 = df1.query('NOME == @aluno_selecionado')

    g2 = alt.Chart(df3).mark_bar().encode(
            x=alt.X('PROVA1'),
            y=alt.Y('DISCIPLINA', title = None), 
            color=alt.Color('STATUS:N'),
            ).properties(width=460, height=300).facet(
            column=alt.Column('CODPERLET:N', title = None),
            ).resolve_scale(y='independent')

    st.altair_chart(g2, use_container_width=True)

    with st.expander("Ver base"):
        st.dataframe(df3.style.format({"CODPERLET": "{:.0f}"}))




