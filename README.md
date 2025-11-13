# 🚀 Auth API -- Programa.AI

API de autenticação desenvolvida como parte do curso de **AppSec da
Programa AI**.\
Este projeto utiliza **Flask**, **Flask-Migrate** e **SQLAlchemy** para
gerenciamento de banco de dados e migrações.

------------------------------------------------------------------------

## 📦 Tecnologias Utilizadas

-   Python 3.x\
-   Flask\
-   Flask SQLAlchemy\
-   Flask Migrate\
-   SQLite (padrão) ou outro banco configurado\
-   Virtualenv (recomendado)

------------------------------------------------------------------------

## ▶️ Como rodar o projeto

### 1️⃣ Clone o repositório

``` bash
git clone https://github.com/seu-usuario/auth-api-programa-ai.git
cd auth-api-programa-ai
```

### 2️⃣ Crie e ative o ambiente virtual

**Linux/macOS**

``` bash
python3 -m venv venv
source venv/bin/activate
```

**Windows**

``` bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Instale as dependências

``` bash
pip install -r requirements.txt
```

------------------------------------------------------------------------

## 🗃️ Configuração do Banco de Dados (Flask-Migrate)

### 1. Inicializar as migrações

``` bash
flask db init
```

### 2. Criar a migração inicial

``` bash
flask db migrate -m "init: users"
```

### 3. Aplicar as migrações

``` bash
flask db upgrade
```

------------------------------------------------------------------------

## ▶️ Executando a API

``` bash
flask run
```

API disponível em:

    http://127.0.0.1:5000

------------------------------------------------------------------------

## 🧩 Estrutura Geral do Projeto

    auth-api/
    │── app/
    │   ├── models/
    │   ├── routes/
    │   ├── __init__.py
    │   ├── config.py
    │── migrations/
    │── venv/
    │── requirements.txt
    │── README.md
    └── run.py / app.py

------------------------------------------------------------------------

## 📌 Variável FLASK_APP

``` bash
export FLASK_APP=app
```

Windows:

``` bash
set FLASK_APP=app
```

