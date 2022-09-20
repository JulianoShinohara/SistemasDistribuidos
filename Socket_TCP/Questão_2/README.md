# SocketTCP-SD
Programação com Sockets TCP - Sistemas Distribuídos
## COMO COMPILAR E EXECUTAR
Para compilar, é necessário abrir dois terminais, um para rodar o servidor e outro para rodar o cliente
Digite no terminal 1:
```
python TCP_servidor.py
```
Digite no terminal 2:
```
python TCP_cliente.py
```
## EXEMPLOS DE USO
Para utilizar o programa basta digitar algumas dessas opções no terminal 2: ADDFILE / DELETE / GETFILESLIST / GETFILE.
- EXEMPLOS e suas funcionalidades:
```
ADDFILE <arquivo>
```
O comando adiciona um arquivo da pasta '/files' para a pasta '/archiveServer'

```
DELETE <arquivo>
```
O comando deleta o arquivo que existe dentro da pasta '/archiveServer'

```
GETFILESLIST
```
O comando faz a listagem dos arquivos que existe dentro da pasta '/archiveServer'

```
GETFILE <arquivo>
```
O comando realiza o download do arquivo que está na pasta '/archiveServer' para a pasta '/files'
## BIBLIOTECAS UTILIZADAS
- socket: Usada para a conexão TCP;
- logging: Usada para criar logs;
- os: Usada para funcionalidades simples que necessita do sistema operacional;
- threading: Usada para interface usando o módulo _thread;



