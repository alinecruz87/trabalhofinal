import mysql.connector
conn = mysql.connector.connect(host='localhost', database='cad_cestas', user='root', password='')
if conn.is_connected():

    cursor = conn.cursor()

    cursor.execute( "SELECT * FROM voluntarios")

    result = cursor.fetchall()

    for voluntario in result:
        texto = str(voluntario[0]) + "- Nome: " + voluntario[1] + " - Endereco: " + str(voluntario[2]) + " - Telefone: " + str(voluntario[3]) + " - CPF: " + str(voluntario[4]) + " - Automovel: " + str(voluntario[5])
        print( texto )
        print("------------------------")

    cursor.close()
    conn.close()