from sqlalchemy import Column, Integer, String, Enum, Float, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime
from enum import Enum as PyEnum
from banco_db.connect_db import engine


Base = declarative_base()

class TipoDeConta(PyEnum):
    Agente = 'Agente'
    Normal = 'Normal'

class CustomUser(Base):
    __tablename__ = 'custom_user'

    id = Column(Integer, primary_key=True, index=True)
    nome_completo = Column(String(30))
    email = Column(String, unique=True)
    codigo_do_agente = Column(Integer, nullable=True)
    tipo_de_conta = Column(Enum(TipoDeConta))
    saldo = Column(Float, nullable=True)
    numero_da_conta = Column(Integer, unique=True, nullable=True)
    numero_de_contacto = Column(Integer, nullable=True)


class Transferir(Base):
    __tablename__ = 'transferir'

    id = Column(Integer, primary_key=True, index=True)
    numero_da_conta = Column(Integer, nullable=True)
    montante = Column(Float)
    timestamp = Column(DateTime, default=datetime.now)
    is_approved = Column(Boolean, default=False)



class Levantar(Base):
    __tablename__ = 'levantar'

    id = Column(Integer, primary_key=True, index=True)
    codigo_do_agente = Column(Integer)
    montante = Column(Float)
    timestamp = Column(DateTime, default=datetime.now)
    is_approved = Column(Boolean, default=False)

class Deposito(Base):
    __tablename__ = 'deposito'

    id = Column(Integer, primary_key=True, index=True)
    numero_da_conta = Column(Integer, nullable=True)
    montante = Column(Float)
    timestamp = Column(DateTime, default=datetime.now)
    is_approved = Column(Boolean, default=False)


class YoolCount(Base):
    __tablename__ = 'yool_count'

    id = Column(Integer, primary_key=True, index=True)
    saldo = Column(Float, nullable=True)



Base.metadata.create_all(engine)