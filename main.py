from fabrica_fila import FabricaFila


# update_fila = FilaNormal()
#
# update_fila.atualiza_fila()
# update_fila.atualiza_fila()
# update_fila.atualiza_fila()
# print(update_fila.chama_cliente(7))
# print(update_fila.chama_cliente(12))
# print(update_fila.estatistica('31/03/2022', 198, 'detail'))

teste_fabrica = FabricaFila.pega_fila('normal')
teste_fabrica.atualiza_fila()
teste_fabrica.atualiza_fila()
teste_fabrica.atualiza_fila()
print(teste_fabrica.chama_cliente(7))
print(teste_fabrica.chama_cliente(10))
print(teste_fabrica.chama_cliente(12))