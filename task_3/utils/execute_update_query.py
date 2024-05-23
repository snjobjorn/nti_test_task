from utils.connect_to_db import connect_to_db
import psycopg2


def execute_update_query(query):
    """
        Функция-генератор кортежей, полученных в результате исполнения SELECT SQL запроса к базе данных
    """
    # Проверка на UPDATE в начале запроса
    first_query_word = query.split()[0]
    if first_query_word.lower() != "update":
        raise Exception(f"This method is only for UPDATE queries. Please, use another one. Your query begins with: {first_query_word}")

    conn = connect_to_db()
    cursor = conn.cursor()
    try:
        cursor.execute(query)
    except psycopg2.Error as e:
        print("Query execution error happened:", e)
    finally:
        conn.close()
