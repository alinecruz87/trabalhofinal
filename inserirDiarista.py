# encoding: utf-8
import mysql.connector
from FormDiarista import FormDiarista
from Diarista import Diarista

conn = mysql.connector.connect(host='localhost', database='cad_cestas', user='root', password='')
if conn.is_connected():
    form = FormDiarista()
    diarista = form.show()

    if diarista != None:

        query = "INSERT INTO diaristas (nome, endereco, telefone, qte_pessoas, ponto_ref, cpf) VALUES ( "
        query += "'" + diarista.nomeD + "' , '" + diarista.enderecoD + "', " + diarista.telefoneD + " , " + diarista.qte_pessoas + " , '" + diarista.ponto_ref + "', " + diarista.cpfD + " ) " 

        cursor = conn.cursor()
        cursor.execute( query )
        conn.commit()
        cursor.close()
        conn.close()
else: 
    print( "Não foi possível conectar ao banco")