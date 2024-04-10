# Новое русское вино

Сайт магазина авторского вина "Новое русское вино".

## Запуск

- Скачайте код
- Выполните команду `pip install requirements.txt`
- Для запуска необходимо иметь файл `wine.xlsx` с содержимым:
```
| Категория	|    Название	 |       Сорт	       |     Цена  |	Картинка	   |        Акция    |
|-------------|--------------|---------------------|-----------|-------------------|-----------------|
|Белые вина	  |  Белая леди	 |       Дамский пальчик |	    399	   | belaya_ledi.png	   |    Выгодное предложение|
Напитки	        Коньяк классический		                350	    konyak_klassicheskyi.png	
Белые вина	    Ркацители	        Ркацители	        499	    rkaciteli.png	
Красные вина	Черный лекарь	    Качич	            399	    chernyi_lekar.png	
Красные вина	Хванчкара	        Александраули	    550	    hvanchkara.png	
Белые вина	    Кокур	            Кокур	            450	    kokur.png	
Красные вина	Киндзмараули	    Саперави	        550	    kindzmarauli.png	
Напитки	Чача		                                    299	    chacha.png	           Выгодное предложение
Напитки	Коньяк кизиловый		                        350	    konyak_kizilovyi.png	
```
обязательнымы являются данные в столбце Категория, все остальные данные в таблице не обязательны, но для корректной работы желательны
- Запустите сайт командой `python3 main.py`
- Перейдите на сайт по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).