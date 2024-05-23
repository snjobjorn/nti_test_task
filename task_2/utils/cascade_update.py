from utils.connect_to_db import connect_to_db
from query.queries_list import queries_sequence
import psycopg2


def cascade_update(source_id):
    """
        Реализация каскадного изменения путем исполненияпоследовательности UPDATE запросов:
        на вход - source_id удаляемого источника, queries_sequence - разработанная
        последовательность SQL запросов в виде форматируемой строки и места для source_id.
    """

    conn = connect_to_db()
    cursor = conn.cursor()

    try:
        for query in queries_sequence:
            cursor.execute(str(query).format(source_id))
    except psycopg2.Error as e:
        print("Query execution error happened:", e)
    finally:
        print("Success!")
        conn.close()
