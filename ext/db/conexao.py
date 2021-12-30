import sqlite3 as Banco

def conectar():
    #cria e conecta o banco de dados
    banco = Banco.Connection('./ext/db/bancodedados.db')
    banco.cursor
    return banco

def criar_tabelas():
    #abre um arquivo sql para criar as tabelas no banco de dados
   
    #abrir arquivo sql
    with open('./ext/db/schema.sql', 'r') as f:
        sql = f.readlines()
        banco = Banco.Cursor
        banco.executescript(sql)
        banco.close
        
   
