import PySimpleGUI as gui
from Diarista import Diarista

class FormDiarista:
    def __init__(self):
        conteudo = [

            [ gui.Text("Nome: ") , gui.Input() ] ,
            [ gui.Text("Endereco: ") , gui.Input() ] ,
            [ gui.Text("Telefone: ") , gui.Input() ] ,
            [ gui.Text("CPF: ") , gui.Input() ] ,
            [ gui.Text("Quantidade de pessoas: ") , gui.Input() ] ,
            [ gui.Text("Ponto de referencia: ") , gui.Input() ] ,

            [ gui.Button("Salvar") ]
        ]
        self.tela = gui.Window("Formulario de Diaristas").layout(conteudo)

    def show(self):
        self.button , self.valores = self.tela.Read()
        nome = self.valores[0]
        endereco = self.valores[1]
        telefone = self.valores[2]
        cpf = self.valores[3]
        qte_pessoas = self.valores[4]
        ponto_ref = self.valores[5]

        if len( nome ) != 0:
            diarista = Diarista()
            diarista.nomeD = nome
            diarista.enderecoD = endereco
            diarista.telefoneD = telefone
            diarista.cpfD = cpf
            diarista.qte_pessoas = qte_pessoas
            diarista.ponto_ref = ponto_ref
            
            return diarista
        else:
            return None