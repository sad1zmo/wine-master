# Новое русское вино

Сайт магазина авторского вина "Новое русское вино".

## Запуск

- Скачайте код
- Выполните команду `pip install requirements.txt`
- Для запуска необходимо иметь файл `wine.xlsx` с подобным содержимым:

| Категория  | Название            | Сорт            | Цена | Картинка                 | Акция                |
| ---------- | ------------------- | --------------- | ---- | ------------------------ | -------------------- |
| Белые вина | Белая леди          | Дамский пальчик | 399  | belaya_ledi.png          | Выгодное предложение |
| Напитки    | Коньяк классический |                 | 350  | konyak_klassicheskyi.png | Выгодное предложение |

обязательнымы являются данные в столбце Категория, все остальные данные в таблице не обязательны, но для корректной работы желательны

- Запустите сайт командой:

```python
python3 main.py
```

- Перейдите на сайт по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).

Если вы хотите изменить Exel файл из которого брать информацию, необходимо указать его путь через переменные окружения:

```python
export EXEL_FILEPATH=./wine.xlsx
```

Если вы хотите изменить страницу в фале, необходимо указать ее через переменные окружения:

```python
export EXEL_SHEET_NAME='Лист1'
```
