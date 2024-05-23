from utils.get_query_from_file import get_query_from_file
from utils.execute_select_query import execute_select_query
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--query_path', type=str, help='Путь до текста запроса SQL')
    args = parser.parse_args()

    query = get_query_from_file(args.query_path)
    # Вывести текст SQL запроса можно так:
    print(query)
    # Получить список из кортежей результата исполнения SQL запроса можно так
    result = list(execute_select_query(query))
    print(result)

