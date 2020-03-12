from itemnotafiscal import ItemNotaFiscal
class Produto(ItemNotaFiscal):
    def __init__(self, codigo, descricao, valor):
        super()._init_(valor)
        self._codigo = codigo
        self._descricao = descricao
        self._valor = valor
    def Produto(self):
        pass
    def toString(self):
        pass
