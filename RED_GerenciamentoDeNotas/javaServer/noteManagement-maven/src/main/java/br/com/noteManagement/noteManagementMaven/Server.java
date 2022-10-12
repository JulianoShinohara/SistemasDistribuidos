package br.com.noteManagement.noteManagementMaven;

////////////////////////////////////////////////////////////////////////////////////////////
// Atividade 3 - RED Server                                                               //
// Descrição: Implementar um serviço de gerenciamento de notas                            //
//       - Matricular o aluno em nova disciplina                                          //
//       - Alterar NOTA do aluno na tabela matricula (RA, cod.Disciplna, ano, semestre)   // 
//       - Alterar FALTAS do aluno na tabela matricula (RA, cod.Disciplna, ano, semestre) // 
//       - Listar alunos de uma disciplina (cod.Disciplina, ano, semestre)                //
//       - Listar disciplinas de um aluno (RA, ano, semestre)                             //
// Autores: Gabriela Marangoni Radigonda e Juliano Kendyi Shinohara                       //
// Data de criação: 06/10/2022                                                            //
// Datas de atualizações:08/10/2022                                                       //
//                       11/10/2022                                                       //
//                                                                                        //
////////////////////////////////////////////////////////////////////////////////////////////

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class Server {
    static final int INSERIR_MATRICULA = 1;
    static final int ALTERAR_NOTA = 2;
    static final int ALTERAR_FALTAS = 3;
    static final int LISTAR_ALUNOS = 4;
    static final int LISTAR_DISCIPLINAS_ALUNO = 5;

    public static Connection connect() {
        Connection conectado = null;

        try {
            // faz a conexão com o db
            String url = "jdbc:sqlite:../database_com_dados-contrib-Daniel-Farina.db";
            conectado = DriverManager.getConnection(url);
            System.out.println("Conectado com sucesso . . . ");

        } catch (SQLException e) {           
            System.out.println(e.getMessage());  // caso a conexão não aconteça
        }

        return conectado;
    }

    ////////////////////////////////////
    /////// INSERE UMA MATRICULA ///////
    ////////////////////////////////////
    public static NoteManagement.inserirMatriculaResponse inserirMatricula(Connection connection, int ra,
            String codigoDisciplina, int ano, int semestre) {
        NoteManagement.inserirMatriculaResponse.Builder response = NoteManagement.inserirMatriculaResponse.newBuilder();
        try {
            Statement statement = connection.createStatement();            
            // faz a busca da disciplina no bd
            ResultSet resultSetDB = statement.executeQuery("SELECT * FROM disciplina WHERE '" + String.valueOf(codigoDisciplina) + "' = codigo;");
            // quando a busca da errado
            if (!resultSetDB.isBeforeFirst()) {
                response.setMensagem("A disciplina informada não existe");
                return response.build();
            }
            // faz a busca do aluno no bd
            resultSetDB = statement.executeQuery("SELECT * FROM aluno WHERE " + ra + " = ra;");
            // quando a busca da errado
            if (!resultSetDB.isBeforeFirst()) {
                response.setMensagem("O aluno informado não existe");
                return response.build();
            }
            // faz a verificação se aluno está matriculado na disciplina
            resultSetDB = statement.executeQuery(
                    "SELECT * FROM matricula WHERE " + ra + " = ra AND '" + String.valueOf(codigoDisciplina)
                            + "' = cod_disciplina AND " + ano + " = ano AND " + semestre + " = semestre;");
            // se o aluno já está matriculado
            if (resultSetDB.isBeforeFirst()) {
                response.setMensagem("O aluno já está matriculado nessa disciplina");
                return response.build();
            }
            // faz a inserção de uma nova matricula
            statement.execute("INSERT INTO matricula (ra, cod_disciplina, ano, semestre, nota, faltas) VALUES (" + ra
                    + ", '" + String.valueOf(codigoDisciplina) + "', " + ano + ", " + semestre + ", 0, 0);");
            //faz a verificação se foi inserido 
            resultSetDB = statement.executeQuery(
                    "SELECT * FROM matricula WHERE " + ra + " = ra AND '" + String.valueOf(codigoDisciplina)
                            + "' = cod_disciplina AND " + ano + " = ano AND " + semestre + " = semestre;");
            // faz a verificação se der errado ao realizar a matricula
            if (!resultSetDB.isBeforeFirst()) {
                response.setMensagem("Não foi possível realizar a matrícula");
                return response.build();
            }
            // faz a criação do objeto de resposta
            while (resultSetDB.next()) {
                int raResult = resultSetDB.getInt("ra");
                int anoResult = resultSetDB.getInt("ano");
                int semestreResult = resultSetDB.getInt("semestre");
                String codigoDisciplinaResult = resultSetDB.getString("cod_disciplina");
                float notaResult = resultSetDB.getFloat("nota");
                int faltasResult = resultSetDB.getInt("faltas");
                response.setMatricula(NoteManagement.Matricula.newBuilder().setRa(raResult).setAno(anoResult)
                        .setSemestre(semestreResult).setCodigoDisciplina(codigoDisciplinaResult).setNota(notaResult)
                        .setFaltas(faltasResult).build());
            }
        }
        // mensagem de erro caso de errado
        catch (SQLException e) {           
            response.setMensagem(e.getMessage());
        }
        return response.build();
    }

    ///////////////////////////////////
    /////  ALTERA A NOTA DO ALUNO /////
    ///////////////////////////////////
    public static NoteManagement.alterarNotaResponse alterarNota(Connection connection, int ra, String codigoDisciplina,
            int ano, int semestre, float nota) {
        NoteManagement.alterarNotaResponse.Builder response = NoteManagement.alterarNotaResponse.newBuilder();
        try {
            // faz a criação de um statement para a realização da consulta
            Statement statement = connection.createStatement();
            // faz a verificação se o aluno está matriculado na disciplina
            ResultSet resultSetDB = statement.executeQuery(
                    "SELECT * FROM matricula WHERE ra = " + ra + " AND '" + String.valueOf(codigoDisciplina)
                            + "' = cod_disciplina AND " + ano + " = ano AND " + semestre + " = semestre;");
            // faz a verificação se o aluno não estiver matriculado na disciplina e retorna mensagem de erro
            if (!resultSetDB.isBeforeFirst()) {
                response.setMensagem("O aluno não foi encontrado na disciplina informada");
                return response.build();
            }
            // faz a atualização da nota do aluno na disciplina
            statement.execute("UPDATE matricula SET nota = " + nota + " WHERE ra =" + ra + " AND cod_disciplina = '"
                    + String.valueOf(codigoDisciplina) + "' AND ano = " + ano + " AND semestre = " + semestre + ";");
            // faz novamente a busca da nota para que possa ser retornada ao aluno a nota atualizada
            resultSetDB = statement.executeQuery(
                    "SELECT * FROM matricula WHERE ra = " + ra + " AND '" + String.valueOf(codigoDisciplina)
                            + "' = cod_disciplina AND " + ano + " = ano AND " + semestre + " = semestre;");
            // faz a criação de um objeto para a resposta
            response.setRa(resultSetDB.getInt("ra"));
            response.setAno(resultSetDB.getInt("ano"));
            response.setSemestre(resultSetDB.getInt("semestre"));
            response.setCodigoDisciplina(resultSetDB.getString("cod_disciplina"));
            response.setNota(resultSetDB.getFloat("nota"));
        }
        // mensagem de erro caso de errado
        catch (SQLException e) {
            response.setMensagem(e.getMessage());
        }
        return response.build();
    }

    ///////////////////////////////////
    //// ALTERA AS FALTAS DO ALUNO ////
    ///////////////////////////////////
    public static NoteManagement.alterarFaltasResponse alterarFaltas(Connection connection, int ra,
            String codigoDisciplina, int ano, int semestre, int faltas) {
        NoteManagement.alterarFaltasResponse.Builder response = NoteManagement.alterarFaltasResponse.newBuilder();
        try {
            // faz a criação de um statement para a realização da consulta
            Statement statement = connection.createStatement();
            // faz a verificação se o aluno está matriculado na disciplina
            ResultSet resultSetDB = statement.executeQuery(
                    "SELECT * FROM matricula WHERE ra = " + ra + " AND '" + String.valueOf(codigoDisciplina)
                            + "' = cod_disciplina AND " + ano + " = ano AND " + semestre + " = semestre;");
            // faz a verificação se o aluno não estiver matriculado na disciplina e retorna mensagem de erro
            if (!resultSetDB.isBeforeFirst()) {
                response.setMensagem("O aluno não foi encontrado na disciplina informada");
                return response.build();
            }
            // faz a atualização das faltas nas disciplinas através da tabela matricula
            statement.execute("UPDATE matricula SET faltas = " + faltas + " WHERE ra =" + ra + " AND cod_disciplina = '"
                    + String.valueOf(codigoDisciplina) + "' AND ano = " + ano + " AND semestre = " + semestre + ";");
            // faz novamente a busca das faltas para que possa ser retornada ao aluno as faltas atualizada
            resultSetDB = statement.executeQuery(
                    "SELECT * FROM matricula WHERE ra = " + ra + " AND '" + String.valueOf(codigoDisciplina)
                            + "' = cod_disciplina AND " + ano + " = ano AND " + semestre + " = semestre;");
            // faz a criação do objeto response
            response.setRa(resultSetDB.getInt("ra"));
            response.setAno(resultSetDB.getInt("ano"));
            response.setSemestre(resultSetDB.getInt("semestre"));
            response.setCodigoDisciplina(resultSetDB.getString("cod_disciplina"));
            response.setFaltas(resultSetDB.getInt("faltas"));
        }
        // mensagem de erro caso de errado
        catch (SQLException e) {
            response.setMensagem(e.getMessage());
        }
        return response.build();
    }

    ////////////////////////////////////
    /////////// LISTAR ALUNOS //////////
    ////////////////////////////////////
    public static NoteManagement.listarAlunosResponse listarAlunos(Connection connection, String codigoDisciplina,
            int ano, int semestre) {
        NoteManagement.listarAlunosResponse.Builder response = NoteManagement.listarAlunosResponse.newBuilder();
        try {
            // faz a criação de um statement para a realização da consulta
            Statement statement = connection.createStatement();
            // faz a busca de todos os alunos matriculados na disciplina
            ResultSet resultSetDB = statement
                    .executeQuery("SELECT a.* FROM matricula m INNER JOIN aluno a ON (a.ra = m.ra) WHERE '"
                            + String.valueOf(codigoDisciplina) + "' = cod_disciplina AND " + ano + " = ano AND "
                            + semestre + " = semestre;");
            // caso não encontre nenhum aluno
            // faz a verificação se não há nenhum aluno matriculado na disciplina e retorna mensagem de erro
            if (!resultSetDB.isBeforeFirst()) {
                response.setMensagem("Não há alunos matriculados nessa disciplina");
                return response.build();
            }
            // faz a criação de um objeto para a resposta
            while (resultSetDB.next()) {
                int ra = resultSetDB.getInt("ra");
                String nome = resultSetDB.getString("nome");
                int periodo = resultSetDB.getInt("periodo");
                response.addAlunos(NoteManagement.listarAlunosResponse.Aluno.newBuilder().setNome(nome).setRa(ra)
                        .setPeriodo(periodo).build());
            }
        }
        // mensagem de erro caso de errado
        catch (SQLException e) {
            response.setMensagem(e.getMessage());
        }
        return response.build();
    }

    ////////////////////////////////////////////
    ///// LISTA AS DISCIPLINAS DE UM ALUNO /////
    ////////////////////////////////////////////
    public static NoteManagement.listarDisciplinasAlunoResponse listarDisciplinasAluno(Connection connection, int ra, int ano, int semestre) {
        // faz a criação de um builder para a resposta
        NoteManagement.listarDisciplinasAlunoResponse.Builder response = NoteManagement.listarDisciplinasAlunoResponse.newBuilder();
        try {
            Statement statement = connection.createStatement();
            // faz a busca das disciplinas do aluno com base no ra, ano e semestre
            ResultSet resultSetDB = statement.executeQuery("SELECT * FROM matricula WHERE " + ra + " = ra AND " + ano
                    + " = ano AND " + semestre + " = semestre;");
            // mensagem de erro caso o aluno que foi informado não esteja matriculado em nenhuma disciplina no ano e semetre informados
            if (!resultSetDB.isBeforeFirst()) {
                response.setMensagem(
                        "O aluno informado não está cadastrado em nenhuma disciplina no ano e semetre informados");
                return response.build();
            }
            // faz a criação de um objeto para a resposta
            while (resultSetDB.next()) {
                String codigoDisciplinaResult = resultSetDB.getString("cod_disciplina");
                float nota = resultSetDB.getFloat("nota");
                int faltas = resultSetDB.getInt("faltas");
                response.addDisciplinas(NoteManagement.listarDisciplinasAlunoResponse.DisciplinaAlunos.newBuilder()
                        .setRa(ra).setCodigoDisciplina(codigoDisciplinaResult).setNota(nota).setFaltas(faltas).build());
            }
        }
        // mensagem de erro
        catch (SQLException e) {
            response.setMensagem(e.getMessage());
        }
        return response.build();  // retorna o response.setAluno("");
    }

    //////////////////////////
    ////////// MAIN //////////
    //////////////////////////
    public static void main(String args[]) {
        // faz a conexão com o bd
        Connection conectado = connect();
        try {
            int PORT = 6000;
            // faz a criação de um socket do tipo 'server'
            ServerSocket listenSocket = new ServerSocket(PORT);
            // faz criação das váriveis para recebimento de mensagens
            String valueStr;
            int sizeBuffer;
            byte[] buffer;
            // faz criação das váriaveis para envio de mensagens
            byte[] msg;
            String responseSize;
            // faz a aceitação da conexão com o socket nas portas definidas anteriormente
            Socket clientSocket = listenSocket.accept();
            // gera uma conexão com o client para receber mensagens do cliente
            DataInputStream inClient = new DataInputStream(clientSocket.getInputStream());
            // gera uma conexão com o client para enviar mensagens para o cliente
            DataOutputStream outClient = new DataOutputStream(clientSocket.getOutputStream());
            while (true) {
                // faz o recebimento do tamanho do buffer
                valueStr = inClient.readLine();
                // faz a converção do tamanho do buffer para inteiro
                sizeBuffer = Integer.valueOf(valueStr);
                // gera o buffer com o tamanho da mensagem
                buffer = new byte[sizeBuffer];
                // faz a leitura do buffer
                inClient.read(buffer);
                // realiza o unmarshalling
                NoteManagement.requestType type = NoteManagement.requestType.parseFrom(buffer);
                // recebe o tamanho do buffer
                valueStr = inClient.readLine();
                // faz a converção do tamanho do buffer para inteiro
                sizeBuffer = Integer.valueOf(valueStr);
                // faz a criação do buffer com o tamanho da mensagem
                buffer = new byte[sizeBuffer];
                // faz a leitura do buffer
                inClient.read(buffer);

                switch (type.getType()) {
                    case LISTAR_ALUNOS:
                        // faz o recebimento do request e faz o unmarshalling
                        NoteManagement.listarAlunosRequest request = NoteManagement.listarAlunosRequest
                                .parseFrom(buffer);
                        // faz a chamada da função para listar os alunos
                        NoteManagement.listarAlunosResponse response = listarAlunos(conectado, request.getCodigoDisciplina(),
                                request.getAno(), request.getSemestre());
                        // faz a converção do resultado da função para bytes
                        msg = response.toByteArray();
                        // obtem o tamanho do resultado e converte para string
                        responseSize = String.valueOf(msg.length) + "\n";
                        // envia o tamanho do resultado em bytes
                        outClient.write(responseSize.getBytes());
                        // envia o resultado em bytes
                        outClient.write(msg);
                        break;
                    case ALTERAR_NOTA:
                        // faz o  rcebimento do request e faz o unmarshalling
                        NoteManagement.alterarNotaRequest alterarNotaRequest = NoteManagement.alterarNotaRequest
                                .parseFrom(buffer);
                        // faz a chamada da função que altera a nota de um aluno
                        NoteManagement.alterarNotaResponse alterarNotaResponse = alterarNota(conectado,
                                alterarNotaRequest.getRa(), alterarNotaRequest.getCodigoDisciplina(),
                                alterarNotaRequest.getAno(), alterarNotaRequest.getSemestre(),
                                alterarNotaRequest.getNota());
                        // faz a converção do resultado da função para bytes
                        msg = alterarNotaResponse.toByteArray();
                        // obtem o tamanho do resultado e converte para string
                        responseSize = String.valueOf(msg.length) + "\n";
                        // envia o tamanho do resultado em bytes
                        outClient.write(responseSize.getBytes());
                        // envia o resultado em bytes
                        outClient.write(msg);
                        break;
                    case ALTERAR_FALTAS:
                        // faz o recebimento do request e faz o unmarshalling
                        NoteManagement.alterarFaltasRequest alterarFaltasRequest = NoteManagement.alterarFaltasRequest
                                .parseFrom(buffer);
                        // faz a chamada da função que altera as faltas de um aluno
                        NoteManagement.alterarFaltasResponse alterarFaltasResponse = alterarFaltas(conectado,
                                alterarFaltasRequest.getRa(), alterarFaltasRequest.getCodigoDisciplina(),
                                alterarFaltasRequest.getAno(), alterarFaltasRequest.getSemestre(),
                                alterarFaltasRequest.getFaltas());
                        // faz a converção do resultado da função para bytes
                        msg = alterarFaltasResponse.toByteArray();
                        // obtem o tamanho do resultado e converte para string
                        responseSize = String.valueOf(msg.length) + "\n";
                        // envia o tamanho do resultado em bytes
                        outClient.write(responseSize.getBytes());
                        // envia o resultado em bytes
                        outClient.write(msg);
                        break;
                    case LISTAR_DISCIPLINAS_ALUNO:
                        // faz o recebimento do request e faz o unmarshalling
                        NoteManagement.listarDisciplinasAlunoRequest listarDisciplinasAlunoRequest = NoteManagement.listarDisciplinasAlunoRequest
                                .parseFrom(buffer);
                        // faz a chamada da função que faz a listagem de disciplinas do aluno
                        NoteManagement.listarDisciplinasAlunoResponse listarDisciplinasAlunoResponse = listarDisciplinasAluno(
                            conectado, listarDisciplinasAlunoRequest.getRa(), listarDisciplinasAlunoRequest.getAno(),
                                listarDisciplinasAlunoRequest.getSemestre());
                        // faz a converção do resultado da função para bytes
                        msg = listarDisciplinasAlunoResponse.toByteArray();
                        // obtem o tamanho do array de bytes e converte para string
                        responseSize = String.valueOf(msg.length) + "\n";
                        // envia o tamanho da resposta em bytes
                        outClient.write(responseSize.getBytes());
                        // envia a resposta em bytes
                        outClient.write(msg);
                        break;
                    case INSERIR_MATRICULA:
                        // faz o recebimento do request e faz o unmarshalling
                        NoteManagement.inserirMatriculaRequest inserirMatriculaRequest = NoteManagement.inserirMatriculaRequest
                                .parseFrom(buffer);
                        // faz a chamada da função de inserir matrícula
                        NoteManagement.inserirMatriculaResponse inserirMatriculaResponse = inserirMatricula(conectado,
                                inserirMatriculaRequest.getMatricula().getRa(),
                                inserirMatriculaRequest.getMatricula().getCodigoDisciplina(),
                                inserirMatriculaRequest.getMatricula().getAno(),
                                inserirMatriculaRequest.getMatricula().getSemestre());
                        // faz a converção do resultado da função para bytes
                        msg = inserirMatriculaResponse.toByteArray();
                        // obtem o tamanho do array de bytes e converte para string
                        responseSize = String.valueOf(msg.length) + "\n";
                        // envia o tamanho da resposta em bytes
                        outClient.write(responseSize.getBytes());
                        // envia a resposta em bytes
                        outClient.write(msg);
                        break;
                    default:
                        // quando não é encontrado nenhuma requisição 
                        System.out.println("Nenhum tipo de requisição");
                        break;
                }
            }
        } catch (IOException e) {
            // faz a mostragem da mensagem de erro
            System.out.println("Listensocket:" + e.getMessage());
        }
    }
}