Датасет с ФИО (kaggle - Russian (Cyrillic) full names and gender): https://www.kaggle.com/datasets/rai220/russian-cyrillic-names-and-sex
![img.png](img.png)

Регулярное выражение, соответствующее всем перечисленным правилам, может выглядеть так:

[а-яА-ЯёЁ'-.,IV()\s]

Это регулярное выражение можно разбить на части:

[а-яА-Я] — соответствует всем строчным и прописным буквам русского алфавита.
ёЁ — соответствует букве «ё».
' — соответствует апострофу.
- — соответствует дефису.
. — соответствует точке.
, — соответствует запятой.
IV — соответствует буквам I и V латинского алфавита.
\s — соответствует пробелу.
() — соответствуют открывающей и закрывающей скобкам.

python task_5\main.py --name_to_parse 'Р0гова;ирина;Петр-на;Ж'