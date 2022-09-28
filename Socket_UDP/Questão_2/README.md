# SocketUDP-SD
Programação com Sockets UDP - Sistemas Distribuídos
## COMO COMPILAR E EXECUTAR
Para compilar, é necessário abrir dois terminais, um para rodar o servidor e outro para rodar o cliente
Digite no terminal 1:
```
python server.py
```
Digite no terminal 2:
```
python client.py
```
## EXEMPLOS DE USO
Para utilizar o programa basta apenas escrever o nome do arquivo que deseja fazer o upload:

```
teste.pdf
```
Após realizar o comando o arquivo deve fazer o upload e ir direto para a pasta "./archiveServer
## BIBLIOTECAS UTILIZADAS
- socket: Usada para a conexão TCP;
- logging: Usada para criar logs;
- os: Usada para funcionalidades simples que necessita do sistema operacional;
- threading: Usada para interface usando o módulo _thread;
- math: usada para a parte matemática;
- hashlib: Usada para criptografar/tratar as mensagens e senha;


