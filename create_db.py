import sqlite3
import bcrypt

conn = sqlite3.connect("database.db")
cursor = conn.cursor()


# ---------------- TABELA USUARIOS ----------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
id INTEGER PRIMARY KEY AUTOINCREMENT,
nome TEXT,
cpf TEXT UNIQUE,
cargo TEXT,
email TEXT UNIQUE,
senha BLOB,
tipo TEXT
)
""")


# ---------------- TABELA RECURSOS ----------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS recursos(
id INTEGER PRIMARY KEY AUTOINCREMENT,
nome TEXT,
tipo TEXT,
status TEXT
)
""")


# ---------------- TABELA LOGS ----------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS logs(
id INTEGER PRIMARY KEY AUTOINCREMENT,
usuario TEXT,
acao TEXT,
data TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")


# ---------------- CRIAR ADMIN ----------------

cursor.execute("SELECT * FROM usuarios WHERE email=?", ("bruce@wayne.com",))
admin = cursor.fetchone()

if not admin:

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

    print("Admin criado com sucesso.")

else:
    print("Admin já existe.")


conn.commit()
conn.close()

print("Banco criado com sucesso.")
print("Login admin:")
print("Email: bruce@wayne.com")
print("Senha: 123")