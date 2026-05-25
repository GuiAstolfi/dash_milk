import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_csv('informacoes_milk.csv')
df['diferenca'] = df['soma_ano'] - df['qtd_ano_anterior']

df_arisona = df.query('State == "ARIZONA"').reset_index(drop=True)
df_california = df.query('State == "CALIFORNIA"').reset_index(drop=True)
df_colorado = df.query('State == "COLORADO"').reset_index(drop=True)
df_florida = df.query('State == "FLORIDA"').reset_index(drop=True)

st.set_page_config( layout='wide')
st.write('### Gráficos de Vendas dos Estados')
st.sidebar.write('# Escolha um Estado')
opicao = st.sidebar.selectbox('Selecione uma opção:', ('ARIZONA', 'CALIFORNIA', 'COLORADO', 'FLORIDA'), index=None)
st.sidebar.markdown('---')

if opicao == 'ARIZONA':
    opicao2 = st.radio('**Escolha um Gráfico:**', ('Renda Total por Ano', 'Soma Acumulada Dos Anos',
    'Análise YoY', 'Percentual De Cada Ano Sobre a Soma Total Dos Anos'), index=None)
    if opicao2 == 'Renda Total por Ano':
        soma_ano_arisona = px.bar(df_arisona, x='Year', y='soma_ano', color='State', color_discrete_sequence=['purple'])
        soma_ano_arisona.update_traces(text=df_arisona['soma_ano'], texttemplate='%{text:$,.0f}', textposition='outside')
        st.plotly_chart(soma_ano_arisona)
    elif opicao2 == 'Soma Acumulada Dos Anos':
        soma_acumulada_arisona = px.bar(df_arisona, x='Year', y='Soma_ac', color='State', color_discrete_sequence=['purple'])
        soma_acumulada_arisona.update_traces(text=df_arisona['Soma_ac'], texttemplate='%{text:$,.0f}', textposition='outside')
        st.plotly_chart(soma_acumulada_arisona)
    elif opicao2 == 'Análise YoY':
        analise_arisona = px.bar(df_arisona, x='Year', y='diferenca', color='State', color_discrete_sequence=['purple'])
        analise_arisona.update_traces(text=df_arisona['diferenca'], texttemplate='%{text:$,.0f}', textposition='outside')
        st.plotly_chart(analise_arisona)
    elif opicao2 == 'Percentual De Cada Ano Sobre a Soma Total Dos Anos':
        percentual_arisona = px.bar(df_arisona, x='Year', y='percentual', color='State', color_discrete_sequence=['purple'])
        percentual_arisona.update_traces(text=df_arisona['percentual'], textposition='outside')
        st.plotly_chart(percentual_arisona)

if opicao == 'CALIFORNIA':
    opicao3 = st.radio('**Escolha um Gráfico:**', ('Renda Total por Ano', 'Soma Acumulada Dos Anos',
    'Análise YoY', 'Percentual De Cada Ano Sobre a Soma Total Dos Anos'), index=None)
    if opicao3 == 'Renda Total por Ano':
        soma_ano_california = px.bar(df_california, x='Year', y='soma_ano', color='State', color_discrete_sequence=['white'])
        soma_ano_california.update_traces(text=df_california['soma_ano'], texttemplate='%{text:$,.0f}', textposition='outside')
        st.plotly_chart(soma_ano_california)
    elif opicao3 == 'Soma Acumulada Dos Anos':
        soma_acumulada_california = px.bar(df_california, x='Year', y='Soma_ac', color='State', color_discrete_sequence=['white'])
        soma_acumulada_california.update_traces(text=df_california['Soma_ac'], texttemplate='%{text:$,.0f}', textposition='outside')
        st.plotly_chart(soma_acumulada_california)
    elif opicao3 == 'Análise YoY':
        analise_california = px.bar(df_california, x='Year', y='diferenca', color='State', color_discrete_sequence=['white'])
        analise_california.update_traces(text=df_california['diferenca'], texttemplate='%{text:$,.0f}', textposition='outside')
        st.plotly_chart(analise_california)
    elif opicao3 == 'Percentual De Cada Ano Sobre a Soma Total Dos Anos':
        percentual_california = px.bar(df_california, x='Year', y='percentual', color='State', color_discrete_sequence=['white'])
        percentual_california.update_traces(text=df_california['percentual'], textposition='outside')
        st.plotly_chart(percentual_california)

