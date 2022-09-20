# SocketTCP-SD
Programação com Sockets TCP - Sistemas Distribuídos
## COMO COMPILAR
Para compilar, é necessário abrir dois terminais, um para rodar o servidor e outro para rodar o cliente
Digite no terminal 1:
```
python TCP_servidor.py
```
Digite no terminal 2:
```
python TCP_cliente.py
```
## COMO EXECUTAR
Para executar o programa é necessário digitar no terminal 2 o seguinte comando:
```
CONNECT Gaby 1234
```
Depois pode ser escolhido as seguintes opções: GETFILES / GETDIRS / PWD / CHDIR / EXIT
## BIBLIOTECAS UTILIZADAS
- socket: Usada para a conexão TCP;
- hashlib: Usada para criptografar/tratar as mensagens e senha;
- logging: Usada para criar logs;
- os: Usada para funcionalidades simples que necessita do sistema operacional;
- threading: Usada para interface usando o módulo _thread.

## EXEMPLOS DE USO
- Primeiro se faz necessário se conectar no servidor (terminal 2):
```
CONNECT Gaby 1234
```
Se a conexão deu certo irá aparecer no terminal da seguinte maneira "Connection: SUCCESS", caso ao contrário "Connection: ERROR".

- Após isso, pode ser digitada as seguintes opções: GETFILES / GETDIRS / PWD / CHDIR / EXIT. Iremos escolher a opção GETFILES, então iremos digitar o seguinte comando:
```
GETFILES
```
Após o comando ser enviado, será exibido no terminal todos os arquivos do diretório atual.