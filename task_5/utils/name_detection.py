import pandas as pd


def name_detection(string, name_data):
    """
        Функция определяет потенциальные ФИО и возвращает имя, степень соответствия, релевантность и коэффициент.
        Работает по принципу поисковой системы, где степень соответствия имеет больший приоритет, чем релевантность.
        На данном этапе константа это магическое число, вычисленная имперически, такое часто бывает :)
    """
    string_list = list(string)
    records = list()
    for item in name_data:
        counter = 0
        list_name = list(item["name"].lower())
        if len(list_name) >= len(string_list):
            for i in range(len(string_list)):
                if string_list[i] in list_name:
                    counter += 1
                if string_list[i] == list_name[i]:
                    counter += 1
            corr_level = counter / (len(item["name"]) * 2)
            x = 1 if int(item["relevance"]) > 10 else 0.5
            coef = (corr_level * 500000 + int(item["relevance"])) * x
            records.append({
                "name": item["name"],
                "correspondence_level": corr_level,
                "relevance": item["relevance"],
                "coef": coef
            })
    df_records = pd.DataFrame.from_records(records)
    df_records = df_records.sort_values(['coef'], ascending=[False])
    return dict(df_records.iloc[0])
