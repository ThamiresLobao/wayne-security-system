# 🦇 Wayne Security System

Sistema de **Controle de Segurança das Indústrias Wayne**, desenvolvido como aplicação web utilizando **Python, Flask, SQLite, HTML, CSS e JavaScript**.

O sistema permite gerenciar **usuários, recursos e atividades de segurança**, garantindo que apenas usuários autorizados possam acessar áreas restritas da empresa.

---

# 📌 Objetivo do Projeto

O objetivo deste projeto é desenvolver um sistema que permita:

- autenticação de usuários
- controle de acesso por nível
- gerenciamento de recursos da empresa
- registro de atividades de segurança
- visualização de dados em um dashboard

O sistema simula a infraestrutura de segurança das **Indústrias Wayne**, empresa fictícia liderada por **Bruce Wayne**.

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
wayne_security/

app.py
create_db.py
database.db
README.md
.gitignore

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

Isso garante que **apenas usuários autorizados acessem áreas restritas do sistema**.

---

# 📊 Funcionalidades do Sistema

### 🔑 Login Seguro

- autenticação com senha criptografada
- controle de sessão

---

### 👥 Gerenciamento de Usuários

Administradores podem:

- cadastrar usuários
- excluir usuários
- visualizar todos os funcionários

---

### 📦 Gerenciamento de Recursos

Permite:

- adicionar recursos
- editar recursos
- atualizar status dos recursos

Exemplos de recursos:

- equipamentos
- veículos
- sistemas internos

---

### 📊 Dashboard

Apresenta dados importantes do sistema:

- total de usuários
- total de recursos
- recursos ativos
- recursos em manutenção
- recursos inativos

---

### 🛡 Logs de Segurança

O sistema registra atividades importantes como:

- login de usuário
- cadastro de usuários
- edição de recursos
- exclusão de usuários
- logout do sistema

Isso permite **monitorar todas as atividades realizadas no sistema**.

---

# 🗄 Estrutura do Banco de Dados

O sistema utiliza **SQLite** com três tabelas principais.

## Tabela: usuarios

| Campo | Descrição |
|------|-----------|
id | Identificador do usuário |
nome | Nome do usuário |
cpf | CPF |
cargo | Cargo |
email | Email de login |
senha | Senha criptografada |
tipo | Tipo de acesso |

---

## Tabela: recursos

| Campo | Descrição |
|------|-----------|
id | Identificador |
nome | Nome do recurso |
tipo | Tipo do recurso |
status | Status do recurso |

---

## Tabela: logs

| Campo | Descrição |
|------|-----------|
id | Identificador |
usuario | Usuário que realizou a ação |
acao | Ação realizada |
data | Data do evento |

---

# 🛡 Segurança Implementada

O sistema possui diversas medidas de segurança:

- criptografia de senha utilizando **bcrypt**
- controle de sessão com **Flask**
- controle de acesso por tipo de usuário
- registro de logs de atividades
- restrição de acesso a áreas administrativas

---

# ⚙ Como Executar o Projeto

## 1️⃣ Clonar o repositório

```bash
git clone https://github.com/ThamiresLobao/wayne-security-system.git

# 👩‍💻 Autora

Projeto desenvolvido por:

**Thamires Lobão**

Estudante de Programação Full Stack IA

# 🎓 Finalidade do Projeto

Este sistema foi desenvolvido como **projeto acadêmico**, com o objetivo de demonstrar a criação de uma aplicação web completa com:
- backend em Python utilizando Flask
- autenticação e controle de acesso
- gerenciamento de usuários e recursos
- integração com banco de dados
- implementação de medidas básicas de segurança

O projeto simula o sistema de segurança das **Indústrias Wayne**, empresa fictícia do universo Batman.

Projeto desenvolvido em 2026 utilizando Python, Flask e SQLite.