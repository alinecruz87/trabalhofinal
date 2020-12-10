import mysql.connector

conn = mysql.connector.connect(host='localhost', database='cad_cestas', user='root', password='')
if conn.is_connected():
    cursor = conn.cursor()
    cursor.execute( "SELECT * FROM voluntarios")
    result = cursor.fetchall()

    for voluntario in result:
        texto = str(voluntario[0]) + ": " + voluntario[1] 
        print( texto )
        print("------------------------")

    id = input("Digite o id da voluntario que deseja excluir:")

    cursor.execute( "DELETE FROM voluntarios WHERE id = " + str(id) )
    conn.commit()

    cursor.execute( "SELECT * FROM voluntarios")
    result = cursor.fetchall()
    for voluntario in result:
        texto = str(voluntario[0]) + ": " + voluntario[1] 
        print( texto )
        print("------------------------")


    cursor.close()
    conn.close()