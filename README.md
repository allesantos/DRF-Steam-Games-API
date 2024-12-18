# Steam Games API
Uma API criada com Django e Django Rest Framework para consultar e baixar a lista de todos os jogos de um usuário na Steam.

## Índice
- [Descrição](#Descrição)
- [Recursos](#Recursos)
- [Pré-requisitos](#Pré-requisitos)
- [Instalação](#Instalação)
- [Uso](#Uso)
- [Contribuição](#Contribuição)
- [Licença](#Licença)

## Descrição
Este projeto foi desenvolvido para permitir que usuários da Steam consultem e baixem a lista completa de jogos vinculados às suas contas. Ele utiliza a API pública da Steam para obter informações sobre os jogos e foi construído usando Django e Django Rest Framework (DRF) para fornecer uma interface RESTful.

### Principais funcionalidades
- Consultar a lista de jogos de um usuário com base no Steam ID.
- Baixar a lista de jogos em formato JSON.
- Interface RESTful para integração com outras aplicações.

## Recursos
__Frameworks usados:__
- Django 4.x
- Django Rest Framework (DRF)
  
__APIs utilizadas:__
- API Pública da Steam
  
__Formatos de saída:__
- JSON

## Pré-requisitos
Antes de começar, você precisará ter as seguintes ferramentas instaladas:

- Python 3.x
- Git
- Uma chave de API da Steam (pode ser obtida [aqui](https://steamcommunity.com/dev/apikey)).
  
Além disso, é recomendável o uso de um ambiente virtual Python para gerenciar dependências.

## Instalação
1. Clone o repositório para sua máquina local:
   
  ```
  git clone https://github.com/seu-usuario/nome-do-repositorio.git
  cd nome-do-repositorio
  ```

2. Crie um ambiente virtual e ative-o:
   
  ```
  python -m venv venv
  source venv/bin/activate  # No Windows: venv\Scripts\activate
  ```

3. Instale as dependências do projeto:
   
  ```
  pip install -r requirements.txt
  ```

4. Configure as variáveis de ambiente para a chave da API da Steam no arquivo .env:
   
  ```
  STEAM_API_KEY=YOUR_STEAM_API_KEY
  ```

5. Execute as migrações do banco de dados:   
  ```
  python manage.py migrate
  ```

6. Inicie o servidor de desenvolvimento:
   
  ```
  python manage.py runserver
  ```

## Uso
### 1. Endpoints principais
- __Listar jogos de um usuário (GET)__
  
  ```
  GET /api/games/{steam_id}/
  ```

Retorna uma lista de jogos vinculados ao Steam ID fornecido.

- __Baixar lista de jogos (GET)__
  
  ```
  GET /api/games/{steam_id}/download/
  ```
Baixa a lista de jogos em formato JSON.

### 2. Exemplo de resposta
__Endpoint:__ /api/games/{steam_id}/

  ```
  [
  {
    "name": "Counter-Strike: Global Offensive",
    "playtime_forever": 1200,
    "last_played": "2024-12-01"
  },
  {
    "name": "Dota 2",
    "playtime_forever": 4500,
    "last_played": "2024-11-25"
  }
]
  ```

## Contribuição

Sinta-se à vontade para contribuir com o projeto! Basta seguir estas etapas:

1. Faça um fork do repositório.
   
2. Crie uma nova branch para sua feature/bugfix:

  ```
git checkout -b minha-feature
```

3. Envie suas alterações:

  ```
git push origin minha-feature
```
4. Abra um Pull Request.
