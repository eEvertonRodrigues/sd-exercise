# Primeira Prática — Sistemas Distribuídos (Docker)

Aplicação web Flask que contabiliza o número de acessos, usando Redis para armazenar o contador. Containerizada com Docker e orquestrada com Docker Compose.

**Arquitetura:** Navegador → Flask/App → Redis → Volume

## Estrutura do projeto

```
.
├── app/                 # Core da aplicação (código-fonte)
│   ├── app.py           # App Flask: contador de acessos, /guests e /guests/data
│   └── requirements.txt # Dependências (flask, redis)
├── docs/                # Resolução da prática:
│                        #   texto formalizador, respostas das questões
│                        #   e vídeo explicativo
├── Dockerfile           # Build da imagem da aplicação
├── docker-compose.yml   # Orquestração: app + redis, rede compartilhada,
│                        #   porta 5050 e volume de persistência
├── load.sh              # Scriptzinho que fica fazendo requisições
│                        #   constantemente (Ctrl+C para parar)
└── Primeira Prática-2.pdf  # Enunciado da atividade
```

## Como executar

```bash
docker compose up -d --build
```

Acesse: http://localhost:5050

## Rotas

| Rota | Descrição |
|---|---|
| `/` | Contador de acessos — registra cada visita no Redis |
| `/guests` | Lista em tempo real da chegada de cada visitante (atualiza a cada 1s) |
| `/guests/data` | JSON com a lista de chegadas (usado pelo polling da página) |

## Gerador de requisições

```bash
./load.sh
```

Fica batendo em `/` a cada 0.5s até você dar **Ctrl+C** — abra `/guests` no navegador ao mesmo tempo para ver as chegadas em tempo real.

## Persistência

O Redis usa o volume nomeado `redis-data`: contador e convidados sobrevivem a `docker compose down` / `up`. Nunca use `down -v` se quiser preservar os dados.

---

# First Practice — Distributed Systems (Docker)

A Flask web app that counts the number of visits, using Redis to store the counter. Containerized with Docker and orchestrated with Docker Compose.

**Architecture:** Browser → Flask/App → Redis → Volume

## Project structure

```
.
├── app/                 # Application core (source code)
│   ├── app.py           # Flask app: visit counter, /guests and /guests/data
│   └── requirements.txt # Dependencies (flask, redis)
├── docs/                # Practice solution:
│                        #   formal text, answers to the questions
│                        #   and explanatory video
├── Dockerfile           # Builds the application image
├── docker-compose.yml   # Orchestration: app + redis, shared network,
│                        #   port 5050 and persistence volume
├── load.sh              # Little script that keeps making
│                        #   constant requests (Ctrl+C to stop)
└── Primeira Prática-2.pdf  # Assignment statement
```

## How to run

```bash
docker compose up -d --build
```

Access: http://localhost:5050

## Routes

| Route | Description |
|---|---|
| `/` | Visit counter — records each visit in Redis |
| `/guests` | Real-time list of every visitor's arrival (updates every 1s) |
| `/guests/data` | JSON with the arrival list (consumed by the page's polling) |

## Request generator

```bash
./load.sh
```

Hits `/` every 0.5s until you press **Ctrl+C** — open `/guests` in your browser at the same time to see arrivals in real time.

## Persistence

Redis uses the named volume `redis-data`: counter and guests survive `docker compose down` / `up`. Never use `down -v` if you want to keep the data.
