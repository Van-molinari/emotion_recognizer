import mysql.connector
import docker
import os

class Database:
    def __init__(self):
        self.dbConnection = mysql.connector.connect(user='root', password='root', host='localhost', port='3307', database='emotion_recognizer')
        self.cursor = self.dbConnection.cursor()

    def insert(self, table:str, values:list):
        if table == "audios": 
            file_id, filename = values
            path_Audio = f"/var/lib/mysql-files/media/{filename}"
            print(path_Audio)
            insert_query = (f"INSERT INTO audios (Cod_files, Desc_Files, Audios_files) VALUES ('{file_id}', '{filename}', LOAD_FILE('{path_Audio}'))")
            print(insert_query)
        elif table == "analytics":
            variables = "Desc_Files, Audios_files"
            emotion, text, prediction = values
        
        self.cursor.execute(insert_query)
        self.dbConnection.commit()