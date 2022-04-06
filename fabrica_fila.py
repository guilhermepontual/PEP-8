from fila_normal import FilaNormal
from constantes import TIPO_FILA_NORMAL
from typing import Union


class FabricaFila:
    @staticmethod
    def pega_fila(tipo_fila) -> Union[FilaNormal]:
        if tipo_fila == TIPO_FILA_NORMAL:
            return FilaNormal()
        else:
            raise NotImplementedError('Tipo de fila não existe!')
