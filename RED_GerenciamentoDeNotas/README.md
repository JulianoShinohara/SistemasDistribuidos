# Atividade RED - SD
Gerenciamento de Notas - Sistemas Distribuídos
## COMO COMPILAR E EXECUTAR
Para compilar o Servidor Java, é necessário a instalação dos pacotes utilizando o "mvn install" dentro do path: "/javaServer/noteManagement-maven".
Com os pacotes instalados basta executar o comando:
```
mvn exec:java
```
Em outro terminal para executar o Client em Python, apenas executar o comando:
```
python3 client.py
```

## BIBLIOTECAS UTILIZADAS
### Bibliotecas utilizadas no python
- socket: Usada para a conexão TCP;

### Bibliotecas utilizadas no Java
- java.io: usada para permitir que funções realizem entrada e saída
- java.net: usada para permitir que funções realizem conexão TCP
- java.sql: usada para permitir que funções realizem conexão com o BD SQLite

## EXEMPLOS DE USO
Exemplo: Listar alunos

Passos:
1 - No terminal do cliente digite o número <4> para fazer a listagem dos alunos
2 - Em seguida digite 
    > código da disciplica <BCC31A>
    > Ano <2019> 
    > semestre <2>
3 - Feito isso aparecerá a Lista dos alunos