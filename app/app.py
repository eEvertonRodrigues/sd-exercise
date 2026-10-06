from flask import Flask, jsonify
import redis
import os
from datetime import datetime

app = Flask(__name__)

# Nome do host do Redis
redis_host = os.getenv("REDIS_HOST", "localhost")

# Conexão com o Redis
r = redis.Redis(
    host=redis_host,
    port=6379,
    decode_responses=True
)

@app.route("/")
def home():
    # Incrementa o número de acessos
    acessos = r.incr("acessos")

    # Registra a chegada do visitante (mais recente no topo, máx. 100)
    r.lpush("guests", f"{datetime.now().strftime('%H:%M:%S.%f')[:-3]} · acesso #{acessos}")
    r.ltrim("guests", 0, 99)

    return f"""
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <title>Prática Docker</title>
    </head>
    <body>
        <h1>Olá, Docker C!</h1>
        <p>Número de acessos: {acessos}</p>
    </body>
    </html>
    """

@app.route("/guests")
def guests():
    return """
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <title>Guests - Prática Docker</title>
        <script>
            async function atualizar() {
                const resp = await fetch("/guests/data");
                const lista = await resp.json();
                document.getElementById("lista").innerHTML =
                    lista.map(g => "<li>" + g + "</li>").join("");
            }
            atualizar();
            setInterval(atualizar, 1000);
        </script>
    </head>
    <body>
        <h1>Convidados em tempo real</h1>
        <ul id="lista"></ul>
        <p><a href="/">Voltar</a></p>
    </body>
    </html>
    """

@app.route("/guests/data")
def guests_data():
    return jsonify(r.lrange("guests", 0, -1))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)
