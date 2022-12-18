###########################################################################################
# Atividade 3 - RED Client                                                                #
# Descrição: Implementar um serviço de gerenciamento de notas                             #
#       - Matricular o aluno em nova disciplina                                           #
#       - Alterar NOTA do aluno na tabela matricula (RA, cod.Disciplna, ano, semestre)    # 
#       - Alterar FALTAS do aluno na tabela matricula (RA, cod.Disciplna, ano, semestre)  # 
#       - Listar alunos de uma disciplina (cod.Disciplina, ano, semestre)                 #
#       - Listar disciplinas de um aluno (ra, ano, semestre)                              #
# Autores: Gabriela Marangoni Radigonda e Juliano Kendyi Shinohara                        #
# Data de criação: 06/10/2022                                                             #
# Datas de atualizações:08/10/2022                                                        #
#                       11/10/2022                                                        #
#                                                                                         #
###########################################################################################

import socket
import gerenciamentoNotas_pb2
# Cria e conecta um socket TCP
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(("localhost", 6000))

# Opçoes de execução
INSERIR_MATRICULA = "1"
ALTERAR_NOTA = "2"
ALTERAR_FALTAS = "3"
LISTAR_ALUNOS = "4"
LISTAR_DISCIPLINAS_ALUNO = "5"

# Enviar os dados da requisição
def enviaRequest(execucaoID, mensagem, tamMensagem):
    enviaRequestType(execucaoID) # Envia o tipo de requisição
    clientsocket.send((str(tamMensagem) + "\n").encode()) # Envia o tamanho da mensagem
    clientsocket.send(mensagem) # Envia a mensagem

# Enviar o tipo de requisição
def enviaRequestType(execucaoID):
    requestType = gerenciamentoNotas_pb2.requestType()
    # Atribui o valor da opção ao tipo de requisição
    requestType.type = int(execucaoID)
    # transforma para string
    msg = requestType.SerializeToString()
    tamMensagem = len(msg)
    clientsocket.send((str(tamMensagem) + "\n").encode()) # Envia o tamanho da mensagem
    clientsocket.send(msg)

