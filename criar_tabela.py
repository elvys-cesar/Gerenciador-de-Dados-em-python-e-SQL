import sqlite3

banco = sqlite3.connect('Banco_C.db')

cursor = banco.cursor()
cursor.execute("CREATE TABLE Funcionarios(nome text NOT NULL, idade integer NOT NULL, email text NOT NULL, telefone interger(11) NOT NULL, endereço text NOT NULL, cargo text NOT NULL)")


print('Dados registrados com sucesso!')
banco.commit()
cursor.execute("SELECT * FROM leitores")
banco.close()