import sqlite3

import livros


def admintools():
    banco = sqlite3.connect("Banco_C.db")
    cursor = banco.cursor()

    print("Bem vindo a ferramenta de administração")
    fazer:str=input("Quais dados deseja atualizar: \nmodificar dados(M)\nDELETAR(D)")
    if fazer=='D':
        try:
        #aqui onde o adm tem a possibilidade de excluir dados


            cursor.execute('''DROP TABLE leitores''')

            banco.commit()
            banco.close()
            print("OPERAÇÃO COMCLUIDA COM ÊXITO!")
        except sqlite3.Error as erro:
            print("ERRO AO PROCESSIGA COM A OPERÇÂO!", erro)
    elif fazer=='M':
        livros = sqlite3.connect("Biblioteca.db")
        cursor=livros.cursor()
        cursor.execute("UPDATE livros SET nome = 'Pecados intocaveis' WHERE id = '1' """)
        livros.commit()
        cursor.execute("SELECT * FROM livros")
        print(cursor.fetchall())