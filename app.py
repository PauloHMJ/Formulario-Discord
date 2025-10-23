from flask import Flask, render_template, request, jsonify
import mysql.connector
from datetime import datetime, timedelta, timezone

app = Flask(__name__)

# --- Configurações do banco MySQL ---
DB_WRITE = {
    "host": "localhost",
    "user": "program_user", 
    "password": "6BvemY2Q4cMoS",
    "database": "discord_staff_db"
}

DB_READ = {
    "host": "localhost",
    "user": "program_visualizer",
    "password": "L465H92xpXVwf",
    "database": "discord_staff_db"
}

BRASILIA = timezone(timedelta(hours=-3))

# --- Criação da tabela se não existir ---
def init_db():
    conn = mysql.connector.connect(**DB_WRITE)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS candidatos (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    created VARCHAR(25),
                    NomeReal VARCHAR(100),
                    NickDiscord VARCHAR(100),
                    Idade INT,
                    Escolaridade VARCHAR(100),
                    Experiencia TEXT,
                    CargoDesejado VARCHAR(100),
                    Atividade TEXT
                )''')
    conn.commit()
    conn.close()

init_db()

# --- Página principal (formulário) ---
@app.route("/")
def index():
    return render_template("index.html")

# --- Página de visualização das respostas ---
@app.route("/ver-respostas")
def respostas():
    return render_template("dados.html")

# --- Verificação de nick duplicado ---
@app.route("/verificar-nick", methods=["POST"])
def verificar_nick():
    data = request.json
    nick = data.get("NickDiscord")

    conn = mysql.connector.connect(**DB_READ)
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM candidatos WHERE NickDiscord = %s", (nick,))
    resultado = c.fetchone()[0]
    conn.close()

    if resultado > 0:
        return jsonify({"existe": True})
    return jsonify({"existe": False})

# --- Enviar dados ---
@app.route("/enviar", methods=["POST"])
def enviar():
    data = request.json
    data_criacao = datetime.now(BRASILIA).strftime("%d/%m/%Y %H:%M:%S")

    conn = mysql.connector.connect(**DB_WRITE)
    c = conn.cursor()
    sql = '''INSERT INTO candidatos 
             (created, NomeReal, NickDiscord, Idade, Escolaridade, Experiencia, CargoDesejado, Atividade)
             VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'''
    valores = (
        data_criacao,
        data.get("NomeReal"),
        data.get("NickDiscord"),
        data.get("Idade"),
        data.get("Escolaridade"),
        data.get("Experiencia"),
        data.get("CargoDesejado"),
        data.get("AtividadeArea")
    )
    c.execute(sql, valores)
    conn.commit()
    conn.close()

    return jsonify({"success": True})


@app.route("/respostas")
def get_respostas():
    conn = mysql.connector.connect(**DB_READ)
    c = conn.cursor(dictionary=True)
    c.execute("SELECT * FROM candidatos ORDER BY id DESC")
    rows = c.fetchall()
    conn.close()
    return jsonify(rows)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
