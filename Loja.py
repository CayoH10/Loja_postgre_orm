import psycopg2
from datetime import date

conn = psycopg2.connect(
    dbname="Loja",
    user="postgres",
    password="ITjWH10c",
    host="localhost"
)
cur = conn.cursor()

cur.execute("INSERT INTO clientes(nome, email) VALUES (%s, %s) RETURNING id", ("ana", "ana@email.com"))
cliente1_id = cur.fetchone()[0]
cur.execute("INSERT INTO clientes(nome, email) VALUES (%s, %s) RETURNING id", ("Bruno", "bruno@email.com"))
cliente2_id = cur.fetchone()[0]

cur.execute("INSERT INTO pedidos(cliente_id, produto, data) VALUES (%s, %s, %s)", (cliente1_id, "Notebook", date.today()))
cur.execute("INSERT INTO pedidos(cliente_id, produto, data) VALUES (%s, %s, %s)", (cliente2_id, "Mouse", date.today()))
cur.execute("INSERT INTO pedidos(cliente_id, produto, data) VALUES (%s, %s, %s)", (cliente1_id, "Teclado", date.today()))

conn.commit()

cur.execute("""
    SELECT clientes.nome, pedidos.produto
    FROM pedidos
    JOIN clientes ON pedidos.cliente_id = clientes.id
""")
for row in cur.fetchall():
    print(row)

conn.close()