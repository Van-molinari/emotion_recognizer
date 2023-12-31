import mysql.connector

class Database:
    def __init__(self):
        self.dbConnection = mysql.connector.connect(user='root', password='root', host='mysql', port='3306', database='emotion_recognizer')
        self.cursor = self.dbConnection.cursor()

    def insert(self, table:str, values:list):
        if table == "audios": 
            file_id, filename = values
            path_Audio = f"/var/lib/mysql-files/{filename}"
            insert_query = (f"INSERT INTO audios (Audio_id, Audio_name, Audio_content) VALUES ('{file_id}', '{filename}', LOAD_FILE('{path_Audio}'))")

        elif table == "recognition":
            file_id, emotion, transcript, prediction = values
            insert_query = (f'INSERT INTO recognition (Audio_id, Emotion, Transcript, Prediction) VALUES ("{file_id}", "{emotion}", "{transcript}", "{prediction}")')
        
        print(insert_query)
        self.cursor.execute(insert_query)
        self.dbConnection.commit()

    def update(self, table:str, values:list):
        if table == "audios": 
            file_id, filename = values
            path_Audio = f"/var/lib/mysql-files/{filename}"
            insert_query = (f"UPDATE audios (Audio_name, Audio_content) VALUES ('{filename}', LOAD_FILE('{path_Audio}')) WHERE Audio_id = '{file_id}'")

        elif table == "recognition":
            file_id, emotion, transcript, prediction = values
            insert_query = (f'UPDATE recognition SET Emotion = "{emotion}", Transcript = "{transcript}", Prediction = "{prediction}" WHERE Audio_id = "{file_id}"')
        
        print(insert_query)
        self.cursor.execute(insert_query)
        self.dbConnection.commit()

    def select(self, table:str, file_id=None):
        if table == "audios" and file_id == None: 
            select_query = "SELECT Audio_id, Audio_name FROM audios"
        
        elif table == "audios" and file_id != None:
            select_query = f"SELECT Audio_content FROM audios WHERE Audio_id='{file_id}'"

        elif table == "recognition":
            select_query = f"SELECT * FROM recognition WHERE Audio_id='{file_id}'"
        self.cursor.execute(select_query)
        query = self.cursor.fetchall()

        return query

    def check_file(self, file):
        path_Audio = f"/var/lib/mysql-files/{file}"
        select_query = f"SELECT Audio_id FROM audios WHERE Audio_content=LOAD_FILE('{path_Audio}')"
        print(select_query)
        self.cursor.execute(select_query)
        query = self.cursor.fetchall()
        print(query)
        if len(query) > 0: return True, query[0][0]
        else: return False
        