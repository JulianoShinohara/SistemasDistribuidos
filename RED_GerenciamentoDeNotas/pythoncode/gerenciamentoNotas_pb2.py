# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gerenciamentoNotas.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18gerenciamentoNotas.proto\"\x1b\n\x0brequestType\x12\x0c\n\x04type\x18\x01 \x01(\x05\"N\n\x13listarAlunosRequest\x12\x18\n\x10\x63odigoDisciplina\x18\x01 \x01(\t\x12\x0b\n\x03\x61no\x18\x02 \x01(\x05\x12\x10\n\x08semestre\x18\x03 \x01(\x05\"\x89\x01\n\x14listarAlunosResponse\x12+\n\x06\x61lunos\x18\x01 \x03(\x0b\x32\x1b.listarAlunosResponse.Aluno\x12\x10\n\x08mensagem\x18\x02 \x01(\t\x1a\x32\n\x05\x41luno\x12\n\n\x02ra\x18\x01 \x01(\x05\x12\x0c\n\x04nome\x18\x02 \x01(\t\x12\x0f\n\x07periodo\x18\x04 \x01(\x05\"g\n\x12\x61lterarNotaRequest\x12\n\n\x02ra\x18\x01 \x01(\x05\x12\x18\n\x10\x63odigoDisciplina\x18\x02 \x01(\t\x12\x0b\n\x03\x61no\x18\x03 \x01(\x05\x12\x10\n\x08semestre\x18\x04 \x01(\x05\x12\x0c\n\x04nota\x18\x05 \x01(\x02\"z\n\x13\x61lterarNotaResponse\x12\n\n\x02ra\x18\x01 \x01(\x05\x12\x18\n\x10\x63odigoDisciplina\x18\x02 \x01(\t\x12\x0b\n\x03\x61no\x18\x03 \x01(\x05\x12\x10\n\x08semestre\x18\x04 \x01(\x05\x12\x0c\n\x04nota\x18\x05 \x01(\x02\x12\x10\n\x08mensagem\x18\x07 \x01(\t\"k\n\x14\x61lterarFaltasRequest\x12\n\n\x02ra\x18\x01 \x01(\x05\x12\x18\n\x10\x63odigoDisciplina\x18\x02 \x01(\t\x12\x0b\n\x03\x61no\x18\x03 \x01(\x05\x12\x10\n\x08semestre\x18\x04 \x01(\x05\x12\x0e\n\x06\x66\x61ltas\x18\x05 \x01(\x05\"~\n\x15\x61lterarFaltasResponse\x12\n\n\x02ra\x18\x01 \x01(\x05\x12\x18\n\x10\x63odigoDisciplina\x18\x02 \x01(\t\x12\x0b\n\x03\x61no\x18\x03 \x01(\x05\x12\x10\n\x08semestre\x18\x04 \x01(\x05\x12\x0e\n\x06\x66\x61ltas\x18\x05 \x01(\x05\x12\x10\n\x08mensagem\x18\x06 \x01(\t\"J\n\x1dlistarDisciplinasAlunoRequest\x12\n\n\x02ra\x18\x01 \x01(\x05\x12\x0b\n\x03\x61no\x18\x02 \x01(\x05\x12\x10\n\x08semestre\x18\x03 \x01(\x05\"\xd1\x01\n\x1elistarDisciplinasAlunoResponse\x12\x45\n\x0b\x64isciplinas\x18\x01 \x03(\x0b\x32\x30.listarDisciplinasAlunoResponse.DisciplinaAlunos\x12\x10\n\x08mensagem\x18\x02 \x01(\t\x1aV\n\x10\x44isciplinaAlunos\x12\n\n\x02ra\x18\x01 \x01(\x05\x12\x18\n\x10\x63odigoDisciplina\x18\x02 \x01(\t\x12\x0c\n\x04nota\x18\x03 \x01(\x02\x12\x0e\n\x06\x66\x61ltas\x18\x04 \x01(\x05\"8\n\x17inserirMatriculaRequest\x12\x1d\n\tmatricula\x18\x01 \x01(\x0b\x32\n.Matricula\"\x8c\x01\n\tMatricula\x12\n\n\x02ra\x18\x01 \x01(\x05\x12\x18\n\x10\x63odigoDisciplina\x18\x02 \x01(\t\x12\x0b\n\x03\x61no\x18\x03 \x01(\x05\x12\x10\n\x08semestre\x18\x04 \x01(\x05\x12\x11\n\x04nota\x18\x05 \x01(\x02H\x00\x88\x01\x01\x12\x13\n\x06\x66\x61ltas\x18\x06 \x01(\x05H\x01\x88\x01\x01\x42\x07\n\x05_notaB\t\n\x07_faltas\"K\n\x18inserirMatriculaResponse\x12\x1d\n\tmatricula\x18\x01 \x01(\x0b\x32\n.Matricula\x12\x10\n\x08mensagem\x18\x02 \x01(\tb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'gerenciamentoNotas_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _REQUESTTYPE._serialized_start=28
  _REQUESTTYPE._serialized_end=55
  _LISTARALUNOSREQUEST._serialized_start=57
  _LISTARALUNOSREQUEST._serialized_end=135
  _LISTARALUNOSRESPONSE._serialized_start=138
  _LISTARALUNOSRESPONSE._serialized_end=275
  _LISTARALUNOSRESPONSE_ALUNO._serialized_start=225
  _LISTARALUNOSRESPONSE_ALUNO._serialized_end=275
  _ALTERARNOTAREQUEST._serialized_start=277
  _ALTERARNOTAREQUEST._serialized_end=380
  _ALTERARNOTARESPONSE._serialized_start=382
  _ALTERARNOTARESPONSE._serialized_end=504
  _ALTERARFALTASREQUEST._serialized_start=506
  _ALTERARFALTASREQUEST._serialized_end=613
  _ALTERARFALTASRESPONSE._serialized_start=615
  _ALTERARFALTASRESPONSE._serialized_end=741
  _LISTARDISCIPLINASALUNOREQUEST._serialized_start=743
  _LISTARDISCIPLINASALUNOREQUEST._serialized_end=817
  _LISTARDISCIPLINASALUNORESPONSE._serialized_start=820
  _LISTARDISCIPLINASALUNORESPONSE._serialized_end=1029
  _LISTARDISCIPLINASALUNORESPONSE_DISCIPLINAALUNOS._serialized_start=943
  _LISTARDISCIPLINASALUNORESPONSE_DISCIPLINAALUNOS._serialized_end=1029
  _INSERIRMATRICULAREQUEST._serialized_start=1031
  _INSERIRMATRICULAREQUEST._serialized_end=1087
  _MATRICULA._serialized_start=1090
  _MATRICULA._serialized_end=1230
  _INSERIRMATRICULARESPONSE._serialized_start=1232
  _INSERIRMATRICULARESPONSE._serialized_end=1307
# @@protoc_insertion_point(module_scope)
