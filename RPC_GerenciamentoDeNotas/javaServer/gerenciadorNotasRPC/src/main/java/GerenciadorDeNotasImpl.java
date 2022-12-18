
////////////////////////////////////////////////////////////////////////////////////////////
// Atividade 4 - RPC Server                                                               //
// Descrição: Implementar um serviço de gerenciamento de notas                            //
//       - Matricular o aluno em nova disciplina                                          //
//       - Alterar NOTA do aluno na tabela matricula (RA, cod.Disciplna, ano, semestre)   // 
//       - Alterar FALTAS do aluno na tabela matricula (RA, cod.Disciplna, ano, semestre) // 
//       - Listar alunos de uma disciplina (cod.Disciplina, ano, semestre)                //
//       - Listar disciplinas de um aluno (RA, ano, semestre)                             //
// Autores: Gabriela Marangoni Radigonda e Juliano Kendyi Shinohara                       //
// Data de criação: 15/10/2022                                                            //
// Datas de atualizações:20/10/2022                                                       //
//                       15/12/2022                                                       //
//                                                                                        //
////////////////////////////////////////////////////////////////////////////////////////////

import io.grpc.stub.StreamObserver;
import java.sql.*;

public class GerenciadorDeNotasImpl extends GerenciadorDeNotasGrpc.GerenciadorDeNotasImplBase {
    // conecta com o banco de dados
    static final Connection connection = connect();

    // cria conexão com o banco de dados
    public static Connection connect() {
        Connection conn = null;

        try {
            // Parâmetros do banco de dados
            String url = "jdbc:sqlite:../database_com_dados-contrib-Daniel-Farina.db";

            // Cria uma conexão com o banco de dados
            conn = DriverManager.getConnection(url);

        } catch (SQLException e) {
            // Caso não consiga se conectar
            System.out.println(e.getMessage());
        }

        return conn;
    }

    @Override
    // Metodo que lista os alunos de uma disciplina
    public void listarAlunos(ListarAlunosRequest request, StreamObserver<ListarAlunosResponse> responseObserver) {
        // Cria o builder de resposta
        ListarAlunosResponse.Builder response = ListarAlunosResponse.newBuilder();
        try {
            // cria um statement para realizar a consulta
            Statement statement = connection.createStatement();
            // busca todos os alunos matriculados na disciplina
            ResultSet rs = statement
                    .executeQuery("SELECT a.* FROM matricula m INNER JOIN aluno a ON (a.ra = m.ra) WHERE '"
                            + String.valueOf(request.getCodigoDisciplina()) + "' = cod_disciplina AND "
                            + request.getAno() + " = ano AND " + request.getSemestre() + " = semestre;");
            // caso não encontre nenhum aluno
            if (!rs.isBeforeFirst()) {
                // joga uma exceção
                throw new SQLException("Não há alunos matriculados nessa disciplina");
            }
            // cria um objeto para a resposta
            while (rs.next()) {
                int ra = rs.getInt("ra");
                String nome = rs.getString("nome");
                int periodo = rs.getInt("periodo");
                response.addAlunos(
                        ListarAlunosResponse.Aluno.newBuilder().setNome(nome).setRa(ra).setPeriodo(periodo).build());
            }

        }
        // caso ocorra um erro
        catch (SQLException e) {
            response.setMensagem(e.getMessage());
        }
        // monta e envia a resposta
        ListarAlunosResponse res = response.build();
        responseObserver.onNext(res);
        responseObserver.onCompleted();
    }

