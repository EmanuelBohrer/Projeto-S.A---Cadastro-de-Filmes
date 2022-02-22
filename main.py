import mysql.connector
from mysql.connector import Error



def Conexao():
    try:
        global conn
        conn = mysql.connector.connect(host='localhost',database='projetosa',user='root',password='')
    except Error as e:
        print("Erro de conexão",e)


def Consultar():
    try:
        Conexao()
        consulta_bdd =("SELECT * from filmes")
        cursor = conn.cursor()
        cursor.execute(consulta_bdd)
        linhas = cursor.fetchall()
        print("Total de filmes no Sistema : ",cursor.rowcount)

        print("\nMostrando todos os filmes cadastrados ")
        for linha in linhas:
            print("ID do Filme :",linha[0])
            print("Título :",linha[1])
            print("Gênero :",linha[2])
            print("Ano de Lançamento :",linha[3])
            print("Diretor do Filme :",linha[4])
            print("Nota :",linha[5],"\n")

    except Error as e:
        print("Falha a exibir os filmes na BDD : ",e)
    finally:
        if (conn.is_connected()):
            conn.close()
            cursor.close()
            print("Conexão Encerrada!")


def ConsultaEspecial(t1):
    try:
        Conexao()
        consulta_bdd =("SELECT * from filmes where id_filme = " + t1)
        cursor = conn.cursor()
        cursor.execute(consulta_bdd)
        linhas = cursor.fetchall()
        print("\nMostrando busca específica ")
        for linha in linhas:
            print("ID do Filme :",linha[0])
            print("Título :",linha[1])
            print("Gênero :",linha[2])
            print("Ano de Lançamento :",linha[3])
            print("Diretor do Filme :",linha[4])
            print("Nota :",linha[5],"\n")


    except Error as e:
        print("Falha a exibir os filmes na BDD : ",e)
    finally:
        if (conn.is_connected()):
            conn.close()
            cursor.close()
            print("Conexão Encerrada!")


def Insert():
    print("Cadastro de Filme no BDD")
    print("Insira os dados conforme solicitados.")
    t1 = input("ID do Filme : ")
    t2 = input("Título : ")
    t3 = input("Gênero : ")
    t4 = input("Ano de Lançamento : ")
    t5 = input("Diretor do Filme : ")
    t6 = input("Nota : ")
    dados = t1 + ',\'' + t2 + '\',\'' + t3 + '\',\'' + t4 + '\',\'' + t5 + '\',' + t6 + ')'
    insert_bdd = """INSERT INTO filmes
            (id_filme,titulo,genero,ano,diretor,nota) 
            VALUES ("""
    sql = insert_bdd + dados
    try:
        Conexao()
        enviar = sql
        cursor = conn.cursor()
        cursor.execute(enviar)
        conn.commit()
        print("Total de registros adicionados na BDD : ",cursor.rowcount)
        cursor.close()
    except Error as e:
        print("Falha ao inserir um registro na BDD : ",e)
    finally:
        if (conn.is_connected()):
            conn.close()
            print("Conexão Encerrada!")


def Random():
    try:
        Conexao()
        random=("SELECT * FROM filmes ORDER BY Rand() LIMIT 1")
        cursor = conn.cursor()
        cursor.execute(random)
        linhas = cursor.fetchall()
        print("\n# Sugestão Randômica # ")
        for linha in linhas:
            print("ID do Filme :", linha[0])
            print("Título :", linha[1])
            print("Gênero :", linha[2])
            print("Ano de Lançamento :", linha[3])
            print("Diretor do Filme :", linha[4])
            print("Nota :", linha[5], "\n")

    except Error as e:
        print("Falha a escolher um filme randômico : ",e)
    finally:
        if(conn.is_connected()):
            conn.close()
            cursor.close()
            print("Conexão com BDD encerada!")


def Delete():
    print("Para efetuar o delete, insira o ID do filme abaixo.")
    t1 = input("Insira o ID : ")
    dados = t1
    delete_bdd = """DELETE FROM filmes WHERE id_filme = """
    delete = delete_bdd + dados
    try:
        Conexao()
        efetuar = delete
        cursor = conn.cursor()
        cursor.execute(efetuar)
        conn.commit()
        print("Total de registros deletados :",cursor.rowcount)
        cursor.close()
    except Error as e:
        print("Falha ao efetuar um delete ",e)
    finally:
        if (conn.is_connected()):
            conn.close()
            print("Conexão Encerrada!")


def Update(declaracao):
    try:
        Conexao()
        alterar = declaracao
        cursor = conn.cursor()
        cursor.execute(alterar)
        conn.commit()
        print("Registro alterado com sucesso.")
    except Error as e:
        print("Erro em alterar registro : ",e)
    finally:
        if (conn.is_connected()):
            conn.close()
            print("Conexão Encerrada!")


def Ranking():
    try:
        Conexao()
        ranking = ("SELECT * FROM filmes order by nota desc")
        cursor = conn.cursor()
        cursor.execute(ranking)
        linhas = cursor.fetchall()
        for linha in linhas:
            print("ID do Filme :", linha[0])
            print("Título :", linha[1])
            print("Gênero :", linha[2])
            print("Ano de Lançamento :", linha[3])
            print("Diretor do Filme :", linha[4])
            print("Nota :", linha[5], "\n")
    except Error as e:
        print("Erro para efetuar o ranking : ",e)
    finally:
        if(conn.is_connected()):
            conn.close()
            cursor.close()
            print("Conexão Encerrada.")


