

def get_query_from_file(file_path):
    """
        Функция читает .sql файл и возвращает его содержимое
    """
    if ".sql" not in file_path:
        raise Exception(f"Please, check if filepath leads to .sql file. Your current filepath is: {file_path}")
    with open(file_path, "r") as file:
        query = file.read()
        return query
