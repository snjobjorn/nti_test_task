# Задание 1

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
