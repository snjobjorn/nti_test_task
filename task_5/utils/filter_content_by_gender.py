import json


def filter_content_by_gender(file_path, gender):
    result_list = list()
    with open(file_path, 'r', encoding='utf8') as file:
        for line in file:
            line = line.strip()
            if line:
                item = json.loads(line)
                if item["gender"].lower() == gender:
                    result_list.append(item)
        return result_list
