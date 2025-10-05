from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

DB = "database.db"

# Cria a tabela se não existir
def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS candidatos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    created DATETIME DEFAULT CURRENT_TIMESTAMP,
                    NomeReal TEXT,
                    NickDiscord TEXT,
                    Idade INTEGER,
                    Escolaridade TEXT,
                    Experiencia TEXT,
                    CargoDesejado TEXT
                )''')
    conn.commit()
    conn.close()

init_db()

# Página principal
@app.route("/")
def index():
    return render_template("index.html")

# Página de respostas
@app.route("/ver-respostas")
def respostas():
    return render_template("dados.html")

# Rota para receber os dados do formulário
@app.route("/enviar", methods=["POST"])
def enviar():
    data = request.json
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute('''INSERT INTO candidatos (NomeReal, NickDiscord, Idade, Escolaridade, Experiencia, CargoDesejado)
                 VALUES (?, ?, ?, ?, ?, ?)''',
              (data.get("NomeReal"),
               data.get("NickDiscord"),
               data.get("Idade"),
               data.get("Escolaridade"),
               data.get("Experiencia"),
               data.get("CargoDesejado")))
    conn.commit()
    conn.close()
    return jsonify({"success": True})

# Rota para listar respostas em JSON
@app.route("/respostas")
def get_respostas():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("SELECT * FROM candidatos ORDER BY created DESC")
    rows = [dict(row) for row in c.fetchall()]
    conn.close()
    return jsonify(rows)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
