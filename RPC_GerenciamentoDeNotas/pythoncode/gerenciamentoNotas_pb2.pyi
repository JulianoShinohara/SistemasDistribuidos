from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AlterarFaltasRequest(_message.Message):
    __slots__ = ["ano", "codigoDisciplina", "faltas", "ra", "semestre"]
    ANO_FIELD_NUMBER: _ClassVar[int]
    CODIGODISCIPLINA_FIELD_NUMBER: _ClassVar[int]
    FALTAS_FIELD_NUMBER: _ClassVar[int]
    RA_FIELD_NUMBER: _ClassVar[int]
    SEMESTRE_FIELD_NUMBER: _ClassVar[int]
    ano: int
    codigoDisciplina: str
    faltas: int
    ra: int
    semestre: int
    def __init__(self, ra: _Optional[int] = ..., codigoDisciplina: _Optional[str] = ..., ano: _Optional[int] = ..., semestre: _Optional[int] = ..., faltas: _Optional[int] = ...) -> None: ...

class AlterarFaltasResponse(_message.Message):
    __slots__ = ["ano", "codigoDisciplina", "faltas", "mensagem", "ra", "semestre"]
    ANO_FIELD_NUMBER: _ClassVar[int]
    CODIGODISCIPLINA_FIELD_NUMBER: _ClassVar[int]
    FALTAS_FIELD_NUMBER: _ClassVar[int]
    MENSAGEM_FIELD_NUMBER: _ClassVar[int]
    RA_FIELD_NUMBER: _ClassVar[int]
    SEMESTRE_FIELD_NUMBER: _ClassVar[int]
    ano: int
    codigoDisciplina: str
    faltas: int
    mensagem: str
    ra: int
    semestre: int
    def __init__(self, ra: _Optional[int] = ..., codigoDisciplina: _Optional[str] = ..., ano: _Optional[int] = ..., semestre: _Optional[int] = ..., faltas: _Optional[int] = ..., mensagem: _Optional[str] = ...) -> None: ...

class AlterarNotaRequest(_message.Message):
    __slots__ = ["ano", "codigoDisciplina", "nota", "ra", "semestre"]
    ANO_FIELD_NUMBER: _ClassVar[int]
    CODIGODISCIPLINA_FIELD_NUMBER: _ClassVar[int]
    NOTA_FIELD_NUMBER: _ClassVar[int]
    RA_FIELD_NUMBER: _ClassVar[int]
    SEMESTRE_FIELD_NUMBER: _ClassVar[int]
    ano: int
    codigoDisciplina: str
    nota: float
    ra: int
    semestre: int
    def __init__(self, ra: _Optional[int] = ..., codigoDisciplina: _Optional[str] = ..., ano: _Optional[int] = ..., semestre: _Optional[int] = ..., nota: _Optional[float] = ...) -> None: ...

class AlterarNotaResponse(_message.Message):
    __slots__ = ["ano", "codigoDisciplina", "mensagem", "nota", "ra", "semestre"]
    ANO_FIELD_NUMBER: _ClassVar[int]
    CODIGODISCIPLINA_FIELD_NUMBER: _ClassVar[int]
    MENSAGEM_FIELD_NUMBER: _ClassVar[int]
    NOTA_FIELD_NUMBER: _ClassVar[int]
    RA_FIELD_NUMBER: _ClassVar[int]
    SEMESTRE_FIELD_NUMBER: _ClassVar[int]
    ano: int
    codigoDisciplina: str
    mensagem: str
    nota: float
    ra: int
    semestre: int
    def __init__(self, ra: _Optional[int] = ..., codigoDisciplina: _Optional[str] = ..., ano: _Optional[int] = ..., semestre: _Optional[int] = ..., nota: _Optional[float] = ..., mensagem: _Optional[str] = ...) -> None: ...

class InserirMatriculaRequest(_message.Message):
    __slots__ = ["matricula"]
    MATRICULA_FIELD_NUMBER: _ClassVar[int]
    matricula: Matricula
    def __init__(self, matricula: _Optional[_Union[Matricula, _Mapping]] = ...) -> None: ...

class InserirMatriculaResponse(_message.Message):
    __slots__ = ["matricula", "mensagem"]
    MATRICULA_FIELD_NUMBER: _ClassVar[int]
    MENSAGEM_FIELD_NUMBER: _ClassVar[int]
    matricula: Matricula
    mensagem: str
    def __init__(self, matricula: _Optional[_Union[Matricula, _Mapping]] = ..., mensagem: _Optional[str] = ...) -> None: ...