# Recebe os dados da requisição do cliente e envia para o servidor
def dadosRequisicao(execucaoID):

    if execucaoID == INSERIR_MATRICULA:
        # Variável com dados da requisição
        request = gerenciamentoNotas_pb2.inserirMatriculaRequest()
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
            # Envia os dados para o servidor
            enviaRequest(execucaoID, request.SerializeToString(), len(request.SerializeToString()))
            tamMensagem = ''
            while True: 
                tamMensagem += clientsocket.recv(1).decode()
                if tamMensagem.endswith('\n'):
                    break
            tamMensagem = int(tamMensagem)
            # Recebe a mensagem
            response = clientsocket.recv(tamMensagem)
            responseParsed = gerenciamentoNotas_pb2.inserirMatriculaResponse()
            responseParsed.ParseFromString(response)
            # Requisição com Sucesso
            if responseParsed.mensagem:
                print(responseParsed.mensagem)
            else:
                print("\n\n---- Aluno inserido ---- \nRA: " + str(responseParsed.matricula.ra) + "\nCodigo da Disciplina:" + str(responseParsed.matricula.codigoDisciplina) + "\nAno: " + str(responseParsed.matricula.ano) + "\nSemestre: " + str(responseParsed.matricula.semestre), "\n")
        else:
            print("Informações incorretas\n")

    elif execucaoID == ALTERAR_NOTA:
        # Variável com dados da requisição
        request = gerenciamentoNotas_pb2.alterarNotaRequest()
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
            # Envia os dados para o servidor
            enviaRequest(execucaoID, request.SerializeToString(), len(request.SerializeToString()))
            tamMensagem = ''
            while True:
                tamMensagem += clientsocket.recv(1).decode()
                if tamMensagem.endswith('\n'):
                    break
            tamMensagem = int(tamMensagem)
            # Recebe a mensagem
            response = clientsocket.recv(tamMensagem)
            responseParsed = gerenciamentoNotas_pb2.alterarNotaResponse()
            responseParsed.ParseFromString(response)
            # Requisição com Sucesso
            if responseParsed.mensagem != "":
                print(responseParsed.mensagem)
            else:
                print("\n\n---- Alteracao realizada com sucesso!! ---- \nRA: " + str(responseParsed.ra) + "\nCodigo da Disciplina:" + str(responseParsed.codigoDisciplina) + "\nAno: " + str(responseParsed.ano) + "\nSemestre: " + str(responseParsed.semestre) + "\nNota: " + str(responseParsed.nota), "\n")
        else:
            print("Informações incorretas\n")

    elif execucaoID == ALTERAR_FALTAS:
        # Variável com dados da requisição
        request = gerenciamentoNotas_pb2.alterarFaltasRequest()
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
            # Envia os dados para o servidor
            enviaRequest(execucaoID, request.SerializeToString(), len(request.SerializeToString()))
            tamMensagem = ''
            while True:
                tamMensagem += clientsocket.recv(1).decode()
                if tamMensagem.endswith('\n'):
                    break
            tamMensagem = int(tamMensagem)
            # Recebe a mensagem
            response = clientsocket.recv(tamMensagem)
            responseParsed = gerenciamentoNotas_pb2.alterarFaltasResponse()
            responseParsed.ParseFromString(response)
            # Requisição com Sucesso
            if responseParsed.mensagem != "":
                print(responseParsed.mensagem)
            else:
                print("\n\n---- Alteracao realizada com sucesso!! ---- \nRA: " + str(responseParsed.ra) + "\nCodigo da Disciplina:" + str(responseParsed.codigoDisciplina) + "\nAno: " + str(responseParsed.ano) + "\nSemestre: " + str(responseParsed.semestre) + "\nFaltas: " + str(responseParsed.faltas), "\n")
        else:
            print("Informações incorretas\n")

    elif execucaoID == LISTAR_ALUNOS:
        # Variável com dados da requisição
        request = gerenciamentoNotas_pb2.listarAlunosRequest()
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
            # Envia os dados para o servidor
            enviaRequest(execucaoID, request.SerializeToString(), len(request.SerializeToString()))
            tamMensagem = ''
            while True:
                tamMensagem += clientsocket.recv(1).decode()
                if tamMensagem.endswith('\n'):
                    break
            tamMensagem = int(tamMensagem)
            # Recebe a mensagem
            response = clientsocket.recv(tamMensagem)
            responseParsed = gerenciamentoNotas_pb2.listarAlunosResponse()
            responseParsed.ParseFromString(response)
            # Requisição com Sucesso
            if responseParsed.mensagem != "":
                print(responseParsed.mensagem)
            else:
                print("\n\n---- Lista de alunos ----")
                for aluno in responseParsed.alunos:
                    print("")
                    print(aluno, end="")
                    print("")
        else:
            print("Informações incorretas\n")

    elif execucaoID == LISTAR_DISCIPLINAS_ALUNO:
        # Variável com dados da requisição
        request = gerenciamentoNotas_pb2.listarDisciplinasAlunoRequest()
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
            # Envia os dados para o servidor
            enviaRequest(execucaoID, request.SerializeToString(), len(request.SerializeToString()))
            tamMensagem = ''
            while True:
                tamMensagem += clientsocket.recv(1).decode()
                if tamMensagem.endswith('\n'):
                    break
            tamMensagem = int(tamMensagem)
            # Recebe a mensagem
            response = clientsocket.recv(tamMensagem)
            responseParsed = gerenciamentoNotas_pb2.listarDisciplinasAlunoResponse()
            responseParsed.ParseFromString(response)
            # Requisição com Sucesso
            if responseParsed.mensagem != "":
                print(responseParsed.mensagem)
            else:
                print("\n\n---- Lista de disciplinas do aluno ----")
                for i in range(len(responseParsed.disciplinas)):
                        print("\nRA: " + str(responseParsed.disciplinas[i].ra) + "\nCódigo da Disciplina: " + str(responseParsed.disciplinas[i].codigoDisciplina) + "\nNota: " + str(responseParsed.disciplinas[i].nota) + "\nFaltas: " + str(responseParsed.disciplinas[i].faltas), "\n")
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
