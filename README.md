### Api Lista de convidados.


# FastAPI Guest List API

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

### Instalação

1. Clone o repositório:

    ```sh
    git clone https://github.com/ailtonacr/api-fast
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

### Executando a Aplicação

1. Certifique-se de que o banco de dados MySQL está rodando e configurado corretamente.

2. Execute a aplicação:

    ```sh
    uvicorn src.main:app --reload
    ```

3. A API estará disponível em `http://127.0.0.1:8000`.

### Endpoints

- `GET /health`: Verifica se a API está funcionando.
- `GET /login`: Inicia o processo de login.
- `GET /callback`: Endpoint de callback para autenticação.
- `POST /add`: Adiciona um novo convidado. (Autenticado)
- `DELETE /remove`: Remove um convidado. (Autenticado)
- `GET /list`: Lista todos os convidados. (Autenticado)
- `GET /search`: Busca um convidado pelo nome. (Autenticado)
- `GET /docs`: Documentação Swagger UI.

### Estrutura do Código

- `main.py`: Contém a configuração do FastAPI e as rotas principais.
- `auth.py`: Contém a lógica de autenticação com Azure AD.
- `session_manager.py`: Gerencia a sessão do usuário.
- `token_manager.py`: Responsável por obter o token de sessão do usuário.
- `db_connection.py`: Configura a conexão com o banco de dados.
- `db_operations.py`: Contém operações de banco de dados para adicionar, remover, listar e buscar convidados.

### Contribuindo

Se você encontrar problemas ou tiver sugestões para melhorar este projeto, sinta-se à vontade para abrir uma issue ou enviar um pull request.

### Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
