import sqlite3
import livros

def atua_dados():
    banco = sqlite3.connect("Banco_C.db")

    cursor = banco.cursor()
    alterar=input("Alterar dados de usuario(A)\nVisualizar tabela de funcionarios(F)\nAlterar Id de livro(B)\nAcrecentar colunas(C)\n: ")

    if alterar=="A":
        A:str= input("Nome do usuario a ser alterado: ")

        cursor.execute(f"SELECT * FROM leitores WHERE nome='{A}' ")

        rows = cursor.fetchall()
        print("Leitor encontrado: ")
        for row in rows:
            print(row)

        B = input("Coluna a ser alterada: ")
        C = input("Valor atribuido: ")
        #esse codigo vai atualizar os dados
        cursor.execute(f"""UPDATE leitores SET '{B}' = '{C}' WHERE nome = '{A}' """)
    elif alterar=='B':
        livros.id_livro()
    elif alterar=='C':
        print("AVISO! AO ACRECENTAR UMA COLUNA \nNÃO É POSSIVEL REMOVELA")
        A=input("Nome da coluna: ")
        cursor.execute(f'''
        ALTER TABLE leitores
        ADD COLUMN '{A}' INTERGER;
        ''')

        cursor.execute("SELECT * FROM leitores")
        print(cursor.fetchall())
        banco.commit()

    elif alterar=='F':
        

        # Display columns
        print('\nDados da tabela funcionarios:')
        data = cursor.execute('''SELECT * FROM Funcionarios''')

        for row in data:
            print(row)

        k=input("\nAdicionar novo funcionario(A)\nDeletar funcionario(D)\nVoltar as opções(V)")
        banco = sqlite3.connect("Banco_C.db")
        if k=='A':
            print("Insira os seus dados;")
            nome: str = input("nome: ")
            idade: int = input("idade: ")
            email: str = input("email: ")
            telefone: int = input("Telefone: ")
            endereco = input("Endereço: ")
            cargo: str = input("Cargo atribuido: ")
            while ((nome == "" or idade == "" or email == "" or telefone == "" or endereco =="" or cargo=="") and (
                    '@hotmail.com' not in email or '@gmail.com' not in email)):
                print("\nAlgo deu errado, tenten novamente!\n")
                nome = input("nome: ")
                idade = input("idade: ")
                email = input("email: ")
                telefone = input("Telefone: ")
                endereco = input("Endereço: ")
                cargo: str = input("Cargo atribuido: ")


            banco = sqlite3.connect("Banco_C.db")
            cursor = banco.cursor()
            # inseri dados do novo cliente no banco
            cursor.execute("""
                    INSERT INTO Funcionarios(nome, idade, email, telefone, endereço, cargo)
                    VALUES (?,?,?,?,?,?)
                    """, (nome, idade, email, telefone, endereco, cargo))
        

            banco.commit()
            cursor.execute('''SELECT * FROM Funcionarios''')
            for row in data:
                print(row)
            # desconectando...


            print('Dados registrados com sucesso!')

            # valida as alterações feitas
            banco.commit()
            cursor.execute("SELECT * FROM Funcionarios")

            # desconectando...
            banco.close()
            
            print('Dados registrados com sucesso!')
        elif k=='V':
            atua_dados()
        elif k=='D':
            cursor.execute('''DROP TABLE Funcionarios WHERE nome, idade, email, telefone, enderenço, cargo''')

            banco.commit()
            banco.close()
            print("OPERAÇÃO COMCLUIDA COM ÊXITO!")
    else:
        print("\nERRO NA ALTENTICAÇÃO, TENTE NOVAMENTE.\n")
        atua_dados()

    #valida as alterações feitas


