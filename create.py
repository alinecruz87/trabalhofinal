# encoding: utf-8
import mysql.connector
conn = mysql.connector.connect(host='localhost', database='cad_cestas', user='root', password='')
if conn.is_connected():
    info = conn.get_server_info()
    print( "Conectado ap MySQL " , info )
    print( "-------------" )
    print( "Tabelas existentes" )
    cursor = conn.cursor()
    cursor.execute( "SHOW TABLES" )
    for linha in cursor:
        print( linha )
    print( "-------------" )
    query = "CREATE TABLE IF NOT EXISTS diaristas ( "
    query += " id INT NOT NULL PRIMARY KEY AUTO_INCREMENT , "
    query += " nome VARCHAR(100) NOT NULL , "
    query += " endereco VARCHAR(200) NOT NULL , "
    query += " telefone INT(11)  , "
    query += " qte_pessoas INT(2)  , "
    query += " ponto_ref varchar(150)  , "
    query += " cpf INT(11) ) "
    cursor.execute( query )

    query = "CREATE TABLE IF NOT EXISTS voluntarios ( "
    query += " id_v INT NOT NULL PRIMARY KEY AUTO_INCREMENT , "
    query += " nome_v VARCHAR(100) NOT NULL , "
    query += " endereco_v VARCHAR(200) NOT NULL , "
    query += " telefone_v INT(11)  , "
    query += " automovel BOOLEAN  , "
    query += " cpf_v INT(11) ) "   
    cursor.execute( query )

    query = "CREATE TABLE IF NOT EXISTS entregas ( "
    query += " id_e INT NOT NULL PRIMARY KEY AUTO_INCREMENT , "
    query += " id_v INT NOT NULL , "
    query += " id_d INT NOT NULL , "
    query += " qtde_cesta INT(2) NOT NULL , "
    query += " FOREIGN KEY (id_v) REFERENCES voluntarios(id_v), "
    query += " FOREIGN KEY (id_d) REFERENCES diaristas(id) )" 
    cursor.execute( query )


    print( "Tabelas existentes: " )
    cursor.execute( "SHOW TABLES" )
    for linha in cursor:
        print( linha )
    cursor.close()
    conn.close()
else:
    print( "Não foi possível conectar ao banco")


   