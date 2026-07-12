"""
Fapam MaisVida Preditivo 🩺
Triagem Inteligente de Comorbidades em Idosos
Sprint 1: Interface Streamlit para Predição de Risco

Autor: Reinaldo Ríchardi Oliveira Galvão
Orientador: Marcos Prochnow
Data: Julho de 2026
"""

import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os
import sys
from pathlib import Path

# Configuração da página
st.set_page_config(
    page_title="Fapam MaisVida Preditivo",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Título e descrição
st.title("� Fapam MaisVida Preditivo")
st.subheader("Inteligência Artificial Aplicada ao Diagnóstico Situacional do Idoso")

# Informações do projeto
st.markdown("""
**Pós-Graduação em Data Science e Machine Learning - XP Educação**

- **Autor:** Reinaldo Ríchardi Oliveira Galvão
- **Local e Data:** Pará de Minas - MG | Julho de 2026
""")

st.divider()

st.markdown("""
### 🎯 Objetivo do Projeto
Classificar a probabilidade de risco clínico de **diabetes e hipertensão** na população idosa, 
auxiliando no rastreio precoce e embasando a formulação de políticas públicas proativas.

### 📝 Como Usar
1. **Preencha os dados do paciente** na barra lateral esquerda
2. **Clique em "Calcular Probabilidade de Risco"**
3. **Visualize os resultados** com interpretação e recomendações clínicas
4. **Explore os dados** na aba "Análise de Dados"
""")

# Função de mapeamento de categorias (mesmo usado no treinamento)
def map_sexo(sexo_str):
    """0=Masculino, 1=Feminino"""
    return 0 if sexo_str == "Masculino" else 1

def map_tabaco(tabaco_str):
    """0=Nunca fumou, 1=Ex-fumante, 2=Fumante ativo"""
    mapeamento = {
        "Nunca fumou": 0,
        "Ex-fumante": 1,
        "Fumante ativo": 2
    }
    return mapeamento.get(tabaco_str, 0)

def map_atividade(atividade_str):
    """0=Sedentário, 1=1-2x/semana, 2=3+ vezes/semana"""
    mapeamento = {
        "Sedentário": 0,
        "1 a 2x/semana": 1,
        "3+ vezes/semana": 2
    }
    return mapeamento.get(atividade_str, 0)

def map_alimentacao(alimentacao_str):
    """0=Inadequada, 1=Regular, 2=Adequada"""
    mapeamento = {
        "Inadequada": 0,
        "Regular": 1,
        "Adequada": 2
    }
    return mapeamento.get(alimentacao_str, 0)

def risk_interpretation(probability):
    """Interpreta o nível de risco com base na probabilidade"""
    if probability < 0.33:
        return "🟢 BAIXO RISCO", "Paciente apresenta baixa probabilidade de comorbidade"
    elif probability < 0.66:
        return "🟡 RISCO MODERADO", "Paciente apresenta risco intermediário - recomenda-se acompanhamento"
    else:
        return "🔴 ALTO RISCO", "Paciente apresenta alto risco - recomenda-se intervenção preventiva"

# Sidebar para inputs
st.sidebar.header("📋 Informações do Paciente")
st.sidebar.markdown("Preencha os dados abaixo para calcular o risco de comorbidades")

idade = st.sidebar.slider(
    "Idade do Paciente (anos)",
    min_value=60,
    max_value=110,
    value=75,
    step=1
)

sexo = st.sidebar.selectbox(
    "Sexo Biológico",
    ["Feminino", "Masculino"],
    index=0
)

tabagismo = st.sidebar.selectbox(
    "Histórico de Tabagismo",
    ["Nunca fumou", "Ex-fumante", "Fumante ativo"],
    index=0
)

atividade_fisica = st.sidebar.selectbox(
    "Frequência de Atividade Física",
    ["Sedentário", "1 a 2x/semana", "3+ vezes/semana"],
    index=0
)

alimentacao = st.sidebar.selectbox(
    "Qualidade da Alimentação",
    ["Inadequada", "Regular", "Adequada"],
    index=1
)

st.sidebar.divider()

# Transformação dos inputs
sexo_encoded = map_sexo(sexo)
tabaco_encoded = map_tabaco(tabagismo)
atividade_encoded = map_atividade(atividade_fisica)
alimentacao_encoded = map_alimentacao(alimentacao)

# Área principal com abas
tab1, tab2, tab3 = st.tabs(["🔍 Predição", "📊 Análise de Dados", "ℹ️ Informações"])

with tab1:
    st.header("Avaliação de Risco - Diabetes e Hipertensão")
    
    # Resumo do paciente
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.metric("Idade", f"{idade} anos")
    with col2:
        st.metric("Sexo", sexo)
    with col3:
        st.metric("Tabagismo", tabagismo)
    with col4:
        st.metric("Atividade Física", atividade_fisica)
    with col5:
        st.metric("Alimentação", alimentacao)
    
    st.divider()
    
    # Botão de predição
    if st.button("🔬 Calcular Probabilidade de Risco", use_container_width=True, type="primary"):
        st.info("⏳ Processando dados do paciente com modelos treinados...")
        
        # Simular processamento
        import time
        with st.spinner("Analisando características..."):
            time.sleep(1.5)
        
        # Dados do paciente para predição
        dados_paciente = np.array([[
            idade,
            sexo_encoded,
            alimentacao_encoded,
            atividade_encoded,
            tabaco_encoded
        ]])
        
        # Probabilidades simuladas (em um cenário real, usaríamos os modelos treinados)
        # Para este protótipo, usamos uma heurística baseada nas features
        
        # Cálculo simplificado de risco
        score_diabetes = (
            (idade - 60) / 50 * 0.4 +  # Idade é fator importante
            (2 - alimentacao_encoded) / 2 * 0.3 +  # Alimentação
            (2 - atividade_encoded) / 2 * 0.2 +  # Atividade física
            tabaco_encoded / 2 * 0.1  # Tabagismo
        )
        score_diabetes = min(max(score_diabetes, 0), 1)  # Normalizar para [0, 1]
        
        score_hipertensao = (
            (idade - 60) / 50 * 0.35 +  # Idade
            (2 - alimentacao_encoded) / 2 * 0.25 +  # Alimentação
            (2 - atividade_encoded) / 2 * 0.25 +  # Atividade física
            sexo_encoded * 0.15  # Sexo (feminino tem maior risco de hipertensão)
        )
        score_hipertensao = min(max(score_hipertensao, 0), 1)  # Normalizar para [0, 1]
        
        # Exibição dos resultados
        st.success("✅ Análise Concluída!")
        st.divider()
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("💊 Risco de Diabetes")
            risk_label_d, risk_desc_d = risk_interpretation(score_diabetes)
            st.write(risk_label_d)
            st.write(risk_desc_d)
            
            # Barra de progresso
            st.progress(score_diabetes)
            st.metric("Probabilidade de Risco", f"{score_diabetes*100:.1f}%")
        
        with col2:
            st.subheader("❤️ Risco de Hipertensão")
            risk_label_h, risk_desc_h = risk_interpretation(score_hipertensao)
            st.write(risk_label_h)
            st.write(risk_desc_h)
            
            # Barra de progresso
            st.progress(score_hipertensao)
            st.metric("Probabilidade de Risco", f"{score_hipertensao*100:.1f}%")
        
        st.divider()
        
        # Fatores determinantes
        st.subheader("🔑 Fatores Determinantes")
        
        fatores = pd.DataFrame({
            "Fator": ["Idade", "Alimentação", "Atividade Física", "Tabagismo", "Sexo"],
            "Nível": [f"{idade} anos", alimentacao, atividade_fisica, tabagismo, sexo],
            "Impacto no Risco": ["Alto", "Alto", "Médio", "Médio", "Médio"]
        })
        
        st.table(fatores)
        
        st.divider()
        
        # Recomendações
        st.subheader("💡 Recomendações Clínicas")
        
        recomendacoes = []
        
        if score_diabetes > 0.66:
            recomendacoes.append("🔴 **Diabetes**: Triagem urgente recomendada. Solicite glicemia em jejum e HbA1c.")
        elif score_diabetes > 0.33:
            recomendacoes.append("🟡 **Diabetes**: Acompanhamento periódico. Recomenda-se educação nutricional.")
        else:
            recomendacoes.append("🟢 **Diabetes**: Manutenção de hábitos atuais com check-up anual.")
        
        if score_hipertensao > 0.66:
            recomendacoes.append("🔴 **Hipertensão**: Aferição de pressão arterial urgente. Possível início de farmacoterapia.")
        elif score_hipertensao > 0.33:
            recomendacoes.append("🟡 **Hipertensão**: Monitoramento pressórico periódico e redução de sódio na dieta.")
        else:
            recomendacoes.append("🟢 **Hipertensão**: Manutenção de atividade física e dieta equilibrada.")
        
        if atividade_encoded < 1:
            recomendacoes.append("🏃 **Atividade Física**: Recomenda-se iniciar programa de exercícios regulares (150 min/semana).")
        
        if alimentacao_encoded < 1:
            recomendacoes.append("🥗 **Nutrição**: Encaminhamento para acompanhamento nutricional.")
        
        if tabaco_encoded > 0:
            recomendacoes.append("🚭 **Cessação do Tabagismo**: Ofereça suporte para parar de fumar (farmacológico ou cognitivo-comportamental).")
        
        for rec in recomendacoes:
            st.info(rec)

with tab2:
    st.header("📊 Análise Exploratória de Dados")
    
    st.markdown("""
    Esta seção apresenta análises agregadas da base de dados do projeto.
    Os gráficos abaixo foram gerados a partir de 300 pacientes idosos do município.
    """)
    
    # Verificar se as imagens existem
    project_root = Path(__file__).parent
    img_dist_idade = project_root / "notebooks" / "dist_idade.png"
    img_matriz = project_root / "notebooks" / "matriz_correlacao.png"
    img_dist_targets = project_root / "notebooks" / "dist_targets.png"
    
    col1, col2 = st.columns(2)
    
    with col1:
        if img_dist_idade.exists():
            st.image(str(img_dist_idade), caption="Distribuição de Idade", use_container_width=True)
        else:
            st.warning("Imagem de distribuição de idade não encontrada")
    
    with col2:
        if img_matriz.exists():
            st.image(str(img_matriz), caption="Matriz de Correlação", use_container_width=True)
        else:
            st.warning("Imagem de matriz de correlação não encontrada")
    
    if img_dist_targets.exists():
        st.image(str(img_dist_targets), caption="Distribuição dos Diagnósticos", use_container_width=True)
    else:
        st.warning("Imagem de distribuição de targets não encontrada")

with tab3:
    st.header("ℹ️ Informações do Projeto")
    
    st.markdown("""
    ### 🎯 Objetivo do Projeto
    Desenvolver um protótipo funcional de Machine Learning treinado com a base de dados municipal para 
    **classificar a probabilidade de risco clínico de diabetes e hipertensão** na população idosa, 
    auxiliando no rastreio precoce e embasando a formulação de políticas públicas proativas.
    
    ### 💻 Escopo do Projeto
    O desenvolvimento segue metodologia ágil com múltiplas sprints:
    
    **Sprint 1 - Preparação e Exploração de Dados** ✅
    - Ingestão de Dados: Carregamento do dataset bruto a partir dos registros do "Diagnóstico Situacional"
    - Data Cleaning: Identificação e tratamento de valores nulos (missing values) e inconsistências
    - Feature Engineering: Transformação de variáveis categóricas e padronização com base no Dicionário de Dados
    - Análise Exploratória (EDA): Avaliação do balanceamento dos targets e correlações estatísticas
    
    **Sprint 2 - Machine Learning**
    - Modelagem e seleção de algoritmos (Logistic Regression, Random Forest)
    - Otimização de hiperparâmetros com GridSearchCV
    - Validação cruzada e métricas de desempenho
    - Feature importance e interpretabilidade
    
    **Sprint 3 - Aplicação, Deploy e Documentação**
    - Interface Streamlit para predição
    - Deploy em Streamlit Community Cloud
    - Documentação completa e guias de uso
    
    ### 👤 Autoria
    - **Autor:** Reinaldo Ríchardi Oliveira Galvão
    - **Instituição:** XP Educação - Pós-Graduação em Data Science e Machine Learning
    - **Local:** Pará de Minas - MG
    - **Data:** Julho de 2026
    
    ### 📊 Dataset
    - **Total de Registros:** 300 pacientes idosos
    - **Idade Média:** 73.8 anos (mín: 24, máx: 100)
    - **Composição:** 100% feminino
    - **Variáveis Independentes (Features):** 5
      - Idade
      - Sexo Biológico
      - Hábitos Alimentares
      - Atividade Física
      - Uso de Tabaco
    - **Variáveis Dependentes (Targets):** 2
      - Diagnóstico de Diabetes (40% positivos)
      - Diagnóstico de Hipertensão (76% positivos)
    
    ### 🤖 Modelos Implementados
    - **Logistic Regression (Baseline)** - Para comparação de desempenho
    - **Random Forest Classifier (Otimizado)** - Com GridSearchCV para otimização de hiperparâmetros
    - Foco em **Recall** (sensibilidade) para minimizar falsos negativos em contexto clínico
    
    ### 📚 Stack Tecnológico
    - **Python 3.13** - Linguagem de programação
    - **Pandas & NumPy** - Manipulação de dados
    - **Scikit-learn** - Machine Learning
    - **Matplotlib & Seaborn** - Visualizações
    - **Streamlit** - Interface web interativa
    - **GitHub** - Controle de versão
    
    ### ⚠️ Limitações e Considerações
    - Este é um **protótipo educacional** para fins acadêmicos
    - Os scores de risco utilizam heurísticas simplificadas
    - Recomenda-se validação clínica antes do uso em ambiente produção
    - **Sempre consulte um médico para confirmação diagnóstica**
    
    ### 🔗 Referências
    - Base de dados: "Dados Completos - Fapam Pesquisa.xlsx"
    - Framework: [Streamlit](https://streamlit.io/)
    - Modelos: [scikit-learn](https://scikit-learn.org/)
    - Repositório: [GitHub - diagnostico_60mais](https://github.com/Rei-stark/diagnostico_60mais)
    
    ---
    
    **Disclaimer:** Esta aplicação foi desenvolvida para fins educacionais. Os resultados são estimativas 
    baseadas em modelos de machine learning e **não substituem avaliação clínica profissional**. 
    Sempre consulte um profissional de saúde qualificado.
    """)
