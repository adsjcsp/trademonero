from datetime import datetime as hoje

from sqlalchemy import (create_engine, Column, MetaData,
                        Table, Integer, Date, String)

engine = create_engine('sqlite:/ext/db/basededados.db',
                       echo=False)

metadata = MetaData(bind=engine)

user_table = Table('usuarios',
                    Column('id', Integer, primary_key=True),
                    Column('nome', String(40), index=True),
                    Column('idade', Integer, nullable=False),
                    Column('senha', String),
                    Column('Criado_em', Date, default=hoje.now),
                    Column('atualizado_em', Date,
                           default=hoje.now,
                           onupdate=hoje.now))

MetaData.create_all