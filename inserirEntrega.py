# encoding: utf-8
import mysql.connector
from FormEntrega import FormEntrega
from Entrega import Entrega

conn = mysql.connector.connect(host='localhost', database='cad_cestas', user='root', password='')
if conn.is_connected():
    form = FormEntrega()
    entrega = form.show()

    if entrega != None:

        query = "INSERT INTO entregas (id_v, id_d, qtde_cesta) VALUES ( "
        query +=  entrega.id_v + " , " + entrega.id_d + " , " + entrega.qtde_entregue + " ) " 

        cursor = conn.cursor()
        cursor.execute( query )
        conn.commit()
        cursor.close()
        conn.close()
else: 
    print( "Não foi possível conectar ao banco")