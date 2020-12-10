from Estoque import Estoque

class Entrega(Estoque):
    def __init__(self, id_v = None, id_d = None, qtde_cesta = None, estoqueE = estoque):
        self.id_v = id_v
        self.id_d = id_d
        self.qtde_cesta = qtde_cesta
        Estoque.__init__(self, estoqueE) 
        

    @staticmethod
    def toEstoqueE(estoqueE, qtde_cesta):
        total = estoqueE - qtde_cesta
        return total
