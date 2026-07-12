# 🧠 Fapam MaisVida Preditivo: Inteligência Artificial Aplicada ao Diagnóstico Situacional do Idoso

**Pós-Graduação em Data Science e Machine Learning - XP Educação**

## 👤 Autoria
- **Autor:** Reinaldo Ríchardi Oliveira Galvão
- **Orientador:** Marcos Prochnow
- **Local e Data:** Pará de Minas - MG | Julho de 2026

## 🎯 Objetivo do Projeto

Desenvolver um protótipo funcional de **Machine Learning** treinado com a base de dados municipal para classificar a **probabilidade de risco clínico de diabetes e hipertensão** na população idosa, auxiliando no rastreio precoce e embasando a formulação de políticas públicas proativas.

## 💻 Tecnologias Utilizadas

- **Python 3.13**
- **Pandas** - Manipulação de dados
- **Scikit-learn** - Modelos de Machine Learning
- **Matplotlib & Seaborn** - Visualizações
- **Streamlit** - Interface web interativa
- **Jupyter Notebook** - Análise exploratória

## 📋 Estrutura do Projeto

```
diagnostico_60mais/
├── notebooks/
│   ├── Diagnostico_60mais_PA.ipynb    # Análise completa em Jupyter
│   ├── dist_idade.png                 # Gráficos gerados
│   ├── matriz_correlacao.png
│   └── dist_targets.png
├── data/
│   └── Dados Completos - Fapam Pesquisa.xlsx  # Dataset original
├── app.py                             # Aplicação Streamlit
├── requirements.txt                   # Dependências do projeto
├── .gitignore
└── README.md                          # Este arquivo
```

## 🚀 Como Executar o Projeto

### 1. Clonar o Repositório
```bash
git clone https://github.com/seu-usuario/diagnostico_60mais.git
cd diagnostico_60mais
```

### 2. Criar Ambiente Virtual
```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate
```

### 3. Instalar Dependências
```bash
pip install -r requirements.txt
```

### 4. Executar a Aplicação Streamlit
```bash
streamlit run app.py
```

A aplicação estará disponível em `http://localhost:8501`

### 5. Explorar o Notebook (Opcional)
```bash
jupyter notebook notebooks/Diagnostico_60mais_PA.ipynb
```

## 📊 Dataset

- **Total de Registros:** 300 pacientes idosos
- **Idade Média:** 73.8 anos (mín: 24, máx: 100)
- **Composição:** 100% feminino
- **Variáveis Independentes (Features):**
  - Idade
  - Sexo Biológico
  - Hábitos Alimentares
  - Atividade Física
  - Uso de Tabaco

- **Variáveis Dependentes (Targets):**
  - Diagnóstico de Diabetes
  - Diagnóstico de Hipertensão

## 🤖 Modelos Implementados

### Sprint 1: Preparação e Exploração de Dados

1. **Data Cleaning**
   - Identificação e tratamento de valores nulos
   - Remoção de inconsistências na coleta em campo

2. **Feature Engineering**
   - Transformação de variáveis categóricas
   - Padronização baseada em Dicionário de Dados
   - Codificação de features (0/1)

3. **Análise Exploratória (EDA)**
   - Distribuição dos targets
   - Matriz de Correlação de Pearson
   - Análise de balanceamento

4. **Modelagem**
   - **Baseline:** Logistic Regression (Recall: 0.XX)
   - **Modelo Otimizado:** Random Forest com GridSearchCV (Recall: 0.XX)

## 📈 Resultados

### Distribuição de Diagnósticos
- **Diabetes:** 181 "Não" vs 119 "Sim" (40% positivos)
- **Hipertensão:** 71 "Não" vs 229 "Sim" (76% positivos)

### Feature Importance (Random Forest)
Top 3 variáveis mais importantes para predição:
1. Idade
2. Atividade Física
3. Hábitos Alimentares

## 🎨 Aplicação Streamlit

A interface oferece 3 seções principais:

### 1. 🔍 Predição
- Input do paciente (idade, sexo, tabagismo, etc)
- Cálculo de risco de diabetes e hipertensão
- Recomendações clínicas personalizadas

### 2. 📊 Análise de Dados
- Gráficos exploratórios
- Distribuição de variáveis
- Matriz de correlação

### 3. ℹ️ Informações
- Detalhes do projeto
- Descrição do dataset
- Informações sobre modelos

## ⚠️ Limitações e Considerações

- Este é um **protótipo educacional** para fins acadêmicos
- Os scores de risco utilizam heurísticas simplificadas
- Recomenda-se validação clínica antes do uso em ambiente produção
- **Sempre consulte um médico para confirmação diagnóstica**

## 📞 Disclaimer

Esta aplicação foi desenvolvida para fins educacionais. Os resultados são estimativas baseadas em modelos de machine learning e **não substituem avaliação clínica profissional**. Sempre consulte um profissional de saúde qualificado.

## 📚 Referências

- Base de dados: "Dados Completos - Fapam Pesquisa.xlsx"
- Framework: [Streamlit](https://streamlit.io/)
- Modelos: [scikit-learn](https://scikit-learn.org/)
- Análise: Pandas, NumPy, Matplotlib, Seaborn

## 📝 Licença

Este projeto é fornecido como trabalho acadêmico. Direitos reservados.

## 🤝 Contribuições

Contribuições são bem-vindas! Abra uma issue ou pull request para sugestões de melhorias.

---

**Última atualização:** Julho de 2026
