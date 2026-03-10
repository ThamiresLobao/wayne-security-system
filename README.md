# 🦇 Wayne Security System

Sistema de **Controle de Segurança das Indústrias Wayne**, desenvolvido como aplicação web utilizando **Python, Flask, SQLite, HTML, CSS e JavaScript**.

O sistema permite gerenciar **usuários, recursos e atividades de segurança**, garantindo que apenas usuários autorizados possam acessar áreas restritas da empresa.

---

# 📌 Objetivo do Projeto

O objetivo deste projeto é desenvolver um sistema que permita:

- Autenticação de usuários
- Controle de acesso por nível
- Gerenciamento de recursos da empresa
- Registro de atividades de segurança
- Visualização de dados em um dashboard

O sistema simula a infraestrutura de segurança das **Indústrias Wayne**, empresa fictícia liderada por Bruce Wayne.

---

# 🚀 Tecnologias Utilizadas

## Backend
- Python
- Flask
- SQLite
- Bcrypt (criptografia de senha)

## Frontend
- HTML5
- CSS3
- JavaScript

---

# 🏗 Arquitetura do Sistema

O sistema segue o modelo **cliente-servidor**.
# 🦇 Wayne Security System

Sistema de **Controle de Segurança das Indústrias Wayne**, desenvolvido como aplicação web utilizando **Python, Flask, SQLite, HTML, CSS e JavaScript**.

O sistema permite gerenciar **usuários, recursos e atividades de segurança**, garantindo que apenas usuários autorizados possam acessar áreas restritas da empresa.

---

# 📌 Objetivo do Projeto

O objetivo deste projeto é desenvolver um sistema que permita:

- Autenticação de usuários
- Controle de acesso por nível
- Gerenciamento de recursos da empresa
- Registro de atividades de segurança
- Visualização de dados em um dashboard

O sistema simula a infraestrutura de segurança das **Indústrias Wayne**, empresa fictícia liderada por Bruce Wayne.

---

# 🚀 Tecnologias Utilizadas

## Backend
- Python
- Flask
- SQLite
- Bcrypt (criptografia de senha)

## Frontend
- HTML5
- CSS3
- JavaScript

---

# 🏗 Arquitetura do Sistema

O sistema segue o modelo **cliente-servidor**.
Frontend (HTML / CSS / JavaScript)
↓
Flask (Python Backend)
↓
SQLite Database

O Flask é responsável por:

- autenticação
- controle de sessão
- lógica do sistema
- comunicação com o banco de dados

---

# 📂 Estrutura do Projeto

O Flask é responsável por:

- autenticação
- controle de sessão
- lógica do sistema
- comunicação com o banco de dados

---

# 📂 Estrutura do Projeto
wayne-security-system/

app.py
create_db.py
database.db
README.md

templates/
│
├── login.html
├── cadastro.html
├── dashboard.html
├── usuarios.html
├── recursos.html
├── editar_recurso.html
└── logs.html

static/
│
├── css/
│ └── style.css
│
└── js/
└── dashboard.js

---

# 🔐 Controle de Acesso

O sistema possui **três tipos de usuários**:

| Tipo | Permissões |
|-----|------------|
Funcionário | Visualizar recursos |
Gerente | Gerenciar recursos |
Administrador | Gerenciar usuários e segurança |

Isso garante que **apenas usuários autorizados acessem áreas restritas**.

---

# 📊 Funcionalidades

### 🔑 Login Seguro
- autenticação com senha criptografada
- controle de sessão

### 👥 Gerenciamento de Usuários
Administradores podem:
- cadastrar usuários
- excluir usuários
- visualizar todos os funcionários

### 📦 Gerenciamento de Recursos
Permite:
- adicionar recursos
- editar recursos
- excluir recursos

### 📊 Dashboard
Apresenta dados importantes como:
- total de usuários
- total de recursos
- recursos ativos
- recursos em manutenção
- recursos inativos

### 🛡 Logs de Segurança
O sistema registra atividades importantes:

- login de usuário
- cadastro de usuários
- edição de recursos
- exclusão de usuários
- logout

---

# ⚙ Como Executar o Projeto

## 1️⃣ Clonar o repositório

```bash
git clone https://github.com/ThamiresLobao/wayne-security-system.git