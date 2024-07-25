### Api Lista de convidados.


# API de gerenciamento de lista de convidados

Esta é uma API construída com FastAPI para gerenciar uma lista de convidados. A API inclui autenticação via Azure AD e suporte para adicionar, remover, listar e buscar convidados.

## Estrutura do Projeto


```project/
│
├── src/
│   ├── main.py
│   ├── auth/
│       ├── auth.py
│       ├── session_manager.py
│       ├── token_manager.py
│   ├── db/
│       ├── db_operations.py
│       ├── db_connection.py
│
├── .env
├── README.md
├── requirements.txt
```

### Instalação

1. Clone o repositório:

    ```sh
    git clone https://github.com/ailtonacr/api
    ```

2. Navegue até o diretório do projeto:

    ```sh
    cd api-fast
    ```

3. Crie e ative um ambiente virtual:

    ```sh
    python -m venv venv
    source venv/bin/activate  # No Windows use: venv\Scripts\activate
    ```

4. Instale as dependências:

    ```sh
    pip install -r requirements.txt
    ```

### Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

```
SESSION_SECRET_KEY=your_session_secret_key
DB_HOST=your_db_host
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_NAME=your_db_name
CLIENT_ID=your_azure_client_id
CLIENT_SECRET=your_azure_client_secret
TENANT_ID=your_azure_tenant_id
REDIRECT_URI=your_redirect_uri
SCOPE=your_scope
```
A variável `REDIRECT_URI` deve ter `https://{seu_host}/callback`. 
Lembre-se de configurar corretamente no seu Azure Ad a URI de redirecionamento e o escopo.

### Crie sua chave de sessão.

Esta chave será usada para configurar suas seções.

1. Execute o seguinte código para gerar uma chave de 32bytes (256bits).
    ```python
    import secrets
    
    secret_key = secrets.token_hex(32)
    print(secret_key)
    ```
2. Adicione ela na variável `SESSION_SECRET_KEY` no seu arquivo `.env` e também salve ela em um local seguro e que só você tenha acesso.

### Executando a Aplicação

1. Certifique-se de que o banco de dados MySQL está rodando e configurado corretamente.

2. Execute a aplicação:
   1. para dev:

    ```sh
    uvicorn api:app --host localhost --port 8000 --reload
    ```
   2. Para prd:
    ```sh
    uvicorn api:app --host 0.0.0.0 --port 8000
   ```

3. A API estará disponível em localmente em `http://localhost:8000`.

### Endpoints

- `GET /health`: Verifica se a API está funcionando.
- `GET /login`: Inicia o processo de login.
- `GET /callback`: Endpoint de callback para autenticação.
- `POST /add`: Adiciona um novo convidado. (Autenticado)
- `DELETE /remove`: Remove um convidado. (Autenticado)
- `GET /list`: Lista todos os convidados. (Autenticado)
- `GET /search`: Busca um convidado pelo nome. (Autenticado)
- `GET /docs`: Documentação Swagger UI. (Autenticado)

### Estrutura do Código

- `api.py`: Contém a configuração do FastAPI e as rotas principais.
- `auth.py`: Contém a lógica de autenticação com Azure AD.
- `session_manager.py`: Gerencia a sessão do usuário.
- `token_manager.py`: Responsável por obter o token de sessão do usuário.
- `db_connection.py`: Configura a conexão com o banco de dados.
- `db_operations.py`: Contém operações de banco de dados para adicionar, remover, listar e buscar convidados.

### Contribuindo

Se você encontrar problemas ou tiver sugestões para melhorar este projeto, sinta-se à vontade para abrir uma issue ou enviar um pull request.

### Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
