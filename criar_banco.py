import sqlite3
import bcrypt

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# TABELA USUARIOS
cursor.execute("""
CREATE TABLE usuarios (
id INTEGER PRIMARY KEY AUTOINCREMENT,
nome TEXT,
cpf TEXT,
cargo TEXT,
email TEXT UNIQUE,
senha BLOB,
tipo TEXT
)
""")

# TABELA RECURSOS
cursor.execute("""
CREATE TABLE recursos (
id INTEGER PRIMARY KEY AUTOINCREMENT,
nome TEXT,
tipo TEXT,
status TEXT
)
""")

# TABELA LOGS
cursor.execute("""
CREATE TABLE logs (
id INTEGER PRIMARY KEY AUTOINCREMENT,
usuario TEXT,
acao TEXT,
data TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

# CRIAR ADMIN
senha = "123"
senha_hash = bcrypt.hashpw(senha.encode("utf-8"), bcrypt.gensalt())

cursor.execute("""
INSERT INTO usuarios (nome,cpf,cargo,email,senha,tipo)
VALUES (?,?,?,?,?,?)
""", (
"Bruce Wayne",
"00000000000",
"CEO",
"bruce@wayne.com",
senha_hash,
"admin"
))

conn.commit()
conn.close()

print("Banco criado com sucesso")
print("Login admin:")
print("Email: bruce@wayne.com")
print("Senha: 123")