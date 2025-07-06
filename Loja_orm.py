from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, Session
from datetime import date

Base = declarative_base()

class Cliente(Base):
    __tablename__ = 'clientes'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    email = Column(String)
    pedidos = relationship("Pedido", back_populates="cliente")

class Pedido(Base):
    __tablename__ = 'pedidos'
    id = Column(Integer, primary_key=True)
    cliente_id = Column(Integer, ForeignKey('clientes.id'))
    produto = Column(String)
    data = Column(Date)
    cliente = relationship("Cliente", back_populates="pedidos")

engine = create_engine("postgresql://postgres:ITjWH10c@localhost/Loja")
Base.metadata.create_all(engine)

with Session(engine) as session:
    session.query(Pedido).delete()
    session.query(Cliente).delete()
    session.commit()

    ana = Cliente(nome="Ana", email="ana@email.com")
    bruno = Cliente(nome="Bruno", email="bruno@email.com")

    session.add_all([ana, bruno])
    session.commit()

    p1 = Pedido(produto="Notebook", data=date.today(), cliente=ana)
    p2 = Pedido(produto="Mouse", data=date.today(), cliente=bruno)
    p3 = Pedido(produto="Teclado", data=date.today(), cliente=ana)

    session.add_all([p1, p2, p3])
    session.commit()

    resultados = session.query(Cliente.nome, Pedido.produto).join(Pedido).all()
    for nome, produto in resultados:
        print(nome, "-", produto)