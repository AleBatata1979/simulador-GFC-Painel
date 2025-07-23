import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Painel do Professor - Sistema 3M", layout="wide")

st.title("📊 Painel do Professor - Sistema 3M")

# Caminhos
pasta_data = "data"
dre_corrigidas = os.path.join(pasta_data, "dre_corrigidas")
indicadores_corrigidos = os.path.join(pasta_data, "indicadores_corrigidos")

# Criação de pastas se não existirem
os.makedirs(dre_corrigidas, exist_ok=True)
os.makedirs(indicadores_corrigidos, exist_ok=True)

st.header("1️⃣ Fundos Cadastrados")

fundos_file = os.path.join(pasta_data, "fundos_cadastrados.csv")

if os.path.exists(fundos_file):
    df_fundos = pd.read_csv(fundos_file)
    st.dataframe(df_fundos)
else:
    st.warning("Nenhum fundo cadastrado ainda.")

st.header("2️⃣ Corrigir DRE Previstas")

arquivos_dre = os.listdir(dre_corrigidas)
if arquivos_dre:
    for arquivo in arquivos_dre:
        st.subheader(f"DRE - {arquivo}")
        df = pd.read_csv(os.path.join(dre_corrigidas, arquivo))
        st.dataframe(df)
else:
    st.info("Nenhuma DRE enviada ainda.")

st.header("3️⃣ Corrigir Indicadores")

arquivos_ind = os.listdir(indicadores_corrigidos)
if arquivos_ind:
    for arquivo in arquivos_ind:
        st.subheader(f"Indicadores - {arquivo}")
        df = pd.read_csv(os.path.join(indicadores_corrigidos, arquivo))
        st.dataframe(df)
else:
    st.info("Nenhum painel de indicadores enviado ainda.")

st.header("4️⃣ Liberação das Etapas")

if st.button("🔓 Liberar próxima etapa para todos os fundos"):
    st.success("✅ Próxima etapa liberada!")
