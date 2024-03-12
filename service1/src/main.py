# from prject1.service1.src.api import rabbitMQ
from api import rabbitMQ
from api import s3
from db import postgres_connect

class service1handler():
    
    def __init__(self) -> None:
        self.id = 1
        self.postgres_obj = postgres_connect.postgresDataHandle()
        pass
    
    # /Users/sara/Desktop/test_song.mp3
    def get_info(self):
        email = input("write your email address:\n")
        file_name= input("write your file name:\n")
        file_path= input("write your file path:\n")

        return email,file_name,file_path

    def send_info(self,email,file_name,file_path):
        rabbitMQ.send(self.id)
        s3.upload_file(file_name,file_path)
        self.postgres_obj.insert_data(self.id,email)
        self.id = self.id + 1

    
if __name__ == "__main__":
    obj = service1handler()
    email,file_name,file_path = obj.get_info()
    obj.send_info(email,file_name,file_path)