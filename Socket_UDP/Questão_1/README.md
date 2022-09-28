# SocketUDP-SD
Programação com Sockets UDP - Sistemas Distribuídos
## COMO COMPILAR E EXECUTAR
Para compilar, é necessário abrir dois terminais, um para rodar o servidor e outro para rodar o cliente
Digite no terminal 1:
```
python client.py 1
```
Digite no terminal 2:
```
python client.py 2
```
## EXEMPLOS DE USO
Para utilizar o programa é necessário escrever um nome para cada usuário:
Exemplo terminal 1:

```
Gabriela 
```
Type your message:
```
Olá
```
Após escrever a mensagem, a mesma será enviada para usuário 2 e aparecerá da seguinte maneira no terminal 2:

Gabriela >> Olá
## BIBLIOTECAS UTILIZADAS
- socket: Usada para a conexão TCP;
- os: Usada para funcionalidades simples que necessita do sistema operacional;
- threading: Usada para interface usando o módulo _thread;


