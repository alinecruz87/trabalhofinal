import PySimpleGUI as gui
import Voluntario as Voluntario

class FormVoluntario:
    def __init__(self):
        conteudo = [

            [ gui.Text("Nome: ") , gui.Input() ] ,
            [ gui.Text("Endereco: ") , gui.Input() ] ,
            [ gui.Text("Telefone: ") , gui.Input() ] ,
            [ gui.Text("CPF: ") , gui.Input() ] ,
            [ gui.Checkbox("Possui automovel: ", key='possuiautomovel') ] ,
            
            [ gui.Button("Salvar") ]
        ]
        self.tela = gui.Window("Formulario de Voluntário").layout(conteudo)

    def show(self):
        self.button , self.valores = self.tela.Read()
        nome = self.valores[0]
        endereco = self.valores[1]
        telefone = self.valores[2]
        cpf = self.valores[3]
        automovel = self.valores[4]
        automovel = bool (automovel)

        if len( nome ) != 0:
            voluntario = Voluntario()
            voluntario.nomeV = nome
            voluntario.enderecoV = endereco
            voluntario.telefoneV = telefone
            voluntario.cpfV = cpf
            voluntario.automovel = automovel

            return voluntario
        else: 
            return None
