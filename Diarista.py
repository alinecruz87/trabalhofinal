from Pessoa import Pessoa

class Diarista(Pessoa):
    def __init__(self, nomeD = None, enderecoD = None, telefoneD = None, cpfD = None, qte_pessoas = None, ponto_ref = None):
        Pessoa.__init__(self, nomeD, enderecoD, telefoneD, cpfD)
        self.qte_pessoas = qte_pessoas
        self.ponto_ref = ponto_ref