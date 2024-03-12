import psycopg2

class postgresDataHandle():
   
    def __init__(self) -> None:
        self.conn = psycopg2.connect(
            database="mydb", user='root', password='P4g0UMyIl6J5y7rSnvc8ZsYp', host='everest.liara.cloud', port= '30689'
        )
        self.conn.autocommit = True

        cursor = self.conn.cursor()
        # cursor.execute('''DROP DATABASE IF EXISTS mydb''')
        # cursor.execute('''CREATE DATABASE mydb''')
        
        cursor.execute('''CREATE TABLE SONG_INFO(
                        ID INT NOT NULL,
                        EMAIL CHAR(50),
                        STATUS CHAR(10),
                        SONGID CHAR(30)
                    )''')
        cursor.execute('''INSERT INTO SONG_INFO(ID ,EMAIl ,STATUS ,SONGID) 
                       VALUES(2 , 'email','pending',null)
                       ''')


    def __del__(self):
        #Closing the connection
        self.conn.close()

    def insert_data(self,id, email):
        self.cursor.execute(f'''INSERT INTO SONG_INFO(ID ,EMAIl ,STATUS ,SONGID) 
                            VALUES({id} , {email} , 'pending' , null)
                            ''')  

    def fail(self,id):
        self.cursor.execute(f'''UPDATE SONG_INFO SET STATUS = 'failure'
                             WHERE ID = {id}
                            ''')
        
if __name__ == "__main__":
    postgres_obj = postgresDataHandle()
