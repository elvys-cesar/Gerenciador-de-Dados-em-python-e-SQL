import sqlite3
import admin
import atualizar_dados
import livros

bliblioteca = sqlite3.connect('biblioteca.db')

online:str=input("Acessar como: administrador(A) ou Leitor(L): ")
while (online != 'L' and online!='A'):
    print("\nErro ao se conectar, tente novamente!\n")
    online:str=input("Acessar como: administrador(A) ou Leitor(L): ")


if online=='A':
    print("Faça login para ter acessor as ferramentas(ADM)")
    passl=input("login: ")
    passw=input("Senha: ")
    while (passl != 'adm' and passw != 'adm123' ):
        print("\nLogin ou senha incorreta! \nTente novamente!\n")
        passl = input("login: ")
        passw = input("Senha: ")

    else:
        if passl=='adm' and passw=='adm123':
            opc:int=input("Selecione a opção: (1): atualizar dados (2): Adicionar Livro: ")
            if opc=="1":
                atualizar_dados.atua_dados()
            if opc=="2":
                livros.novo_livro()


elif online=='L':
    user=input("Lista de livros(L), Acessar banco de usuarios(A) ou Criar novo usuario(C)")

    if user=='A':
        banco = sqlite3.connect('Banco_C.db')

        cursor = banco.cursor()

        # Display columns
        print('\nColumns in leitores table:')
        data = cursor.execute('''SELECT * FROM leitores''')
        for column in data.description:
            print(column[0])


        print('\nData in leitores table:')
        data = cursor.execute('''SELECT * FROM leitores''')

        for row in data:
            print(row)
            
    if user=='C':
        print("Insira os seus dados;")
        nome:str = input("nome: ")
        idade:int = input("idade: ")
        email:str = input("email: ")
        telefone:int = input("Telefone: ")

        while ((nome =="" or idade=="" or email=="" or telefone == "") and ('@hotmail.com' not in email or '@gmail.com' not in email)):
            print("\nAlgo deu errado, tenten novamente!\n")
            nome = input("nome: ")
            idade = input("idade: ")
            email = input("email: ")
            telefone = input("Telefone: ")

        banco = sqlite3.connect('Banco_C.db')

        cursor = banco.cursor()

        # inseri dados do novo cliente no banco
        cursor.execute("""
                INSERT INTO leitores(nome, idade, email, telefone)
                VALUES (?,?,?,?)
                """, (nome, idade, email, telefone))

        print('Dados registrados com sucesso!')

        # valida as alterações feitas
        banco.commit()
        cursor.execute("SELECT * FROM leitores")

        # desconectando...
        banco.close()


    if user=="L":
        banco = sqlite3.connect('Biblioteca.db')
        cursor=banco.cursor()

        print('\nColumns in livros table:')
        data = cursor.execute('''SELECT * FROM livros''')
        for column in data.description:
            print(column[0])

        print('\nData in livros table:')
        data = cursor.execute('''SELECT * FROM livros''')
        for row in data:
            print(row)