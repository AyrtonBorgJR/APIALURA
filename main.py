from fastapi import FastAPI, Query
import requests

app = FastAPI()

@app.get('/api/hello')
def hello_world():
    """TESTE DE MENSAGEM SOBRE A DOCUMENTAÇÃO"""
    return {'Hello':'World'}
    

@app.get('/api/restaurantes/')
def get_restaurantes(restaurante: str = Query(None)):

    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

    response = requests.get(url)

    if response.status_code == 200:
        dados_json = response.json()
        if restaurante is None:
            return {'Dados': dados_json}

        dados_restaurante = [] # Criação de dicionário
        for item in dados_json:
            if item['Company'] == restaurante:
                    dados_restaurante.append({
                    "item": item['Item'], #item para acesso a coisas do Json
                    "price": item['price'],
                    "description": item['description']
                    })
        return{'Restaurante':restaurante,'Itens':dados_restaurante}
            
    else:
        return(f'Erro:{response.status_code} - {response.text}')