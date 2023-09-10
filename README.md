Парсер для новостей с сайта https://78.ru/news

## Описание

### Web приложения для сбора новостей и работы с ними в админ панели Django.

При запуске парсер первый раз собирает последние 13 новостей с сайта https://78.ru/news. Далее каждые 15 минут собирает последние новости.   В проекте используется брокер задач Celery для праралельной работы парсера. 
Новости сохраняются в БД SQLite. 
С помощью админ панели возможно просматривать сохраненые данные.
Есть возможность выгрузить выделенные новости в JSON файл.
В БД сохраняются следующие данные:

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
- Клонируйте репозиторий командой:
```
git clone git@github.com:oitczvovich/parser_78.git
``` 
- Перейдите в каталог командой:
```
cd project
```
- Создаем файл .env с переменными окружения пример в файле `.env_example`


### Использование чистой БД
- Необходимо удалить текущую БД.

```
rm posts.sqlite3
```
- Выполните команду для запуска контейнера:

```
sudo docker-compose up -d --build
``` 

- Выполнить миграции и подключить статику
```
sudo docker-compose exec parser_78_web_1 python manage.py makemigrations
sudo docker-compose exec parser_78_web_1 python manage.py migrate
sudo docker-compose exec parser_78_web_1 python manage.py collectstatic --noinput
``` 
- Создадим суперпользователя:
```
sudo docker-compose exec parser_78_web_1 python manage.py createsuperuser
``` 
### Использование текущей БД

- Выполните команду для запуска контейнера:

```
sudo docker-compose up -d --build
``` 

### Проект
Работает по адресу:

http://84.252.137.243:1337/admin/<br>
username: SuperUser<br>
password: GERvre4tvaSAAG453gr<br>


## Авторы проекта
### Скалацкий Владимир
e-mail: skalakcii@yandex.ru<br>
https://github.com/oitczvovi<br>
Telegramm: @OitcZvovich