from flask import Flask, render_template, request, redirect, session
import sqlite3
import bcrypt

app = Flask(__name__)
app.secret_key = "wayne_secret"


# ---------------- CONEXÃO BANCO ----------------
def conectar_db():
    conn = sqlite3.connect("database.db", timeout=10)
    conn.row_factory = sqlite3.Row
    return conn


# ---------------- LOG DO SISTEMA ----------------
def registrar_log(usuario, acao):

    conn = conectar_db()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO logs (usuario,acao)
    VALUES (?,?)
    """, (usuario, acao))

    conn.commit()
    conn.close()


# ---------------- CONTROLE DE ACESSO ----------------
def verificar_permissao(tipos_permitidos):

    if "usuario" not in session:
        return False

    if session["tipo"] not in tipos_permitidos:
        return False

    return True


# ---------------- LOGIN ----------------
@app.route("/")
def login():
    return render_template("login.html")


@app.route("/auth", methods=["POST"])
def auth():

    email = request.form.get("email")
    senha = request.form.get("senha").encode("utf-8")

    conn = conectar_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM usuarios WHERE email=?", (email,))
    user = cursor.fetchone()

    conn.close()

    if user:

        senha_db = user["senha"]

        if isinstance(senha_db, str):
            senha_db = senha_db.encode("utf-8")

        if bcrypt.checkpw(senha, senha_db):

            session["usuario"] = user["nome"]
            session["tipo"] = user["tipo"]
            session["id"] = user["id"]

            registrar_log(user["nome"], "Fez login no sistema")

            return redirect("/dashboard")

    return "Login inválido"


# ---------------- PAGINA DE CADASTRO ----------------
@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")


# ---------------- CADASTRAR USUARIO PUBLICO ----------------
@app.route("/registrar", methods=["POST"])
def registrar():

    nome = request.form.get("nome")
    cpf = request.form.get("cpf")
    cargo = request.form.get("cargo")
    email = request.form.get("email")
    senha = request.form.get("senha")

    tipo = "funcionario"

    senha_hash = bcrypt.hashpw(senha.encode("utf-8"), bcrypt.gensalt())

    conn = conectar_db()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO usuarios (nome,cpf,cargo,email,senha,tipo)
    VALUES (?,?,?,?,?,?)
    """, (nome, cpf, cargo, email, senha_hash, tipo))

    conn.commit()
    conn.close()

    return redirect("/")


# ---------------- DASHBOARD ----------------
@app.route("/dashboard")
def dashboard():

    if "usuario" not in session:
        return redirect("/")

    conn = conectar_db()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM recursos")
    total_recursos = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM usuarios")
    total_users = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM recursos WHERE status='Ativo'")
    ativos = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM recursos WHERE status='Manutenção'")
    manutencao = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM recursos WHERE status='Inativo'")
    inativos = cursor.fetchone()[0]

    conn.close()

    return render_template(
        "dashboard.html",
        usuario=session["usuario"],
        total_recursos=total_recursos,
        total_users=total_users,
        ativos=ativos,
        manutencao=manutencao,
        inativos=inativos
    )


# ---------------- LISTAR RECURSOS ----------------
@app.route("/recursos")
def recursos():

    if "usuario" not in session:
        return redirect("/")

    conn = conectar_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM recursos")
    recursos = cursor.fetchall()

    conn.close()

    return render_template("recursos.html", recursos=recursos)


# ---------------- ADICIONAR RECURSO ----------------
@app.route("/add_recurso", methods=["POST"])
def add_recurso():

    if not verificar_permissao(["admin","gerente"]):
        return "🚫 Apenas gerentes ou administradores podem adicionar recursos."

    nome = request.form.get("nome")
    tipo = request.form.get("tipo")
    status = request.form.get("status")

    conn = conectar_db()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO recursos (nome,tipo,status) VALUES (?,?,?)",
        (nome, tipo, status)
    )

    conn.commit()

    registrar_log(session["usuario"], f"Adicionou recurso {nome}")

    conn.close()

    return redirect("/recursos")


