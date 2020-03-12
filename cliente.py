from  tipocliente import  TipoCliente
from  notafiscalvenda import  NotaFiscalVenda

class Cliente(TipoCliente,NotaFiscalVenda):
    def __init__(self, id, nome, codigo, cnpjcpf, tipo):
        super().__init__(tipo,codigo)
        self._id = id
        self._nome = nome
        self._cnpjcpf = cnpjcpf
    def Cliente(self):
        pass
    def toString(self):
        pass
