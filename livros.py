import sqlite3

banco = sqlite3.connect('biblioteca.db')
cursor = banco.cursor()
def id_livro():
    id: str
    a: str
    print("As alterações disponiveis são apenas para ID,\nO id vai ajudar a localizar a pessoa com quem o livro se encontra\nCaso o ID seja nulo, significa que o livro se encontra disponivel.")
    nome: str = input("digite o nome do livro: ")
    cursor.execute(f"SELECT * FROM livros WHERE nome='{nome}' ")

    rows = cursor.fetchall()
    print("livro encontrado: ")
    for row in rows:
        print(row)

    a: str = input("Altere o ID: ")
    if a == "0" or not a:
        id: str = "00"
        status = "DISPONIVEL"
    else:
        status = "INDISPONIVEL"
        id = a
    #esse codigo vai atualizar os dados
    cursor.execute(f"""UPDATE livros SET ID = '{id}' WHERE nome = '{nome}' """)
    cursor.execute(f"""UPDATE livros SET status = '{status}' WHERE nome = '{nome}' """)

    banco.commit()
    cursor.execute("SELECT * FROM livros")
    print(cursor.fetchall())
def novo_livro():
    global id
    nome: str
    status: str
    verifique: str = input("Nome do livro: ")
    id = input("Id do leitor: ")
    if not verifique:
        novo_livro()
    else:
        nome=verifique

    if id=="00" or "0" or not id:
        id="00"
        status="DISPONIVEL"
    elif id:
        status="INDISPONIVEL"

    print("\nAviso, livros com ID:00, são livros disponiveis")
#    cursor.execute("CREATE TABLE livros(ID, nome, status)")

    #Adicionar livro a um id(leitor)
    cursor.execute("""INSERT INTO livros(ID, nome, status) VALUES (?,?,?)""",(id, nome, status))

    banco.commit()
    cursor.execute("SELECT * FROM livros")
    print(cursor.fetchall())
