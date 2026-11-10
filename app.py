import sqlite3
from flask import Flask, request

app = Flask(__name__)

# Função que cria o banco e a tabela de testes
def init_db():
    conn = sqlite3.connect(':memory:', check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")
    cursor.execute("INSERT OR IGNORE INTO users (id, username, password) VALUES (1, 'admin', 'admin123')")
    conn.commit()
    return conn

# Inicializa o banco globalmente com a flag de segurança de thread ajustada
db_conn = init_db()

@app.route('/')
def home():
    return '''
        <h2>Login de Teste (Vulnerável)</h2>
        <form method="POST" action="/login">
            Usuário: <input type="text" name="username"><br>
            Senha: <input type="password" name="password"><br>
            <input type="submit" value="Entrar">
        </form>
    '''

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    cursor = db_conn.cursor()
    
    # VULNERABILIDADE CRÍTICA: Concatenação direta de strings na query SQL (SQL Injection)
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    print(f"[DEBUG Query Executada]: {query}")
    
    try:
        cursor.execute(query)
        user = cursor.fetchone()
        if user:
            return f"<h1>Bem-vindo, {user[1]}! Login bem-sucedido.</h1>"
        else:
            return "<h1>Credenciais inválidas!</h1>"
    except Exception as e:
        return f"<h1>Erro no banco: {e}</h1>"

if __name__ == '__main__':
    app.run(debug=True, port=5000)
    