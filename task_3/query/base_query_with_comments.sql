-- Обращаю внимание, что запрос примерный и может быть оптимизирован при уточнении структуры хранилища и тестировании

-- UPDATE запрос с использованием оператора конкатенации строк SQL и выборки по конкретному fact_detail_ID
UPDATE fact_detail SET add_info = add_info || '{text}' WHERE fact_detail_ID = {fact_detail_id}