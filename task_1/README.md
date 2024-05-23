# Задание 1

**Текст задания**
<details>
  <summary>Текст задания находится в этом скрытом блоке</summary>
  
  1. Опираясь на приведенную ERD и таблицы со списком атрибутов (для удобства копирования), составить базовый запрос, демонстрирующий для каждого user все его актуальные факты деятельности (fact), детали деятельности (fact_detail) и источники данных, от которых получены эти факты деятельности (source), со статистикой по количеству фактов деятельности и деталей деятельности для каждого user. Для каждой детали деятельности (fact_detail) вывести словарные значения ее типа и типа результата. Данные отсортировать по дате записи в базу (ts) в рамках каждого user.
  Таблицы:
  source (200 записей)
  source_ID (PK)
  source_external_ID : varchar 
  source_title : varchar 
  source_description : varchar 
  source_add_info : varchar 
  is_deleted : int(1) Boolean признак того, что запись считается недействительной (soft delete)
  ts : datetime
  fact (2500 записей)
  fact_ID (PK)
  user_ID (FK)
  source_ID (FK)
  dict_fact_type_ID (FK) 
  fact_external_ID : varchar 
  fact_start_date : datetime 
  fact_end_date : datetime 
  fact_title : varchar 
  fact_description : varchar 
  fact_add_info : varchar 
  fact_string : varchar 
  fact_tag : varchar
  is_teambased : int(1) 
  is_deleted : int(1) Boolean признак того, что запись считается недействительной (soft delete)
  ts : datetime
  fact_detail (30000 записей)
  fact_detail_ID 
  fact_ID 
  dict_detail_type_ID
  dict_result_value_type_ID
  result_scale_info_ID : int (nullable)
  key : varchar 
  value : varchar 
  add_info : varchar
  is_deleted : int(1) Boolean признак того, что запись считается недействительной (soft delete)
  ts : datetime
</details>

В файле "task_1/query/base_query.sql" находится SQL запрос к базе данных согласно заданию, описанному в корневом README.md.

В файле "task_1/query/base_query.sql" находится тот же SQL запрос с комментариями:

```sql
-- Обращаю внимание, что запрос примерный и может быть оптимизирован при уточнении структуры хранилища и тестировании

SELECT
-- Выводим ID пользователей
    fact.user_ID,
-- Выводим название факта деятельности
    fact.fact_title,
-- Выводим название источника
    source.source_title,
-- Выводим поля с деталями фактов
    fact_detail.key AS detail_key,
    fact_detail.value AS detail_value,
-- Считаем и выводим количество фактов деятельности
    COUNT(fact.fact_ID) AS fact_count,
-- Считаем и выводим количество уникальных деталей фактов, так как, согласно схеме ERD,
-- связь fact и fact_detail - one to many
    COUNT(DISTINCT fact_detail.fact_detail_ID) AS detail_count
FROM
-- Объединение таблиц
    fact
    LEFT JOIN source ON source.source_id = fact.source_ID
    LEFT JOIN fact_detail ON fact_detail.fact_id = fact.fact_ID
WHERE
-- Оставляем именно актуальные факты
    fact.is_deleted = 0
GROUP BY
-- Группируем по user_ID для получения статистики по пользователям
    fact.user_ID
ORDER BY
-- Сортируем по timestamp
    fact.ts DESC
```

Также в данном блоке реализовано подключение к базе при помощи библиотек языка Python:
* Запросы лежат в папке query
* Остальные методы расположены в папке utils: в каждом из соответствующих файлов есть комментарий и описана логика его работы
* При запуске main.py из командной строки реализован парсинг аргументов, где `--query_path` есть путь до файла .sql с SELECT запросом
* Запуск скрипта может быть проведен следующим образом:
```bash
  python task_1\main.py --query_path task_1\query\base_query.sql
```
