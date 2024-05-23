import os
from utils.filter_content_by_gender import filter_content_by_gender
from utils.name_detection import name_detection


def fio_preprocessing(fio):
    """
        Функция возвращает потенциальный словарь с определенными корректными именами по входящей строке.
    """
    # Разбиение ФИО на подстроки
    fio_split = fio.lower().split(";")

    output = {
        "surname": None,
        "name": None,
        "middlename": None,
        "gender": fio_split[-1].lower() if fio_split[-1].lower() == "м" or fio_split[-1].lower() == "ж" else None
    }

    # Получение данных о фамилиях
    surname_data = filter_content_by_gender(os.path.normpath("task_5/data/surname_data.jsonl"), output["gender"])
    # Определение потенциальной фамилии
    detected_surname = name_detection(fio_split[0], surname_data)
    # Запись в Output
    output["surname"] = detected_surname["name"]
    print(detected_surname)
    # Получение данных об имени
    name_data = filter_content_by_gender(os.path.normpath("task_5/data/name_data.jsonl"), output["gender"])
    # Определение потенциального имени
    detected_name = name_detection(fio_split[1], name_data)
    output["name"] = detected_name["name"]
    # Запись в Output
    print(detected_name)
    # Получение данных об отчестве
    middlename_data = filter_content_by_gender(os.path.normpath("task_5/data/middlename_data.jsonl"), output["gender"])
    # Определение потенциального отчества
    detected_middlename = name_detection(fio_split[2], middlename_data)
    output["middlename"] = detected_middlename["name"]
    # Запись в Output
    print(detected_middlename)
    return output
