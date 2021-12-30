def conexao_banco_de_dados():
    import sqlite3 as Banco
    from ext.config import pathdb
    
    #cria e conecta o banco de dados
    conn_banco = Banco.Connection(str(pathdb))
    conn_banco.cursor
    return conn_banco

def criar_tabelas():
    #abre um arquivo sql para criar as tabelas no banco de dados
   
    #abrir arquivo sql
    with open('./ext/db/schema.sql', 'r') as f:
        f.readline()
        
    return print(f)
        
        #db = conexao_banco_de_dados()
        #db.execute(f)
        #db.commit

