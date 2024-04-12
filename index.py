"""
Projeto: Sistema de Gerenciamento de Biblioteca

Neste projeto, você criará um sistema de gerenciamento de biblioteca que permitirá aos usuários:

Adicionar novos livros ao catálogo da biblioteca.
Registrar empréstimos de livros para os membros da biblioteca.
Verificar quais livros estão disponíveis para empréstimo.
Verificar o histórico de empréstimos de um determinado membro.
Etc.
Para este projeto, você pode criar uma estrutura de banco de dados com as seguintes tabelas:

Livros: Para armazenar informações sobre os livros na biblioteca.
Membros: Para armazenar informações sobre os membros da biblioteca.
Empréstimos: Para registrar os empréstimos de livros para os membros da biblioteca.
"""
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="juliana",
  database = "biblioteca"
)

mycursor = mydb.cursor()


def adicionarLivro():
    titulo = input("Digite o título do livro\n\n")
    nome = input("Digite o seu nome completo\n\n")
    if titulo and nome != "":
        sql = "INSERT INTO livros(livros, membros,emprestado) VALUES (%s,%s,'nao')"
        val = (titulo,nome)
        mycursor.execute(sql,val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")
    else:
        print("Insira nomes válidos.\n\n")

def registrarEmprestimo():
    livro_emprestado = input("Digite o livro que deseja alugar\n\n")
    nome = input("Digite o seu nome completo\n\n")
    consulta = "SELECT * FROM livros WHERE livros = %s"
    mycursor.execute(consulta,(livro_emprestado,))
    livro = mycursor.fetchone()
        
    if livro:
        emprestado_status = "UPDATE livros SET emprestado = 'sim' WHERE livros = %s "
        emprestado_para = "UPDATE livros SET emprestado_para = %s WHERE livros = %s"
        mycursor.execute(emprestado_status, (livro_emprestado,))
        mycursor.execute(emprestado_para,(nome, livro_emprestado))
        mydb.commit()


def verificarDisponiveis():
    livro_disponivel = input("Digite o nome do livro que deseja verificar:\n\n")
    consulta = "SELECT * FROM livros WHERE livros = %s AND emprestado = 'sim'"
    mycursor.execute(consulta,(livro_disponivel,))
    livro = mycursor.fetchone()

    if livro:
        print("O livro já está emprestado\n\n")
    else:
        print("O livro está disponível para alocação.\n\n")


while True:
    opcao = input("Selecione as opções\n1- Adicionar novos livros ao catalogo\n2- Registrar empréstimo de livro para os membros da biblioteca\n3- Verificar livros disponíveis para empréstimo\n4-Verificar histórico de empréstimo\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n")
    if opcao == "1":
        adicionarLivro()
    elif opcao == "2":
        registrarEmprestimo()
    elif opcao == "3":
        verificarDisponiveis()
    elif opcao == "4":
        verificarHistorico()
    else:
        print("Opção inválida, tente novamente.\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n")




