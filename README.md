Парсер для новостей с сайта https://78.ru/news

## Описание

### Web приложения для сбора новостей и работы с ними в админ панели Django.

Призапуске парсер собирает последние 13 новостей. Далее каждые 15 минут собирает новости со страницы https://78.ru/news
Новости сохраняются в БД SQLite. Есть возможность выгрузить выделенные новости в JSON файл.
В БД сохраняются следующие данные.
<ul>
post__url - прямая ссылка на новость<br>
post__title - заголовок новости<br>
date__create  - дата публикации новости в формате unix timestamp<br>
post__text - полный текст новости, включая разметку и изображения.<br>
post__id - уникальный идентификатор новости, md5 hash от прямой ссылки на новость.<br>
</ul>

## Технологии в проекте

🔹 Python
🔹 Django REST Framework
🔹 Celery
🔹 SQLite
🔹 Docker


## Подготовка и запуск проекта

- Выполните вход на свой удаленный сервер:
```
ssh username@ip
```
- Установите docker и docker-compose на сервер:
```
sudo apt install docker.io 
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

```