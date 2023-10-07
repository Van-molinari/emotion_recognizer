import mysql.connector

class Database:
    def __init__(self):
        self.dbConnection = mysql.connector.connect(user='root', password='root', host='localhost', port='3307', database='emotion_recognizer')
        self.cursor = self.dbConnection.cursor()

    def insert(self, table:str, values:list):
        if table == "audios": 
            file_id, filename = values
            path_Audio = f"/var/lib/mysql-files/media/{filename}"
            insert_query = (f"INSERT INTO audios (Cod_files, Desc_Files, Audios_files) VALUES ('{file_id}', '{filename}', LOAD_FILE('{path_Audio}'))")

        elif table == "recognition":
            file_id, emotion, transcript, prediction = values
            insert_query = (f'INSERT INTO recognition (File_id, Emotion, Transcript, Percentage) VALUES ("{file_id}", "{emotion}", "{transcript}", "{prediction}")')
        
        print(insert_query)
        self.cursor.execute(insert_query)
        self.dbConnection.commit()

    def select(self, table, file_id=None):
        if table == "audios" and file_id == None: 
            select_query = "SELECT Cod_files, Desc_files FROM audios"
        
        elif table == "audios" and file_id != None:
            select_query = f"SELECT Audios_files FROM audios WHERE Cod_files='{file_id}'"

        elif table == "recognition":
            select_query = f"SELECT * FROM recognition WHERE File_id='{file_id}'"
        self.cursor.execute(select_query)
        query = self.cursor.fetchall()

        return query
        