from  datetime import datetime as hoje

from sqlalchemy import (create_engine, MetaData, Column, 
                        Table, Integer, String, Datetime)

engine = create_engine('sqlite:/ext/db/basededados.db', 
                       echo=False)

metafata = MetaData(bind=engine)

user_tabler = Table('usuarios', 
                    metadata, 
                    Column('id', Integer, primary_key=True),
                    Column('nome', String(40), index=True ),
                    Column('idade', Integer, nullable=False),
                    Columun('senha', String),
                    Column('Criado_em', Datetime, default=hoje.now),
                    Column('atualizado_em', Datetime, default=hoje.now, onupdate=hoje.now))

MetaData.create_all