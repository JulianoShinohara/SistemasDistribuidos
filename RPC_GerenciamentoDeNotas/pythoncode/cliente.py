###########################################################################################
# Atividade 4 - RPC Client                                                                #
# Descrição: Implementar um serviço de gerenciamento de notas                             #
#       - Matricular o aluno em nova disciplina                                           #
#       - Alterar NOTA do aluno na tabela matricula (RA, cod.Disciplna, ano, semestre)    # 
#       - Alterar FALTAS do aluno na tabela matricula (RA, cod.Disciplna, ano, semestre)  # 
#       - Listar alunos de uma disciplina (cod.Disciplina, ano, semestre)                 #
#       - Listar disciplinas de um aluno (ra, ano, semestre)                              #
# Autores: Gabriela Marangoni Radigonda e Juliano Kendyi Shinohara                        #
# Data de criação: 15/10/2022                                                             #
# Datas de atualizações:20/10/2022                                                        #
#                       14/12/2022                                                        #
#                                                                                         #
###########################################################################################

import grpc

import gerenciamentoNotas_pb2_grpc
import gerenciamentoNotas_pb2

channel = grpc.insecure_channel('localhost:6000')
stub = gerenciamentoNotas_pb2_grpc.GerenciadorDeNotasStub(channel)


# Opçoes de execução
INSERIR_MATRICULA = "1"
ALTERAR_NOTA = "2"
ALTERAR_FALTAS = "3"
LISTAR_ALUNOS = "4"
LISTAR_DISCIPLINAS_ALUNO = "5"