if opicao == 'COLORADO':
    opicao4 = st.radio('**Escolha um Gráfico:**', ('Renda Total por Ano', 'Soma Acumulada Dos Anos',
    'Análise YoY', 'Percentual De Cada Ano Sobre a Soma Total Dos Anos'), index=None)
    if opicao4 == 'Renda Total por Ano':
        soma_ano_colorado = px.bar(df_colorado, x='Year', y='soma_ano', color='State', color_discrete_sequence=['red'])
        soma_ano_colorado.update_traces(text=df_colorado['soma_ano'], texttemplate='%{text:$,.0f}', textposition='outside')
        st.plotly_chart(soma_ano_colorado)
    elif opicao4 == 'Soma Acumulada Dos Anos':
        soma_acumulada_colorado = px.bar(df_colorado, x='Year', y='Soma_ac', color='State', color_discrete_sequence=['red'])
        soma_acumulada_colorado.update_traces(text=df_colorado['Soma_ac'], texttemplate='%{text:$,.0f}', textposition='outside')
        st.plotly_chart(soma_acumulada_colorado)
    elif opicao4 == 'Análise YoY':
        analise_colorado = px.bar(df_colorado, x='Year', y='diferenca', color='State', color_discrete_sequence=['red'])
        analise_colorado.update_traces(text=df_colorado['diferenca'], texttemplate='%{text:$,.0f}', textposition='outside')
        st.plotly_chart(analise_colorado)
    elif opicao4 == 'Percentual De Cada Ano Sobre a Soma Total Dos Anos':
        percentual_colorado = px.bar(df_colorado, x='Year', y='percentual', color='State', color_discrete_sequence=['red'])
        percentual_colorado.update_traces(text=df_colorado['percentual'], textposition='outside')
        st.plotly_chart(percentual_colorado)

if opicao == 'FLORIDA':
    opicao5 = st.radio('**Escolha um Gráfico:**', ('Renda Total por Ano', 'Soma Acumulada Dos Anos',
    'Análise YoY', 'Percentual De Cada Ano Sobre a Soma Total Dos Anos'), index=None)
    if opicao5 == 'Renda Total por Ano':
        soma_ano_florida = px.bar(df_florida, x='Year', y='soma_ano', color='State', color_discrete_sequence=['yellow'])
        soma_ano_florida.update_traces(text=df_florida['soma_ano'], texttemplate='%{text:$,.0f}', textposition='outside')
        st.plotly_chart(soma_ano_florida)
    elif opicao5 == 'Soma Acumulada Dos Anos':
        soma_acumulada_florida = px.bar(df_florida, x='Year', y='Soma_ac', color='State', color_discrete_sequence=['yellow'])
        soma_acumulada_florida.update_traces(text=df_florida['Soma_ac'], texttemplate='%{text:$,.0f}', textposition='outside')
        st.plotly_chart(soma_acumulada_florida)
    elif opicao5 == 'Análise YoY':
        analise_florida = px.bar(df_florida, x='Year', y='diferenca', color='State', color_discrete_sequence=['yellow'])
        analise_florida.update_traces(text=df_florida['diferenca'], texttemplate='%{text:$,.0f}', textposition='outside')
        st.plotly_chart(analise_florida)
    elif opicao5 == 'Percentual De Cada Ano Sobre a Soma Total Dos Anos':
        percentual_florida = px.bar(df_florida, x='Year', y='percentual', color='State', color_discrete_sequence=['yellow'])
        percentual_florida.update_traces(text=df_florida['percentual'], textposition='outside')
        st.plotly_chart(percentual_florida)