# ---------------- EDITAR RECURSO ----------------
@app.route("/editar_recurso/<id>")
def editar_recurso(id):

    if not verificar_permissao(["admin","gerente"]):
        return "🚫 Apenas gerentes ou administradores podem editar recursos."

    conn = conectar_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM recursos WHERE id=?", (id,))
    recurso = cursor.fetchone()

    conn.close()

    return render_template("editar_recurso.html", recurso=recurso)


# ---------------- ATUALIZAR RECURSO ----------------
@app.route("/update_recurso/<id>", methods=["POST"])
def update_recurso(id):

    if not verificar_permissao(["admin","gerente"]):
        return "🚫 Apenas gerentes ou administradores podem editar recursos."

    nome = request.form.get("nome")
    tipo = request.form.get("tipo")
    status = request.form.get("status")

    conn = conectar_db()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE recursos
    SET nome=?, tipo=?, status=?
    WHERE id=?
    """, (nome, tipo, status, id))

    conn.commit()

    registrar_log(session["usuario"], f"Editou recurso {nome}")

    conn.close()

    return redirect("/recursos")


# ---------------- USUÁRIOS ----------------
@app.route("/usuarios")
def usuarios():

    if not verificar_permissao(["admin"]):
        return "🚫 Acesso restrito a administradores."

    conn = conectar_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()

    conn.close()

    return render_template("usuarios.html", usuarios=usuarios)


# ---------------- LOGS DE SEGURANÇA ----------------
@app.route("/logs")
def logs():

    if not verificar_permissao(["admin","gerente"]):
        return "🚫 Acesso restrito."

    conn = conectar_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM logs ORDER BY data DESC")
    logs = cursor.fetchall()

    conn.close()

    return render_template("logs.html", logs=logs)


# ---------------- CADASTRAR USUARIO PELO ADMIN ----------------
@app.route("/add_usuario", methods=["POST"])
def add_usuario():

    if not verificar_permissao(["admin"]):
        return "🚫 Apenas administradores podem cadastrar usuários."

    nome = request.form.get("nome")
    cpf = request.form.get("cpf")
    cargo = request.form.get("cargo")
    email = request.form.get("email")
    senha = request.form.get("senha")
    tipo = request.form.get("tipo")

    senha_hash = bcrypt.hashpw(senha.encode("utf-8"), bcrypt.gensalt())

    try:

        conn = conectar_db()
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO usuarios (nome,cpf,cargo,email,senha,tipo)
        VALUES (?,?,?,?,?,?)
        """, (nome, cpf, cargo, email, senha_hash, tipo))

        conn.commit()

        registrar_log(session["usuario"], f"Cadastrou o usuário {nome}")

        conn.close()

    except sqlite3.IntegrityError:

        conn.close()
        return "⚠ Este email já está cadastrado."

    return redirect("/usuarios")


# ---------------- EXCLUIR USUARIO ----------------
@app.route("/delete_usuario/<id>")
def delete_usuario(id):

    if not verificar_permissao(["admin"]):
        return "🚫 Apenas administradores podem excluir usuários."

    conn = conectar_db()
    cursor = conn.cursor()

    if str(session["id"]) == id:
        conn.close()
        return "Administrador não pode excluir o próprio usuário."

    cursor.execute("SELECT tipo FROM usuarios WHERE id=?", (id,))
    user = cursor.fetchone()

    if user and user["tipo"] == "admin":
        conn.close()
        return "Não é permitido excluir outro administrador."

    cursor.execute("DELETE FROM usuarios WHERE id=?", (id,))
    conn.commit()

    registrar_log(session["usuario"], f"Excluiu usuário ID {id}")

    conn.close()

    return redirect("/usuarios")


# ---------------- LOGOUT ----------------
@app.route("/logout")
def logout():

    if "usuario" in session:
        registrar_log(session["usuario"], "Saiu do sistema")

    session.clear()

    return redirect("/")


# ---------------- RODAR SISTEMA ----------------
if __name__ == "__main__":
    app.run(debug=True)