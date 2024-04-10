# Análise Exploratória de Dados e Dashboard sobre o Amazon Prime Video

## Introdução

Este projeto de análise exploratória de dados visa examinar e entender melhor o crescimento do Amazon Prime Video ao longo dos anos. Utilizando um conjunto de dados que inclui informações sobre os títulos disponíveis na plataforma, como diretor, elenco, país de origem, data de adição, ano de lançamento, classificação, duração, categorias e descrição, realizaremos uma análise para identificar padrões e tendências ao longo do tempo.

## Organização do Projeto

meu_projeto/
│
├── data/
│   ├── raw/              # Dados originais e não processados
│   ├── processed/        # Dados processados e limpos
│   └── external/         # Dados externos adicionais, se necessário
│
├── notebooks/
│   ├── exploratory/      # Notebooks para análise exploratória
│   ├── preprocessing/    # Notebooks para pré-processamento de dados
│   ├── modeling/         # Notebooks para modelagem e análise
│   └── reports/          # Notebooks para geração de relatórios e visualizações
│
└── README.md              # Documentação do projeto

## Dataset

O conjunto de dados utilizado neste projeto inclui as seguintes colunas:

- **show_id**: ID único de cada título.
- **type**: Tipo do conteúdo (Filme ou Série de TV).
- **title**: Título do conteúdo.
- **director**: Diretor do conteúdo.
- **cast**: Elenco do conteúdo.
- **country**: País de origem do conteúdo.
- **date_added**: Data em que o conteúdo foi adicionado ao Amazon Prime Video.
- **release_year**: Ano de lançamento do conteúdo.
- **rating**: Classificação indicativa do conteúdo.
- **duration**: Duração do conteúdo.
- **listed_in**: Categoria(s) do conteúdo.
- **description**: Descrição do conteúdo.

## Objetivos

Os principais objetivos deste projeto são:

1. Realizar uma análise exploratória dos dados para compreender a distribuição e características dos títulos disponíveis no Amazon Prime Video.
2. Identificar padrões e tendências de crescimento do catálogo ao longo dos anos.
3. Criar visualizações e insights através de um dashboard no Power BI para apresentar de forma clara e concisa as descobertas da análise.

## Ferramentas Utilizadas

- Linguagem de Programação: Python
- Bibliotecas: Pandas, Matplotlib, Seaborn
- Ferramenta de Visualização: Power BI

## Metodologia

1. **Coleta e Preparação dos Dados**: Carregar o conjunto de dados, limpar e preparar os dados para análise.
2. **Análise Exploratória de Dados**: Explorar o conjunto de dados, identificar padrões, distribuições e tendências.
3. **Preparação dos Dados para o Dashboard**: Preparar os dados para serem visualizados no Power BI.
4. **Criação do Dashboard**: Desenvolver um dashboard no Power BI com visualizações interativas para apresentar os insights obtidos.
5. **Apresentação dos Resultados**: Compartilhar os resultados da análise e as conclusões obtidas através do dashboard.

## Conclusão

Este projeto fornecerá insights valiosos sobre o crescimento do Amazon Prime Video ao longo dos anos, destacando padrões e tendências no catálogo de filmes e programas de TV. O dashboard criado no Power BI permitirá uma apresentação visual e interativa desses insights, facilitando a compreensão e a comunicação dos resultados obtidos.

Para executar o código Python e visualizar o dashboard no Power BI, consulte o arquivo README.md do repositório.
