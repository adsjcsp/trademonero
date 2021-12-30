import sqlite3 as Banco


banco = Banco.Connection('./ext/db/bancodedados.db')
banco.cursor

f = open('./ext/db/schema.sql', 'r')
f.readline()
banco.execute(f)
banco.commit
