from fastapi import FastAPI
import psycopg
import os

app = FastAPI()


def get_conn():
    return psycopg.connect(os.environ["DATABASE_URL"], prepare_threshold=None)


@app.get("/api/health")
def health_check():
    return {"status": "ok"}


@app.get("/api/clients")
def get_clients():
    with get_conn() as conn:
        rows = conn.execute(
            "select id, nombre, telefono from clientes order by id"
        ).fetchall()
    return [{"id": r[0], "nombre": r[1], "telefono": r[2]} for r in rows]
