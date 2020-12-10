# encoding: utf-8
import mysql.connector
from FormVoluntario import FormVoluntario
from Voluntario import Voluntario

conn = mysql.connector.connect(host='localhost', database='cad_cestas', user='root', password='')
if conn.is_connected():
    form = FormVoluntario()
    voluntario = form.show()

    if voluntario != None:

        query = "INSERT INTO voluntarios (nome_v, endereco_v, telefone_v, automovel, cpf_v) VALUES ( "
        query += "'" + voluntario.nomeV + "' , '" + voluntario.enderecoV + "', " + voluntario.telefoneV + " , " + voluntario.cpfV + " , " + voluntario.automovel + ") " 

        cursor = conn.cursor()
        cursor.execute( query )
        conn.commit()
        cursor.close()
        conn.close()
else: 
    print( "Não foi possível conectar ao banco")