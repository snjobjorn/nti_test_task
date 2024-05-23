from utils.get_query_from_file import get_query_from_file
from utils.execute_update_query import execute_update_query
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--id', type=int, help='fact_detail_id')
    parser.add_argument('--text', type=str, help='Добавляемый текст')
    parser.add_argument('--query_path', type=str, help='Путь до текста запроса SQL')
    args = parser.parse_args()

    query = get_query_from_file(str(args.query_path)).format(text=args.text, fact_detail_id=args.id)
    # Вывести текст SQL запроса можно так:
    print(query)
    execute_update_query(query)
