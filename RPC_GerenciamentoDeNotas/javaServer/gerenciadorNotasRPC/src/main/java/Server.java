import io.grpc.BindableService;
import io.grpc.ServerBuilder;

public class Server {
    public static void main(String[] args) {
        io.grpc.Server server = ServerBuilder
                .forPort(6000)
                .addService((BindableService) new GerenciadorDeNotasImpl())
                .build();

        try {
            server.start();
            System.out.println("Servidor iniciado.");
            server.awaitTermination();
        } catch (Exception e) {
            System.err.println("Erro: " + e);
        }

    }
}
