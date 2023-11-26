# Интерактивная карта Москвы.

Карта Москвы, на которую пользователи могут добавлять интересные объекты и места для развлечений с подробными описаниями и фотографиями. 

## Запуск

Для запуска сайта вам понадобится Python третьей версии.

Скачайте код с GitHub:
```sh
git clone https://github.com/user-name-art/week14_django_yandexmap.git
```

Установите зависимости:

```sh
pip install -r requirements.txt
```

Создайте базу данных SQLite

```sh
python3 manage.py migrate
```

Запустите разработческий сервер

```
python3 manage.py runserver
```

## Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` рядом с `manage.py` и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

Доступны 5 переменных:
- `DEBUG` — дебаг-режим. Поставьте `True`, чтобы увидеть отладочную информацию в случае ошибки.
- `SECRET_KEY` — секретный ключ проекта.
- `DATABASE_ENGINE` — база данных, например: django.db.backends.sqlite3
- `DB_NAME` — название базы данных, например: db.sqlite3
- `ALLOWED_HOSTS` — см [документацию Django](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts)


## Цели проекта

Код написан в учебных целях — для курса по Python и веб-разработке на сайте [Devman](https://dvmn.org).
