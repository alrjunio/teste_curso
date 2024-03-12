from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base


Base = declarative_base()

class CursoModel(Base): 
    __tablename__ = 'cursos'

    id: int = Column (Integer, primary_key=True, autoincrement=True)
    titulo: str = Column(String(100))
    aulas: int = Column(Integer)
    horas: int = Column(Integer)



def __repr__(self):
    return f"<Curso(titulo={self.titulo}, aulas={self.aulas}, horas={self.horas})>"

# Substitua 'mydatabase' pelo nome do seu banco de dados,
# 'user' pelo seu username e 'password' pela sua senha.
engine = create_engine('mysql+pymysql://root:Janela2412#@localhost/faculdade')

# Crie todas as tabelas definidas nos modelos Base
CursoModel.metadata.create_all(engine)
