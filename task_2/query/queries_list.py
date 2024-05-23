queries_sequence = list([
    # Удаление источника
    "UPDATE source SET is_deleted = 1 WHERE source_ID = {0}",
    # Каскадное удаление всех данных из связанных таблиц
    "UPDATE fact SET is_deleted = 1 WHERE source_ID = {0}",
    "UPDATE fact_detail SET is_deleted = 1 WHERE fact_ID IN (SELECT fact_ID FROM fact WHERE source_ID = {0})",
    "UPDATE fact_creator SET is_deleted = 1 WHERE fact_ID IN (SELECT fact_ID FROM fact WHERE source_ID = {0})"
])