    @Override
    // Metodo que altera a nota de um aluno em uma disciplina
    public void alterarNota(AlterarNotaRequest request, StreamObserver<AlterarNotaResponse> responseObserver) {
        AlterarNotaResponse.Builder response = AlterarNotaResponse.newBuilder();
        // tneta executar
        try {
            // cria um statement para realizar a consulta
            Statement statement = connection.createStatement();
            // verifica se o aluno está matriculado na disciplina
            ResultSet rs = statement.executeQuery("SELECT * FROM matricula WHERE ra = " + request.getRa() + " AND '"
                    + String.valueOf(request.getCodigoDisciplina()) + "' = cod_disciplina AND " + request.getAno()
                    + " = ano AND " + request.getSemestre() + " = semestre;");
            // caso não esteja matriculado
            if (!rs.isBeforeFirst()) {
                // joga uma exceção
                throw new SQLException("O aluno não foi encontrado na disciplina informada");
            }
            // atualiza a nota
            statement.execute("UPDATE matricula SET nota = " + request.getNota() + " WHERE ra =" + request.getRa()
                    + " AND cod_disciplina = '" + String.valueOf(request.getCodigoDisciplina()) + "' AND ano = "
                    + request.getAno() + " AND semestre = " + request.getSemestre() + ";");
            // busca novamente a nota para retornar o aluno com a nota atualizada
            rs = statement.executeQuery("SELECT * FROM matricula WHERE ra = " + request.getRa() + " AND '"
                    + String.valueOf(request.getCodigoDisciplina()) + "' = cod_disciplina AND " + request.getAno()
                    + " = ano AND " + request.getSemestre() + " = semestre;");
            // cria um objeto para a resposta
            response.setRa(rs.getInt("ra"));
            response.setAno(rs.getInt("ano"));
            response.setSemestre(rs.getInt("semestre"));
            response.setCodigoDisciplina(rs.getString("cod_disciplina"));
            response.setNota(rs.getFloat("nota"));
        }
        // caso ocorra um erro
        catch (SQLException e) {
            response.setMensagem(e.getMessage());
        }
        // monta e envia a resposta
        AlterarNotaResponse res = response.build();
        responseObserver.onNext(res);
        responseObserver.onCompleted();
    }

    @Override
    public void alterarFaltas(AlterarFaltasRequest request, StreamObserver<AlterarFaltasResponse> responseObserver) {
        AlterarFaltasResponse.Builder response = AlterarFaltasResponse.newBuilder();
        // tenta executar
        try {
            // cria um statement para realizar a consulta
            Statement statement = connection.createStatement();
            // verificar se o aluno está matriculado na disciplina
            ResultSet rs = statement.executeQuery("SELECT * FROM matricula WHERE ra = " + request.getRa() + " AND '"
                    + String.valueOf(request.getCodigoDisciplina()) + "' = cod_disciplina AND " + request.getAno()
                    + " = ano AND " + request.getSemestre() + " = semestre;");
            // caso não esteja, retornar mensagem de erro
            if (!rs.isBeforeFirst()) {
                // joga uma exceção
                throw new SQLException("O aluno não foi encontrado na disciplina informada");
            }
            // atualiza as faltas
            statement.execute("UPDATE matricula SET faltas = " + request.getFaltas() + " WHERE ra =" + request.getRa()
                    + " AND cod_disciplina = '" + String.valueOf(request.getCodigoDisciplina()) + "' AND ano = "
                    + request.getAno() + " AND semestre = " + request.getSemestre() + ";");
            // busca novamente a nota para retornar o aluno com as faltas atualizadas
            rs = statement.executeQuery("SELECT * FROM matricula WHERE ra = " + request.getRa() + " AND '"
                    + String.valueOf(request.getCodigoDisciplina()) + "' = cod_disciplina AND " + request.getAno()
                    + " = ano AND " + request.getSemestre() + " = semestre;");
            // cria o objeto response
            response.setRa(rs.getInt("ra"));
            response.setAno(rs.getInt("ano"));
            response.setSemestre(rs.getInt("semestre"));
            response.setCodigoDisciplina(rs.getString("cod_disciplina"));
            response.setFaltas(rs.getInt("faltas"));
        }
        // caso ocorra um erro
        catch (SQLException e) {
            response.setMensagem(e.getMessage());
        }
        // monta e envia a resposta
        AlterarFaltasResponse res = response.build();
        responseObserver.onNext(res);
        responseObserver.onCompleted();
    }

    @Override
    public void listarDisciplinasAluno(ListarDisciplinasAlunoRequest request,
            StreamObserver<ListarDisciplinasAlunoResponse> responseObserver) {
        // cria um builder para a resposta
        ListarDisciplinasAlunoResponse.Builder response = ListarDisciplinasAlunoResponse.newBuilder();
        // tenta executar
        try {
            // cria um statement
            Statement statement = connection.createStatement();
            // busca as disciplinas do aluno com base no ra e ano e semestre
            ResultSet rs = statement.executeQuery("SELECT * FROM matricula WHERE " + request.getRa() + " = ra AND "
                    + request.getAno() + " = ano AND " + request.getSemestre() + " = semestre;");
            // se não houver nenhum resultado
            if (!rs.isBeforeFirst()) {
                // joga uma exceção
                throw new SQLException(
                        "O aluno informado não está cadastrado em nenhuma disciplina no ano e semetre informados");
            }
            // cria um objeto para a resposta /* enfase na diferença entre add e set */
            while (rs.next()) {
                String codigoDisciplinaResult = rs.getString("cod_disciplina");
                float nota = rs.getFloat("nota");
                int faltas = rs.getInt("faltas");
                response.addDisciplinas(
                        ListarDisciplinasAlunoResponse.DisciplinaAlunos.newBuilder().setRa(request.getRa())
                                .setCodigoDisciplina(codigoDisciplinaResult).setNota(nota).setFaltas(faltas).build());
            }

        }
        // caso ocorra algum erro, define a mensagem de erro
        catch (SQLException e) {
            response.setMensagem(e.getMessage());
        }
        // monta e envia a resposta
        ListarDisciplinasAlunoResponse res = response.build();
        responseObserver.onNext(res);
        responseObserver.onCompleted();
    }