class ListarAlunosRequest(_message.Message):
    __slots__ = ["ano", "codigoDisciplina", "semestre"]
    ANO_FIELD_NUMBER: _ClassVar[int]
    CODIGODISCIPLINA_FIELD_NUMBER: _ClassVar[int]
    SEMESTRE_FIELD_NUMBER: _ClassVar[int]
    ano: int
    codigoDisciplina: str
    semestre: int
    def __init__(self, codigoDisciplina: _Optional[str] = ..., ano: _Optional[int] = ..., semestre: _Optional[int] = ...) -> None: ...

class ListarAlunosResponse(_message.Message):
    __slots__ = ["alunos", "mensagem"]
    class Aluno(_message.Message):
        __slots__ = ["nome", "periodo", "ra"]
        NOME_FIELD_NUMBER: _ClassVar[int]
        PERIODO_FIELD_NUMBER: _ClassVar[int]
        RA_FIELD_NUMBER: _ClassVar[int]
        nome: str
        periodo: int
        ra: int
        def __init__(self, ra: _Optional[int] = ..., nome: _Optional[str] = ..., periodo: _Optional[int] = ...) -> None: ...
    ALUNOS_FIELD_NUMBER: _ClassVar[int]
    MENSAGEM_FIELD_NUMBER: _ClassVar[int]
    alunos: _containers.RepeatedCompositeFieldContainer[ListarAlunosResponse.Aluno]
    mensagem: str
    def __init__(self, alunos: _Optional[_Iterable[_Union[ListarAlunosResponse.Aluno, _Mapping]]] = ..., mensagem: _Optional[str] = ...) -> None: ...

class ListarDisciplinasAlunoRequest(_message.Message):
    __slots__ = ["ano", "ra", "semestre"]
    ANO_FIELD_NUMBER: _ClassVar[int]
    RA_FIELD_NUMBER: _ClassVar[int]
    SEMESTRE_FIELD_NUMBER: _ClassVar[int]
    ano: int
    ra: int
    semestre: int
    def __init__(self, ra: _Optional[int] = ..., ano: _Optional[int] = ..., semestre: _Optional[int] = ...) -> None: ...

class ListarDisciplinasAlunoResponse(_message.Message):
    __slots__ = ["disciplinas", "mensagem"]
    class DisciplinaAlunos(_message.Message):
        __slots__ = ["codigoDisciplina", "faltas", "nota", "ra"]
        CODIGODISCIPLINA_FIELD_NUMBER: _ClassVar[int]
        FALTAS_FIELD_NUMBER: _ClassVar[int]
        NOTA_FIELD_NUMBER: _ClassVar[int]
        RA_FIELD_NUMBER: _ClassVar[int]
        codigoDisciplina: str
        faltas: int
        nota: float
        ra: int
        def __init__(self, ra: _Optional[int] = ..., codigoDisciplina: _Optional[str] = ..., nota: _Optional[float] = ..., faltas: _Optional[int] = ...) -> None: ...
    DISCIPLINAS_FIELD_NUMBER: _ClassVar[int]
    MENSAGEM_FIELD_NUMBER: _ClassVar[int]
    disciplinas: _containers.RepeatedCompositeFieldContainer[ListarDisciplinasAlunoResponse.DisciplinaAlunos]
    mensagem: str
    def __init__(self, disciplinas: _Optional[_Iterable[_Union[ListarDisciplinasAlunoResponse.DisciplinaAlunos, _Mapping]]] = ..., mensagem: _Optional[str] = ...) -> None: ...

class Matricula(_message.Message):
    __slots__ = ["ano", "codigoDisciplina", "faltas", "nota", "ra", "semestre"]
    ANO_FIELD_NUMBER: _ClassVar[int]
    CODIGODISCIPLINA_FIELD_NUMBER: _ClassVar[int]
    FALTAS_FIELD_NUMBER: _ClassVar[int]
    NOTA_FIELD_NUMBER: _ClassVar[int]
    RA_FIELD_NUMBER: _ClassVar[int]
    SEMESTRE_FIELD_NUMBER: _ClassVar[int]
    ano: int
    codigoDisciplina: str
    faltas: int
    nota: float
    ra: int
    semestre: int
    def __init__(self, ra: _Optional[int] = ..., codigoDisciplina: _Optional[str] = ..., ano: _Optional[int] = ..., semestre: _Optional[int] = ..., faltas: _Optional[int] = ..., nota: _Optional[float] = ...) -> None: ...
