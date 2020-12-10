from Pessoa import Pessoa

class Voluntario(Pessoa):
    def __init__(self, nomeV = None, enderecoV = None, telefoneV = None, cpfV = None, automovel = None):
        Pessoa.__init__(self, nomeV, enderecoV, telefoneV, cpfV)
        self.automovel = automovel
