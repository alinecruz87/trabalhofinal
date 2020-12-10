import PySimpleGUI as gui
from Entrega import Entrega

class FormEntrega:
    def __init__(self):
        conteudo = [

            [ gui.Text("ID Voluntario: ") , gui.Input() ] ,
            [ gui.Text("ID Diarista: ") , gui.Input() ] ,
            [ gui.Text("Quantidade entregue: ") , gui.Input() ] ,

            [ gui.Button("Salvar") ]
        ]
        self.tela = gui.Window("Formulario de Entregass").layout(conteudo)

    def show(self):
        self.button , self.valores = self.tela.Read()
        id_v = self.valores[0]
        id_d = self.valores[1]
        qtde_entregue = self.valores[2]
        

        if  id_v != null:
            entrega = Entrega()
            entrega.id_v = id_v
            entrega.id_d = id_d
            entrega.qtde_entregue = qtde_entregue
            
            
            return entrega
        else:
            return None