import requests
import json

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

response = requests.get(url)


if response.status_code == 200:
    dados_json = response.json()
    dados_restaurante = {} # Criação de dicionário
    for item in dados_json:
        nome_restaurante = item['Company']
        if nome_restaurante not in dados_restaurante: #SE O NOME NÃO EXISTER, ADICIONA, SE EXISTIR, ELE IGNORA.
            dados_restaurante[nome_restaurante] = []
        
        dados_restaurante[nome_restaurante].append({
            "item": item['Item'], #item para acesso a coisas do Json
            "price": item['price'],
            "description": item['description']
            })
        

else:
    print(f'O erro foi o {response.status_code}')

for nome_restaurante, dados in dados_restaurante.items():
    nome_do_arquivo = f'{nome_restaurante}.json'
    with open(nome_do_arquivo, 'w') as arquivo_restaurante:
        json.dump(dados, arquivo_restaurante, indent=4)


###print(dados_restaurante['Wendy’s'])

###print(list(dados_restaurante.keys())) # IMPRIMIR TODOS DE UMA CATEGORIA