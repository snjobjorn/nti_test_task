import argparse
import os

from utils.fio_preprocessing import fio_preprocessing

if __name__ == '__main__':
    # test_string_f = "Р0гова;ирина;Петр-на;Ж"
    # test_string_m = "Кураш0в;маским;михаилович;М"
    parser = argparse.ArgumentParser()
    parser.add_argument('--name_to_parse', type=str, help='Строка для парсинга, разделенная точкой с запятой.')
    args = parser.parse_args()
    possible_names = fio_preprocessing(args.name_to_parse)
    print(f"\nИтоговое ФИО: {possible_names}")
