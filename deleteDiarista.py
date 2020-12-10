import mysql.connector

conn = mysql.connector.connect(host='localhost', database='cad_cestas', user='root', password='')
if conn.is_connected():
    cursor = conn.cursor()
    cursor.execute( "SELECT * FROM diaristas")
    result = cursor.fetchall()

    for diarista in result:
        texto = str(diarista[0]) + ": " + diarista[1] 
        print( texto )
        print("------------------------")

    id = input("Digite o id da diarista que deseja excluir:")

    cursor.execute( "DELETE FROM diaristas WHERE id = " + str(id) )
    conn.commit()

    cursor.execute( "SELECT * FROM diaristas")
    result = cursor.fetchall()
    for diarista in result:
        texto = str(diarista[0]) + ": " + diarista[1] 
        print( texto )
        print("------------------------")


    cursor.close()
    conn.close()