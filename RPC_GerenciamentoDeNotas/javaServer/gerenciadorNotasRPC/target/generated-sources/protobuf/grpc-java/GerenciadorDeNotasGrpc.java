import static io.grpc.MethodDescriptor.generateFullMethodName;

/**
 * <pre>
 * interface de serviço
 * </pre>
 */
@javax.annotation.Generated(
    value = "by gRPC proto compiler (version 1.50.2)",
    comments = "Source: service.proto")
@io.grpc.stub.annotations.GrpcGenerated
public final class GerenciadorDeNotasGrpc {

  private GerenciadorDeNotasGrpc() {}

  public static final String SERVICE_NAME = "GerenciadorDeNotas";

  // Static method descriptors that strictly reflect the proto.
  private static volatile io.grpc.MethodDescriptor<ListarAlunosRequest,
      ListarAlunosResponse> getListarAlunosMethod;

  @io.grpc.stub.annotations.RpcMethod(
      fullMethodName = SERVICE_NAME + '/' + "ListarAlunos",
      requestType = ListarAlunosRequest.class,
      responseType = ListarAlunosResponse.class,
      methodType = io.grpc.MethodDescriptor.MethodType.UNARY)
  public static io.grpc.MethodDescriptor<ListarAlunosRequest,
      ListarAlunosResponse> getListarAlunosMethod() {
    io.grpc.MethodDescriptor<ListarAlunosRequest, ListarAlunosResponse> getListarAlunosMethod;
    if ((getListarAlunosMethod = GerenciadorDeNotasGrpc.getListarAlunosMethod) == null) {
      synchronized (GerenciadorDeNotasGrpc.class) {
        if ((getListarAlunosMethod = GerenciadorDeNotasGrpc.getListarAlunosMethod) == null) {
          GerenciadorDeNotasGrpc.getListarAlunosMethod = getListarAlunosMethod =
              io.grpc.MethodDescriptor.<ListarAlunosRequest, ListarAlunosResponse>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "ListarAlunos"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  ListarAlunosRequest.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  ListarAlunosResponse.getDefaultInstance()))
              .setSchemaDescriptor(new GerenciadorDeNotasMethodDescriptorSupplier("ListarAlunos"))
              .build();
        }
      }
    }
    return getListarAlunosMethod;
  }

  private static volatile io.grpc.MethodDescriptor<AlterarNotaRequest,
      AlterarNotaResponse> getAlterarNotaMethod;

  @io.grpc.stub.annotations.RpcMethod(
      fullMethodName = SERVICE_NAME + '/' + "AlterarNota",
      requestType = AlterarNotaRequest.class,
      responseType = AlterarNotaResponse.class,
      methodType = io.grpc.MethodDescriptor.MethodType.UNARY)
  public static io.grpc.MethodDescriptor<AlterarNotaRequest,
      AlterarNotaResponse> getAlterarNotaMethod() {
    io.grpc.MethodDescriptor<AlterarNotaRequest, AlterarNotaResponse> getAlterarNotaMethod;
    if ((getAlterarNotaMethod = GerenciadorDeNotasGrpc.getAlterarNotaMethod) == null) {
      synchronized (GerenciadorDeNotasGrpc.class) {
        if ((getAlterarNotaMethod = GerenciadorDeNotasGrpc.getAlterarNotaMethod) == null) {
          GerenciadorDeNotasGrpc.getAlterarNotaMethod = getAlterarNotaMethod =
              io.grpc.MethodDescriptor.<AlterarNotaRequest, AlterarNotaResponse>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "AlterarNota"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  AlterarNotaRequest.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  AlterarNotaResponse.getDefaultInstance()))
              .setSchemaDescriptor(new GerenciadorDeNotasMethodDescriptorSupplier("AlterarNota"))
              .build();
        }
      }
    }
    return getAlterarNotaMethod;
  }

  private static volatile io.grpc.MethodDescriptor<AlterarFaltasRequest,
      AlterarFaltasResponse> getAlterarFaltasMethod;

  @io.grpc.stub.annotations.RpcMethod(
      fullMethodName = SERVICE_NAME + '/' + "AlterarFaltas",
      requestType = AlterarFaltasRequest.class,
      responseType = AlterarFaltasResponse.class,
      methodType = io.grpc.MethodDescriptor.MethodType.UNARY)
  public static io.grpc.MethodDescriptor<AlterarFaltasRequest,
      AlterarFaltasResponse> getAlterarFaltasMethod() {
    io.grpc.MethodDescriptor<AlterarFaltasRequest, AlterarFaltasResponse> getAlterarFaltasMethod;
    if ((getAlterarFaltasMethod = GerenciadorDeNotasGrpc.getAlterarFaltasMethod) == null) {
      synchronized (GerenciadorDeNotasGrpc.class) {
        if ((getAlterarFaltasMethod = GerenciadorDeNotasGrpc.getAlterarFaltasMethod) == null) {
          GerenciadorDeNotasGrpc.getAlterarFaltasMethod = getAlterarFaltasMethod =
              io.grpc.MethodDescriptor.<AlterarFaltasRequest, AlterarFaltasResponse>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "AlterarFaltas"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  AlterarFaltasRequest.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  AlterarFaltasResponse.getDefaultInstance()))
              .setSchemaDescriptor(new GerenciadorDeNotasMethodDescriptorSupplier("AlterarFaltas"))
              .build();
        }
      }
    }
    return getAlterarFaltasMethod;
  }

  private static volatile io.grpc.MethodDescriptor<ListarDisciplinasCursoRequest,
      ListarDisciplinasCursoResponse> getListarDisciplinasCursoMethod;

  @io.grpc.stub.annotations.RpcMethod(
      fullMethodName = SERVICE_NAME + '/' + "ListarDisciplinasCurso",
      requestType = ListarDisciplinasCursoRequest.class,
      responseType = ListarDisciplinasCursoResponse.class,
      methodType = io.grpc.MethodDescriptor.MethodType.UNARY)
  public static io.grpc.MethodDescriptor<ListarDisciplinasCursoRequest,
      ListarDisciplinasCursoResponse> getListarDisciplinasCursoMethod() {
    io.grpc.MethodDescriptor<ListarDisciplinasCursoRequest, ListarDisciplinasCursoResponse> getListarDisciplinasCursoMethod;
    if ((getListarDisciplinasCursoMethod = GerenciadorDeNotasGrpc.getListarDisciplinasCursoMethod) == null) {
      synchronized (GerenciadorDeNotasGrpc.class) {
        if ((getListarDisciplinasCursoMethod = GerenciadorDeNotasGrpc.getListarDisciplinasCursoMethod) == null) {
          GerenciadorDeNotasGrpc.getListarDisciplinasCursoMethod = getListarDisciplinasCursoMethod =
              io.grpc.MethodDescriptor.<ListarDisciplinasCursoRequest, ListarDisciplinasCursoResponse>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "ListarDisciplinasCurso"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  ListarDisciplinasCursoRequest.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  ListarDisciplinasCursoResponse.getDefaultInstance()))
              .setSchemaDescriptor(new GerenciadorDeNotasMethodDescriptorSupplier("ListarDisciplinasCurso"))
              .build();
        }
      }
    }
    return getListarDisciplinasCursoMethod;
  }

  private static volatile io.grpc.MethodDescriptor<ListarDisciplinasAlunoRequest,
      ListarDisciplinasAlunoResponse> getListarDisciplinasAlunoMethod;

  @io.grpc.stub.annotations.RpcMethod(
      fullMethodName = SERVICE_NAME + '/' + "ListarDisciplinasAluno",
      requestType = ListarDisciplinasAlunoRequest.class,
      responseType = ListarDisciplinasAlunoResponse.class,
      methodType = io.grpc.MethodDescriptor.MethodType.UNARY)
  public static io.grpc.MethodDescriptor<ListarDisciplinasAlunoRequest,
      ListarDisciplinasAlunoResponse> getListarDisciplinasAlunoMethod() {
    io.grpc.MethodDescriptor<ListarDisciplinasAlunoRequest, ListarDisciplinasAlunoResponse> getListarDisciplinasAlunoMethod;
    if ((getListarDisciplinasAlunoMethod = GerenciadorDeNotasGrpc.getListarDisciplinasAlunoMethod) == null) {
      synchronized (GerenciadorDeNotasGrpc.class) {
        if ((getListarDisciplinasAlunoMethod = GerenciadorDeNotasGrpc.getListarDisciplinasAlunoMethod) == null) {
          GerenciadorDeNotasGrpc.getListarDisciplinasAlunoMethod = getListarDisciplinasAlunoMethod =
              io.grpc.MethodDescriptor.<ListarDisciplinasAlunoRequest, ListarDisciplinasAlunoResponse>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "ListarDisciplinasAluno"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  ListarDisciplinasAlunoRequest.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  ListarDisciplinasAlunoResponse.getDefaultInstance()))
              .setSchemaDescriptor(new GerenciadorDeNotasMethodDescriptorSupplier("ListarDisciplinasAluno"))
              .build();
        }
      }
    }
    return getListarDisciplinasAlunoMethod;
  }

  private static volatile io.grpc.MethodDescriptor<InserirMatriculaRequest,
      InserirMatriculaResponse> getInserirMatriculaMethod;

  @io.grpc.stub.annotations.RpcMethod(
      fullMethodName = SERVICE_NAME + '/' + "InserirMatricula",
      requestType = InserirMatriculaRequest.class,
      responseType = InserirMatriculaResponse.class,
      methodType = io.grpc.MethodDescriptor.MethodType.UNARY)
  public static io.grpc.MethodDescriptor<InserirMatriculaRequest,
      InserirMatriculaResponse> getInserirMatriculaMethod() {
    io.grpc.MethodDescriptor<InserirMatriculaRequest, InserirMatriculaResponse> getInserirMatriculaMethod;
    if ((getInserirMatriculaMethod = GerenciadorDeNotasGrpc.getInserirMatriculaMethod) == null) {
      synchronized (GerenciadorDeNotasGrpc.class) {
        if ((getInserirMatriculaMethod = GerenciadorDeNotasGrpc.getInserirMatriculaMethod) == null) {
          GerenciadorDeNotasGrpc.getInserirMatriculaMethod = getInserirMatriculaMethod =
              io.grpc.MethodDescriptor.<InserirMatriculaRequest, InserirMatriculaResponse>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "InserirMatricula"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  InserirMatriculaRequest.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  InserirMatriculaResponse.getDefaultInstance()))
              .setSchemaDescriptor(new GerenciadorDeNotasMethodDescriptorSupplier("InserirMatricula"))
              .build();
        }
      }
    }
    return getInserirMatriculaMethod;
  }

  /**
   * Creates a new async stub that supports all call types for the service
   */
  public static GerenciadorDeNotasStub newStub(io.grpc.Channel channel) {
    io.grpc.stub.AbstractStub.StubFactory<GerenciadorDeNotasStub> factory =
      new io.grpc.stub.AbstractStub.StubFactory<GerenciadorDeNotasStub>() {
        @java.lang.Override
        public GerenciadorDeNotasStub newStub(io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
          return new GerenciadorDeNotasStub(channel, callOptions);
        }
      };
    return GerenciadorDeNotasStub.newStub(factory, channel);
  }

  /**
   * Creates a new blocking-style stub that supports unary and streaming output calls on the service
   */
  public static GerenciadorDeNotasBlockingStub newBlockingStub(
      io.grpc.Channel channel) {
    io.grpc.stub.AbstractStub.StubFactory<GerenciadorDeNotasBlockingStub> factory =
      new io.grpc.stub.AbstractStub.StubFactory<GerenciadorDeNotasBlockingStub>() {
        @java.lang.Override
        public GerenciadorDeNotasBlockingStub newStub(io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
          return new GerenciadorDeNotasBlockingStub(channel, callOptions);
        }
      };
    return GerenciadorDeNotasBlockingStub.newStub(factory, channel);
  }

  /**
   * Creates a new ListenableFuture-style stub that supports unary calls on the service
   */
  public static GerenciadorDeNotasFutureStub newFutureStub(
      io.grpc.Channel channel) {
    io.grpc.stub.AbstractStub.StubFactory<GerenciadorDeNotasFutureStub> factory =
      new io.grpc.stub.AbstractStub.StubFactory<GerenciadorDeNotasFutureStub>() {
        @java.lang.Override
        public GerenciadorDeNotasFutureStub newStub(io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
          return new GerenciadorDeNotasFutureStub(channel, callOptions);
        }
      };
    return GerenciadorDeNotasFutureStub.newStub(factory, channel);
  }

  /**
   * <pre>
   * interface de serviço
   * </pre>
   */
  public static abstract class GerenciadorDeNotasImplBase implements io.grpc.BindableService {

    /**
     */
    public void listarAlunos(ListarAlunosRequest request,
        io.grpc.stub.StreamObserver<ListarAlunosResponse> responseObserver) {
      io.grpc.stub.ServerCalls.asyncUnimplementedUnaryCall(getListarAlunosMethod(), responseObserver);
    }

    /**
     */
    public void alterarNota(AlterarNotaRequest request,
        io.grpc.stub.StreamObserver<AlterarNotaResponse> responseObserver) {
      io.grpc.stub.ServerCalls.asyncUnimplementedUnaryCall(getAlterarNotaMethod(), responseObserver);
    }

    /**
     */
    public void alterarFaltas(AlterarFaltasRequest request,
        io.grpc.stub.StreamObserver<AlterarFaltasResponse> responseObserver) {
      io.grpc.stub.ServerCalls.asyncUnimplementedUnaryCall(getAlterarFaltasMethod(), responseObserver);
    }

    /**
     */
    public void listarDisciplinasCurso(ListarDisciplinasCursoRequest request,
        io.grpc.stub.StreamObserver<ListarDisciplinasCursoResponse> responseObserver) {
      io.grpc.stub.ServerCalls.asyncUnimplementedUnaryCall(getListarDisciplinasCursoMethod(), responseObserver);
    }

    /**
     */
    public void listarDisciplinasAluno(ListarDisciplinasAlunoRequest request,
        io.grpc.stub.StreamObserver<ListarDisciplinasAlunoResponse> responseObserver) {
      io.grpc.stub.ServerCalls.asyncUnimplementedUnaryCall(getListarDisciplinasAlunoMethod(), responseObserver);
    }

    /**
     */
    public void inserirMatricula(InserirMatriculaRequest request,
        io.grpc.stub.StreamObserver<InserirMatriculaResponse> responseObserver) {
      io.grpc.stub.ServerCalls.asyncUnimplementedUnaryCall(getInserirMatriculaMethod(), responseObserver);
    }

    @java.lang.Override public final io.grpc.ServerServiceDefinition bindService() {
      return io.grpc.ServerServiceDefinition.builder(getServiceDescriptor())
          .addMethod(
            getListarAlunosMethod(),
            io.grpc.stub.ServerCalls.asyncUnaryCall(
              new MethodHandlers<
                ListarAlunosRequest,
                ListarAlunosResponse>(
                  this, METHODID_LISTAR_ALUNOS)))
          .addMethod(
            getAlterarNotaMethod(),
            io.grpc.stub.ServerCalls.asyncUnaryCall(
              new MethodHandlers<
                AlterarNotaRequest,
                AlterarNotaResponse>(
                  this, METHODID_ALTERAR_NOTA)))
          .addMethod(
            getAlterarFaltasMethod(),
            io.grpc.stub.ServerCalls.asyncUnaryCall(
              new MethodHandlers<
                AlterarFaltasRequest,
                AlterarFaltasResponse>(
                  this, METHODID_ALTERAR_FALTAS)))
          .addMethod(
            getListarDisciplinasCursoMethod(),
            io.grpc.stub.ServerCalls.asyncUnaryCall(
              new MethodHandlers<
                ListarDisciplinasCursoRequest,
                ListarDisciplinasCursoResponse>(
                  this, METHODID_LISTAR_DISCIPLINAS_CURSO)))
          .addMethod(
            getListarDisciplinasAlunoMethod(),
            io.grpc.stub.ServerCalls.asyncUnaryCall(
              new MethodHandlers<
                ListarDisciplinasAlunoRequest,
                ListarDisciplinasAlunoResponse>(
                  this, METHODID_LISTAR_DISCIPLINAS_ALUNO)))
          .addMethod(
            getInserirMatriculaMethod(),
            io.grpc.stub.ServerCalls.asyncUnaryCall(
              new MethodHandlers<
                InserirMatriculaRequest,
                InserirMatriculaResponse>(
                  this, METHODID_INSERIR_MATRICULA)))
          .build();
    }
  }

  /**
   * <pre>
   * interface de serviço
   * </pre>
   */
  public static final class GerenciadorDeNotasStub extends io.grpc.stub.AbstractAsyncStub<GerenciadorDeNotasStub> {
    private GerenciadorDeNotasStub(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected GerenciadorDeNotasStub build(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      return new GerenciadorDeNotasStub(channel, callOptions);
    }

    /**
     */
    public void listarAlunos(ListarAlunosRequest request,
        io.grpc.stub.StreamObserver<ListarAlunosResponse> responseObserver) {
      io.grpc.stub.ClientCalls.asyncUnaryCall(
          getChannel().newCall(getListarAlunosMethod(), getCallOptions()), request, responseObserver);
    }

    /**
     */
    public void alterarNota(AlterarNotaRequest request,
        io.grpc.stub.StreamObserver<AlterarNotaResponse> responseObserver) {
      io.grpc.stub.ClientCalls.asyncUnaryCall(
          getChannel().newCall(getAlterarNotaMethod(), getCallOptions()), request, responseObserver);
    }

    /**
     */
    public void alterarFaltas(AlterarFaltasRequest request,
        io.grpc.stub.StreamObserver<AlterarFaltasResponse> responseObserver) {
      io.grpc.stub.ClientCalls.asyncUnaryCall(
          getChannel().newCall(getAlterarFaltasMethod(), getCallOptions()), request, responseObserver);
    }

    /**
     */
    public void listarDisciplinasCurso(ListarDisciplinasCursoRequest request,
        io.grpc.stub.StreamObserver<ListarDisciplinasCursoResponse> responseObserver) {
      io.grpc.stub.ClientCalls.asyncUnaryCall(
          getChannel().newCall(getListarDisciplinasCursoMethod(), getCallOptions()), request, responseObserver);
    }

    /**
     */
    public void listarDisciplinasAluno(ListarDisciplinasAlunoRequest request,
        io.grpc.stub.StreamObserver<ListarDisciplinasAlunoResponse> responseObserver) {
      io.grpc.stub.ClientCalls.asyncUnaryCall(
          getChannel().newCall(getListarDisciplinasAlunoMethod(), getCallOptions()), request, responseObserver);
    }

    /**
     */
    public void inserirMatricula(InserirMatriculaRequest request,
        io.grpc.stub.StreamObserver<InserirMatriculaResponse> responseObserver) {
      io.grpc.stub.ClientCalls.asyncUnaryCall(
          getChannel().newCall(getInserirMatriculaMethod(), getCallOptions()), request, responseObserver);
    }
  }

  /**
   * <pre>
   * interface de serviço
   * </pre>
   */
  public static final class GerenciadorDeNotasBlockingStub extends io.grpc.stub.AbstractBlockingStub<GerenciadorDeNotasBlockingStub> {
    private GerenciadorDeNotasBlockingStub(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected GerenciadorDeNotasBlockingStub build(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      return new GerenciadorDeNotasBlockingStub(channel, callOptions);
    }

    /**
     */
    public ListarAlunosResponse listarAlunos(ListarAlunosRequest request) {
      return io.grpc.stub.ClientCalls.blockingUnaryCall(
          getChannel(), getListarAlunosMethod(), getCallOptions(), request);
    }

    /**
     */
    public AlterarNotaResponse alterarNota(AlterarNotaRequest request) {
      return io.grpc.stub.ClientCalls.blockingUnaryCall(
          getChannel(), getAlterarNotaMethod(), getCallOptions(), request);
    }

    /**
     */
    public AlterarFaltasResponse alterarFaltas(AlterarFaltasRequest request) {
      return io.grpc.stub.ClientCalls.blockingUnaryCall(
          getChannel(), getAlterarFaltasMethod(), getCallOptions(), request);
    }

    /**
     */
    public ListarDisciplinasCursoResponse listarDisciplinasCurso(ListarDisciplinasCursoRequest request) {
      return io.grpc.stub.ClientCalls.blockingUnaryCall(
          getChannel(), getListarDisciplinasCursoMethod(), getCallOptions(), request);
    }

    /**
     */
    public ListarDisciplinasAlunoResponse listarDisciplinasAluno(ListarDisciplinasAlunoRequest request) {
      return io.grpc.stub.ClientCalls.blockingUnaryCall(
          getChannel(), getListarDisciplinasAlunoMethod(), getCallOptions(), request);
    }

    /**
     */
    public InserirMatriculaResponse inserirMatricula(InserirMatriculaRequest request) {
      return io.grpc.stub.ClientCalls.blockingUnaryCall(
          getChannel(), getInserirMatriculaMethod(), getCallOptions(), request);
    }
  }

  /**
   * <pre>
   * interface de serviço
   * </pre>
   */
  public static final class GerenciadorDeNotasFutureStub extends io.grpc.stub.AbstractFutureStub<GerenciadorDeNotasFutureStub> {
    private GerenciadorDeNotasFutureStub(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected GerenciadorDeNotasFutureStub build(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      return new GerenciadorDeNotasFutureStub(channel, callOptions);
    }

    /**
     */
    public com.google.common.util.concurrent.ListenableFuture<ListarAlunosResponse> listarAlunos(
        ListarAlunosRequest request) {
      return io.grpc.stub.ClientCalls.futureUnaryCall(
          getChannel().newCall(getListarAlunosMethod(), getCallOptions()), request);
    }

    /**
     */
    public com.google.common.util.concurrent.ListenableFuture<AlterarNotaResponse> alterarNota(
        AlterarNotaRequest request) {
      return io.grpc.stub.ClientCalls.futureUnaryCall(
          getChannel().newCall(getAlterarNotaMethod(), getCallOptions()), request);
    }

    /**
     */
    public com.google.common.util.concurrent.ListenableFuture<AlterarFaltasResponse> alterarFaltas(
        AlterarFaltasRequest request) {
      return io.grpc.stub.ClientCalls.futureUnaryCall(
          getChannel().newCall(getAlterarFaltasMethod(), getCallOptions()), request);
    }

    /**
     */
    public com.google.common.util.concurrent.ListenableFuture<ListarDisciplinasCursoResponse> listarDisciplinasCurso(
        ListarDisciplinasCursoRequest request) {
      return io.grpc.stub.ClientCalls.futureUnaryCall(
          getChannel().newCall(getListarDisciplinasCursoMethod(), getCallOptions()), request);
    }

    /**
     */
    public com.google.common.util.concurrent.ListenableFuture<ListarDisciplinasAlunoResponse> listarDisciplinasAluno(
        ListarDisciplinasAlunoRequest request) {
      return io.grpc.stub.ClientCalls.futureUnaryCall(
          getChannel().newCall(getListarDisciplinasAlunoMethod(), getCallOptions()), request);
    }

    /**
     */
    public com.google.common.util.concurrent.ListenableFuture<InserirMatriculaResponse> inserirMatricula(
        InserirMatriculaRequest request) {
      return io.grpc.stub.ClientCalls.futureUnaryCall(
          getChannel().newCall(getInserirMatriculaMethod(), getCallOptions()), request);
    }
  }

  private static final int METHODID_LISTAR_ALUNOS = 0;
  private static final int METHODID_ALTERAR_NOTA = 1;
  private static final int METHODID_ALTERAR_FALTAS = 2;
  private static final int METHODID_LISTAR_DISCIPLINAS_CURSO = 3;
  private static final int METHODID_LISTAR_DISCIPLINAS_ALUNO = 4;
  private static final int METHODID_INSERIR_MATRICULA = 5;

  private static final class MethodHandlers<Req, Resp> implements
      io.grpc.stub.ServerCalls.UnaryMethod<Req, Resp>,
      io.grpc.stub.ServerCalls.ServerStreamingMethod<Req, Resp>,
      io.grpc.stub.ServerCalls.ClientStreamingMethod<Req, Resp>,
      io.grpc.stub.ServerCalls.BidiStreamingMethod<Req, Resp> {
    private final GerenciadorDeNotasImplBase serviceImpl;
    private final int methodId;

    MethodHandlers(GerenciadorDeNotasImplBase serviceImpl, int methodId) {
      this.serviceImpl = serviceImpl;
      this.methodId = methodId;
    }

    @java.lang.Override
    @java.lang.SuppressWarnings("unchecked")
    public void invoke(Req request, io.grpc.stub.StreamObserver<Resp> responseObserver) {
      switch (methodId) {
        case METHODID_LISTAR_ALUNOS:
          serviceImpl.listarAlunos((ListarAlunosRequest) request,
              (io.grpc.stub.StreamObserver<ListarAlunosResponse>) responseObserver);
          break;
        case METHODID_ALTERAR_NOTA:
          serviceImpl.alterarNota((AlterarNotaRequest) request,
              (io.grpc.stub.StreamObserver<AlterarNotaResponse>) responseObserver);
          break;
        case METHODID_ALTERAR_FALTAS:
          serviceImpl.alterarFaltas((AlterarFaltasRequest) request,
              (io.grpc.stub.StreamObserver<AlterarFaltasResponse>) responseObserver);
          break;
        case METHODID_LISTAR_DISCIPLINAS_CURSO:
          serviceImpl.listarDisciplinasCurso((ListarDisciplinasCursoRequest) request,
              (io.grpc.stub.StreamObserver<ListarDisciplinasCursoResponse>) responseObserver);
          break;
        case METHODID_LISTAR_DISCIPLINAS_ALUNO:
          serviceImpl.listarDisciplinasAluno((ListarDisciplinasAlunoRequest) request,
              (io.grpc.stub.StreamObserver<ListarDisciplinasAlunoResponse>) responseObserver);
          break;
        case METHODID_INSERIR_MATRICULA:
          serviceImpl.inserirMatricula((InserirMatriculaRequest) request,
              (io.grpc.stub.StreamObserver<InserirMatriculaResponse>) responseObserver);
          break;
        default:
          throw new AssertionError();
      }
    }

    @java.lang.Override
    @java.lang.SuppressWarnings("unchecked")
    public io.grpc.stub.StreamObserver<Req> invoke(
        io.grpc.stub.StreamObserver<Resp> responseObserver) {
      switch (methodId) {
        default:
          throw new AssertionError();
      }
    }
  }

  private static abstract class GerenciadorDeNotasBaseDescriptorSupplier
      implements io.grpc.protobuf.ProtoFileDescriptorSupplier, io.grpc.protobuf.ProtoServiceDescriptorSupplier {
    GerenciadorDeNotasBaseDescriptorSupplier() {}

    @java.lang.Override
    public com.google.protobuf.Descriptors.FileDescriptor getFileDescriptor() {
      return HelloWorldProto.getDescriptor();
    }

    @java.lang.Override
    public com.google.protobuf.Descriptors.ServiceDescriptor getServiceDescriptor() {
      return getFileDescriptor().findServiceByName("GerenciadorDeNotas");
    }
  }

  private static final class GerenciadorDeNotasFileDescriptorSupplier
      extends GerenciadorDeNotasBaseDescriptorSupplier {
    GerenciadorDeNotasFileDescriptorSupplier() {}
  }

  private static final class GerenciadorDeNotasMethodDescriptorSupplier
      extends GerenciadorDeNotasBaseDescriptorSupplier
      implements io.grpc.protobuf.ProtoMethodDescriptorSupplier {
    private final String methodName;

    GerenciadorDeNotasMethodDescriptorSupplier(String methodName) {
      this.methodName = methodName;
    }

    @java.lang.Override
    public com.google.protobuf.Descriptors.MethodDescriptor getMethodDescriptor() {
      return getServiceDescriptor().findMethodByName(methodName);
    }
  }

  private static volatile io.grpc.ServiceDescriptor serviceDescriptor;

  public static io.grpc.ServiceDescriptor getServiceDescriptor() {
    io.grpc.ServiceDescriptor result = serviceDescriptor;
    if (result == null) {
      synchronized (GerenciadorDeNotasGrpc.class) {
        result = serviceDescriptor;
        if (result == null) {
          serviceDescriptor = result = io.grpc.ServiceDescriptor.newBuilder(SERVICE_NAME)
              .setSchemaDescriptor(new GerenciadorDeNotasFileDescriptorSupplier())
              .addMethod(getListarAlunosMethod())
              .addMethod(getAlterarNotaMethod())
              .addMethod(getAlterarFaltasMethod())
              .addMethod(getListarDisciplinasCursoMethod())
              .addMethod(getListarDisciplinasAlunoMethod())
              .addMethod(getInserirMatriculaMethod())
              .build();
        }
      }
    }
    return result;
  }
}
