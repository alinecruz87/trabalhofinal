import mysql.connector
conn = mysql.connector.connect(host='localhost', database='cad_cestas', user='root', password='')
if conn.is_connected():

    cursor = conn.cursor()

    cursor.execute( "SELECT * FROM diaristas")

    result = cursor.fetchall()

    for diarista in result:
        texto = str(diarista[0]) + "- Nome: " + diarista[1] + " - Endereco: " + str(diarista[2]) + " - Telefone: " + str(diarista[3]) + " - CPF: " + str(diarista[4]) + " - Qte Pessoas: " + str(diarista[5]) + " - Ponto de Referencia: " + str(diarista[6])  
        print( texto )
        print("------------------------")

    cursor.close()
    conn.close()