# Recebe os dados da requisição do cliente e envia para o servidor
def dadosRequisicao(execucaoID):

    if execucaoID == INSERIR_MATRICULA:
        # Variável com dados da requisição
        request = gerenciamentoNotas_pb2.InserirMatriculaRequest()
        # Recebe os dados da requisição
        print("Inserir novo aluno em uma disciplina: ")
        ra = input("RA do aluno: ")
        codigoDisciplina = input("Codigo da disciplina: ")
        ano = input("Ano: ")
        semestre = input("Semestre: ")
        # Verifica se os dados da requisição são válidos
        if ra.isdigit() and ano.isdigit() and semestre.isdigit() and codigoDisciplina != "" and ano != "" and semestre != "" and ra != "":
            request.matricula.ra = int(ra)
            request.matricula.codigoDisciplina = codigoDisciplina
            request.matricula.ano = int(ano)
            request.matricula.semestre = int(semestre)
            # Envia os dados e recebe a resposta do servidor
            response = stub.InserirMatricula(request)
            # Requisição com Sucesso
            if response.mensagem:
                print(response.mensagem)
            else:
                print("\n\n---- Aluno inserido ---- \nRA: " + str(response.matricula.ra) + "\nCodigo da Disciplina:" + str(response.matricula.codigoDisciplina) + "\nAno: " + str(response.matricula.ano) + "\nSemestre: " + str(response.matricula.semestre), "\n")
        else:
            print("Informações incorretas\n")

    elif execucaoID == ALTERAR_NOTA:
        # Variável com dados da requisição
        request = gerenciamentoNotas_pb2.AlterarNotaRequest()
        # Recebe os dados da requisição
        print("Altera nota de um aluno em determina disciplina: ")
        ra = input("RA do aluno: ")
        codigoDisciplina = input("Codigo da disciplina: ")
        ano = input("Ano: ")
        semestre = input("Semestre: ")
        nota = input("Nova nota do aluno: ")
        # Verifica se os dados da requisição são válidos
        if ra.isdigit() and ano.isdigit() and semestre.isdigit() and nota.isdigit() and codigoDisciplina != "" and ano != "" and semestre != "" and nota != "" and ra != "":
            request.ra = int(ra)
            request.codigoDisciplina = codigoDisciplina
            request.ano = int(ano)
            request.semestre = int(semestre)
            request.nota = float(nota)
            # Envia os dados e recebe a resposta do servidor
            response = stub.AlterarNota(request)
            # Requisição com Sucesso
            if response.mensagem != "":
                print(response.mensagem)
            else:
                print("\n\n---- Alteracao realizada com sucesso!! ---- \nRA: " + str(response.ra) + "\nCodigo da Disciplina:" + str(response.codigoDisciplina) + "\nAno: " + str(response.ano) + "\nSemestre: " + str(response.semestre) + "\nNota: " + str(response.nota), "\n")
        else:
            print("Informações incorretas\n")

    elif execucaoID == ALTERAR_FALTAS:
        # Variável com dados da requisição
        request = gerenciamentoNotas_pb2.AlterarFaltasRequest()
        # Recebe os dados da requisição
        print("Alterar faltas de um aluno em determinada disciplina: ")
        ra = input("RA do aluno: ")
        codigoDisciplina = input("Codigo da disciplina: ")
        ano = input("Ano: ")
        semestre = input("Semestre: ")
        faltas = input("Nova quantidade de faltas do aluno: ")
        # Verifica se os dados da requisição são válidos
        if ra != '' and codigoDisciplina != '' and ano != '' and semestre != '' and faltas != '' and ra.isdigit() and ano.isdigit() and semestre.isdigit() and faltas.isdigit():
            request.ra = int(ra)
            request.codigoDisciplina = codigoDisciplina
            request.ano = int(ano)
            request.semestre = int(semestre)
            request.faltas = int(faltas)
            # Envia os dados e recebe a resposta do servidor
            response = stub.AlterarFaltas(request)
            # Requisição com Sucesso
            if response.mensagem != "":
                print(response.mensagem)
            else:
                print("\n\n---- Alteracao realizada com sucesso!! ---- \nRA: " + str(response.ra) + "\nCodigo da Disciplina:" + str(response.codigoDisciplina) + "\nAno: " + str(response.ano) + "\nSemestre: " + str(response.semestre) + "\nFaltas: " + str(response.faltas), "\n")
        else:
            print("Informações incorretas\n")

    elif execucaoID == LISTAR_ALUNOS:
        # Variável com dados da requisição
        request = gerenciamentoNotas_pb2.ListarAlunosRequest()
        # Recebe os dados da requisição
        print("Listas alunos matriculados na disciplina: ")
        codigoDisciplina = input("Codigo da disciplina: ")
        ano = input("Ano: ")
        semestre = input("Semestre: ")
        # Verifica se os dados da requisição são válidos
        if ano.isdigit() and semestre.isdigit() and codigoDisciplina != "" and ano != "" and semestre != "":
            request.codigoDisciplina = codigoDisciplina
            request.ano = int(ano)
            request.semestre = int(semestre)
            # Envia os dados e recebe a resposta do servidor
            response = stub.ListarAlunos(request)
            # Requisição com Sucesso
            if response.mensagem != "":
                print(response.mensagem)
            else:
                print("\n\n---- Lista de alunos ----")
                for aluno in response.alunos:
                    print("")
                    print(aluno, end="")
                    print("")
        else:
            print("Informações incorretas\n")

    elif execucaoID == LISTAR_DISCIPLINAS_ALUNO:
        # Variável com dados da requisição
        request = gerenciamentoNotas_pb2.ListarDisciplinasAlunoRequest()
        # Recebe os dados da requisição
        print("Listar as disciplinas matriculadas por aluno: ")
        ra = input("RA do aluno: ")
        ano = input("Ano: ")
        semestre = input("Semestre: ")
        # Verifica se os dados da requisição são válidos
        if ra.isdigit() and ano.isdigit() and semestre.isdigit() and ra != '' and ano != '' and semestre != '':
            request.ra = int(ra)
            request.ano = int(ano)
            request.semestre = int(semestre)
            # Envia os dados e recebe a resposta do servidor
            response = stub.ListarDisciplinasAluno(request)
            # Requisição com Sucesso
            if response.mensagem != "":
                print(response.mensagem)
            else:
                print("\n\n---- Lista de disciplinas do aluno ----")
                for i in range(len(response.disciplinas)):
                        print("\nRA: " + str(response.disciplinas[i].ra) + "\nCódigo da Disciplina: " + str(response.disciplinas[i].codigoDisciplina) + "\nNota: " + str(response.disciplinas[i].nota) + "\nFaltas: " + str(response.disciplinas[i].faltas), "\n")
        else:
            print("Informações incorretas")
    else:
        print("Digite um número valido!!\n")


def main():
    while True:
        print("\n###################################")
        print("1 - Inserir Nova Matricula")
        print("2 - Alterar Nota")
        print("3 - Alterar Faltas")
        print("4 - Listar Alunos")
        print("5 - Listar Disciplinas do Aluno")
        print("###################################\n")

        execucaoID = input("Digite uma opcao: ")
        print("")
        if(execucaoID.isdigit()):
            dadosRequisicao(execucaoID)
        else:
            print("Digite um número !!\n")

if __name__ == "__main__":
    main()