def ConsultaGen(declaracao1):
    try:
        Conexao()
        cursor = conn.cursor()
        cursor.execute(declaracao1)
        linhas = cursor.fetchall()
        print("\nTotal de filmes deste gênero no BDD : ",cursor.rowcount)
        for linha in linhas:
            print("\n")
            print("ID do Filme :", linha[0])
            print("Título :", linha[1])
            print("Gênero :", linha[2])
            print("Ano de Lançamento :", linha[3])
            print("Diretor do Filme :", linha[4])
            print("Nota :", linha[5], "\n")

    except Error as e:
        print("Falha a exibir os filmes na BDD : ", e)
    finally:
        if (conn.is_connected()):
            conn.close()
            cursor.close()
            print("Conexão Encerrada!")


def VerificaId():
    seleciona = "SELECT id_filme from filmes where id_filme = '{}'".format(t1)
    try:
        Conexao()
        cursor = conn.cursor()
        cursor.execute(seleciona)
        resultado = cursor.fetchall()
        if len(resultado)!=0:
            print("ID de filme encontrado.")
            return 'sim'
        else:
            print("ID não encontrado.")
            return 'nao'
    except Error as e:
        print("Ouve uma falha para verificar o ID :  ",e)
    finally:
        if (conn.is_connected()):
            conn.close()
            cursor.close()


def Login():
    user_log = str(input("Insira user : "))
    senha_log = str(input("Insira senha : "))
    validar = False
    if not(senha_log =='' or user_log==''):
        try:
            Conexao()
            cursor = conn.cursor()
            cursor.execute('select * from db_user')
            records = cursor.fetchall()
            for i in records:
                if user_log in i and senha_log in i:
                    validar = True
                    return i[3]
            if validar == False:
                return ''
        except Error as e:
            print("Falha ao login : ",e)
        finally:
            if (conn.is_connected()):
                conn.close()
                cursor.close()


var = 1
while var !=0:
    permissao = ''
    print("\033[1;92m[ Para sair do programa, digite 0. ]")
    print("[ Para logar digite 1. ]")
    var3 = int(input("Digite : "))
    if var3 == 0:
        var=0
    elif var3 ==1:
        permissao = Login()
    if permissao == 'master':
        op = 1
        while op!=0:
            print(f"""
                  ### B.W Sistema de Filmes [MASTER ADMIN] ###
                  1 - Ranking de Filmes
                  2 - CRUD 
                  3 - Sugestão de filme randômica
                  4 - Pesquisa por gênero
                  0 - Sair do Programa
                  """)
            op = int(input('Escolha sua opção : '))
            if op ==0:
                var = 0
            if op == 1:
                Ranking()
            elif op == 2:
                x = 1
                while x != 0:
                    print(f"""
                              ### B.W Sistema de Filmes (CRUD) ###
                              1 - Adicionar Filmes
                              2 - Deletar um Filme 
                              3 - Exibir Filmes nos registros
                              4 - Atualizar um filme no registro
                              0 - Sair da tela
                              """)
                    x = int(input("Escolha sua opção : "))
                    if x == 1:
                        Insert()
                    elif x == 2:
                        Delete()
                    elif x == 3:
                        Consultar()
                    elif x == 4:
                        t1 = input("Insira o ID do filme para um Update : ")
                        if VerificaId() == 'nao':
                            continue
                        ConsultaEspecial(t1)
                        print("\nInsira os novos registro do filme : ")
                        titulof = input("Título novo : ")
                        generof = input("Gênero novo : ")
                        anof = input("Ano de Lançamento : ")
                        diretorf = input("Diretor : ")
                        notaf = input("Nota : ")

                        declaracao = """UPDATE filmes SET titulo = """ '\'' + titulof + '\','"""
                            genero = """ '\'' + generof + '\','""" ano = """'\'' + anof + '\','""" diretor = """'\'' + diretorf + '\','"""
                            nota =  """'' + notaf + ' WHERE id_filme = ' + t1
                        Update(declaracao)

                    elif x == 0:
                        print("Saindo da tela.")
                    else:
                        print("Opção inválida, tente novamente.")
            elif op == 3:
                Random()
            elif op == 4:
                print("Insira o gênero para a pesquisa : ")
                id = input("Gênero : ")
                declaracao1 = """SELECT * from filmes WHERE genero = """ '\'' + id + '\';'
                ConsultaGen(declaracao1)
        conn.close()
    elif permissao == 'user':
        op = 1
        while op!=0:
            print(f"""
                  ### B.W Sistema de Filmes [USER COMUM] ###
                  1 - Ranking de Filmes
                  2 - Sugestão de filme randômica
                  3 - Pesquisa por gênero
                  4 - Exibir Filmes
                  0 - Sair do Programa
                  """)
            op = int(input("Insira a opção : "))
            if op == 0:
                var=0
            if op == 1:
                Ranking()
            elif op == 2:
                Random()
            elif op == 3:
                print("Insira o gênero para a pesquisa : ")
                id = input("Gênero : ")
                declaracao1 = """SELECT * from filmes WHERE genero = """ '\'' + id + '\';'
                ConsultaGen(declaracao1)
            elif op == 4:
                Consultar()
            elif op == 0:
                print("Saindo do programa.")
        conn.close()

    elif permissao == '':
        print("Caixa em branco, ou Login inválido.'\033[93m")












