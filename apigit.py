import requests
import pandas as pd


url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

r = requests.get(url)
print('Status code:', r.status_code)

response_dict = r.json()
print(response_dict.keys())

print('Total repositories:', response_dict['total_count'])
repo_dicts = response_dict['items']
#print('Repositories returned:', len(repo_dicts))
#repo_dict = repo_dicts[0]
# print('\nKeys:', len(repo_dict))
# for key in sorted(repo_dict.keys()):
#     print(key)
nome = []
proprietario = []
estrela = []
caminho = []
criado = []
atualizado = []
descricao = []
# print('\nSelected infordmation about each repository:')
for repo_dict in repo_dicts:

     nome.append(repo_dict['name'])
     proprietario.append(repo_dict['owner']['login'])
     estrela.append(repo_dict['stargazers_count'])
     caminho.append(repo_dict['html_url'])
     criado.append(repo_dict['created_at'])
     atualizado.append(repo_dict['updated_at'])
     descricao.append(repo_dict['description'])
#df = pd.DataFrame.from_dict(repo_dicts)
df = pd.DataFrame({'nomes': nome, 'proprietarios': proprietario, 'estrelas':estrela, 'caminhos': caminho,
                       'criados': criado, 'atualizado': atualizado, 'descricaos':descricao})

df.to_excel('resultado.xlsx', index=False)





