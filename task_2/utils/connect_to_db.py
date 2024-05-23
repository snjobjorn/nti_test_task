import os
import psycopg2
from dotenv import load_dotenv


def connect_to_db():
    """
        Функция возвращает инстанс объекта подключения к базе данных PostgreSQL
    """
    load_dotenv()
    db_name = os.environ['DB_NAME']
    user = os.environ['USER']
    password = os.environ['PASSWORD']
    host = os.environ['HOST']
    port = os.environ['PORT']
    connection = psycopg2.connect(
        database=db_name,
        user=user,
        password=password,
        host=host,
        port=port
    )
    connection.autocommit = True
    return connection