    @Override
    public void inserirMatricula(InserirMatriculaRequest request,
            StreamObserver<InserirMatriculaResponse> responseObserver) {
        // cria um builder para a resposta
        InserirMatriculaResponse.Builder response = InserirMatriculaResponse.newBuilder();
        // tenta executar
        try {
            // cria um statement
            Statement statement = connection.createStatement();
            // verifica se a disciplina existe
            ResultSet rs = statement.executeQuery("SELECT * FROM disciplina WHERE '"
                    + String.valueOf(request.getMatricula().getCodigoDisciplina()) + "' = codigo;");
            // caso não encontre a disciplina, retorna mensagem de erro
            if (!rs.isBeforeFirst()) {
                // joga uma exceção
                throw new SQLException("A disciplina informada não existe");
            }

            // verifica se o aluno existe
            rs = statement.executeQuery("SELECT * FROM aluno WHERE " + request.getMatricula().getRa() + " = ra;");
            // caso não exista, define a mensagem de erro
            if (!rs.isBeforeFirst()) {
                // joga uma exceção
                throw new SQLException("O aluno informado não existe");
            }

            // verifica se o aluno já está matriculado na disciplina
            rs = statement.executeQuery("SELECT * FROM matricula WHERE " + request.getMatricula().getRa()
                    + " = ra AND '" + String.valueOf(request.getMatricula().getCodigoDisciplina())
                    + "' = cod_disciplina AND " + request.getMatricula().getAno() + " = ano AND "
                    + request.getMatricula().getSemestre() + " = semestre;");
            // caso esteja matriculado, retorna mensagem de erro
            if (rs.isBeforeFirst()) {
                // joga uma exceção
                throw new SQLException("O aluno já está matriculado nessa disciplina");
            }

            // executa a inserção na tabela matricula
            statement.execute("INSERT INTO matricula (ra, cod_disciplina, ano, semestre, nota, faltas) VALUES ("
                    + request.getMatricula().getRa() + ", '"
                    + String.valueOf(request.getMatricula().getCodigoDisciplina()) + "', "
                    + request.getMatricula().getAno() + ", " + request.getMatricula().getSemestre() + ", 0, 0);");
            // executa a query para verificar se a matricula foi inserida
            rs = statement.executeQuery("SELECT * FROM matricula WHERE " + request.getMatricula().getRa()
                    + " = ra AND '" + String.valueOf(request.getMatricula().getCodigoDisciplina())
                    + "' = cod_disciplina AND " + request.getMatricula().getAno() + " = ano AND "
                    + request.getMatricula().getSemestre() + " = semestre;");
            // verifica se a resposta é vazia
            if (!rs.isBeforeFirst()) {
                // joga uma exceção
                throw new SQLException("Não foi possível realizar a matrícula");
            }
            // cria o objeto de resposta
            while (rs.next()) {
                int raResult = rs.getInt("ra");
                int anoResult = rs.getInt("ano");
                int semestreResult = rs.getInt("semestre");
                String codigoDisciplinaResult = rs.getString("cod_disciplina");
                float notaResult = rs.getFloat("nota");
                int faltasResult = rs.getInt("faltas");
                response.setMatricula(Matricula.newBuilder().setRa(raResult).setAno(anoResult)
                        .setSemestre(semestreResult).setCodigoDisciplina(codigoDisciplinaResult).setNota(notaResult)
                        .setFaltas(faltasResult).build());
            }

        }
        // caso ocorra algum erro, define a mensagem de erro
        catch (SQLException e) {
            // mostrar a mensagem de erro
            response.setMensagem(e.getMessage());
        }
        // monta e envia a resposta
        InserirMatriculaResponse res = response.build();
        responseObserver.onNext(res);
        responseObserver.onCompleted();
    }
}
