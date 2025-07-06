Este projeto demonstra a criação e manipulação de um banco de dados relacional utilizando o PostgreSQL, com duas abordagens distintas:

SQL puro: utilizando a biblioteca psycopg2 para executar comandos diretamente.

ORM (Object-Relational Mapping): utilizando a biblioteca SQLAlchemy para abstrair a camada de acesso ao banco.

Estrutura do banco:
Clientes

id, nome, email

Pedidos

id, cliente_id (chave estrangeira), produto, data

Funcionalidades:
Criação das tabelas com relacionamento (1:N).

Inserção de dados (clientes e pedidos).

Consulta com JOIN para exibir o nome do cliente e o produto comprado.