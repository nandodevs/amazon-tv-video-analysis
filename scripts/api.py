import pandas as pd
import wikipedia

# Carregar o arquivo CSV
dataset = pd.read_csv('scripts\dataset_origin.csv')

# Identificar os registros com dados vazios na coluna "director"
registros_vazios = dataset[dataset['director'].isnull()]

# Configurar o User-Agent personalizado
wikipedia.set_user_agent('Seu_Nome_De_Usuário/1.0')

# Iterar sobre os registros vazios
for index, row in registros_vazios.iterrows():
    # Obter o título do filme
    titulo_filme = row['title']
    
    try:
        # Obter o objeto de página do Wikipedia
        page = wikipedia.page(titulo_filme)
        
        # Verificar se a seção de diretor está presente no conteúdo da página
        if 'Directed by' in page.content:
            # Extrair o nome do diretor a partir do conteúdo da página
            start_index = page.content.index('Directed by') + len('Directed by')
            end_index = page.content.index('\n', start_index)
            nome_diretor = page.content[start_index:end_index].strip()
            
            # Preencher o valor vazio na coluna "director" com o nome do diretor obtido
            dataset.at[index, 'director'] = nome_diretor
    except wikipedia.exceptions.PageError:
        # Tratar o caso em que a página não foi encontrada
        print(f'A página do filme "{titulo_filme}" não foi encontrada no Wikipedia.')

# Exibir o dataset com os dados preenchidos
print(dataset)