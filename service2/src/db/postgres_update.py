import psycopg2

class postgresDataHandle():
   
    def __init__(self) -> None:
        self.conn = psycopg2.connect(
            database="mydb", user='root', password='P4g0UMyIl6J5y7rSnvc8ZsYp', host='everest.liara.cloud', port= '30689'
        )
        self.conn.autocommit = True

        cursor = self.conn.cursor()


    def update_songID(self, song_id , id):
        self.cursor.execute(f'''UPDATE SONG_INFO SET SONGID = {song_id}
                             WHERE ID = {id}
                            ''')    

    def update_status(self,id):
        self.cursor.execute(f'''UPDATE SONG_INFO SET STATUS = 'ready'
                             WHERE ID = {id}
                            ''')    
        
    def fail(self,id):
        self.cursor.execute(f'''UPDATE SONG_INFO SET STATUS = 'failure'
                             WHERE ID = {id}
                            ''')    