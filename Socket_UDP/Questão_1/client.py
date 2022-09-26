################################################################################################################# 
# Questão 1 - UDP CLIENT                                                                                        #                                                                              #
# Descrição: Fazer um chat P2P que possibilite os clientes trocarem mensagens entre si                          #
#                                                                                                               #   
#   - tipo de mensagem [ 1 byte ]                                                                               #
#   - tamanho apelido (tam_apl) [ 1 byte ]                                                                      #
#   - apelido [ tam_apl ( 1 a 64 ) bytes]                                                                       #
#   - tamanho mensagem ( tam_msg ) [ 1 byte ]                                                                   #
#   - mensagem [ tam_msg bytes ]                                                                                #
#                                                                                                               #
#   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+                                             #
#   | Messagem Type | Nick Size | Nick [ Nick Size] ( 1-64 bytes) |                                             #
#   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+                                             #
#   | Messagem Type |   Message [ Message Size] ( 0-255 bytes)    |                                             #
#   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+    
# Autores: Gabriela Marangoni Radigonda e Juliano Kendyi Shinohara                                              #
# Data de criação: 23/09/2022                                                                                   #
# Data de modificação: 25/09/2022 
#################################################################################################################







