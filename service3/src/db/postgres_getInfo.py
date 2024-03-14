import psycopg2

class postgresDataHandle():
   
    def __init__(self) -> None:
        self.conn = psycopg2.connect(
            database="mydb", user='root', password='P4g0UMyIl6J5y7rSnvc8ZsYp', host='everest.liara.cloud', port= '30689'
        )
        self.conn.autocommit = True

        self.cursor = self.conn.cursor()

    def get_songID(self):
        self.cursor.execute('''SELECT SONGID from SONG_INFO WHERE STATUS = 'ready' ''')


    def update_status(self,id):
        self.cursor.execute(f'''UPDATE SONG_INFO SET STATUS = 'done'
                             WHERE ID = {id}
                            ''')       