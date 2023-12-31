# О проекте
«Фудграм» — сайт, на котором пользователи будут публиковать рецепты, добавлять чужие рецепты в избранное и подписываться на публикации других авторов. Пользователям сайта также будет доступен сервис «Список покупок». Он позволит создавать список продуктов, которые нужно купить для приготовления выбранных блюд.
У веб-приложения уже есть готовый фронтенд — это одностраничное SPA-приложение, написанное на фреймворке React. 


## Стек технологий

Python, Django, PostgreSQL, Django Rest Framework, Djoser, CI/CD, Nginx


## Настройка приложения

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:Aleksandri-A/foodgram-project-react.git
```

Скачайте и установите curl — консольную утилиту, которая умеет скачивать файлы по команде пользователя:
```
sudo apt update
sudo apt install curl
```

Запустите скрипт:
```
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh ./get-docker.sh
```

Дополнительно к Docker установите утилиту Docker Compose:
```
sudo apt-get install docker-compose-plugin 
```

В терминале в папке с docker-compose.yml выполните команду:

```
docker compose up 
```

Перейдите в директорию, где лежит файл docker-compose.yml, и выполните миграции:

docker compose exec backend python manage.py migrate
Выполните команду сборки статики. 

```
docker compose exec backend python manage.py collectstatic
```

## Деплой: публикация проекта в Docker на сервере

Поочерёдно выполните на сервере команды для установки Docker и Docker Compose для Linux.

```
sudo apt update
sudo apt install curl
curl -fSL https://get.docker.com -o get-docker.sh
sudo sh ./get-docker.sh
sudo apt-get install docker-compose-plugin 
```

Создайте на сервере директорию foodgram и файл docker-compose.production.yml и скопируйте в него сожержимое из локального docker-compose.production.yml.

Создайте файл .env и внесите ваши данные:
```
POSTGRES_DB=foodgram
POSTGRES_USER=foodgram_user
POSTGRES_PASSWORD=foodgram_password
DB_PORT=5432
DB_HOST=db
```
Для запуска Docker Compose в режиме демона команду выполните эту команду на сервере в папке foodgram/:
```
sudo docker compose -f docker-compose.production.yml up -d 
```

Выполните миграции, соберите статические файлы бэкенда и скопируйте их в /backend_static/static/:
```
sudo docker compose -f docker-compose.production.yml exec backend python manage.py migrate
sudo docker compose -f docker-compose.production.yml exec backend python manage.py collectstatic
sudo docker compose -f docker-compose.production.yml exec backend cp -r /app/collected_static/admin/. /app/static/admin/
sudo docker compose -f docker-compose.production.yml exec backend cp -r /app/collected_static/rest_framework/. /app/static/rest_framework/
```

Если Nginx ещё не установлен на удалённый сервер, установите его:
```
sudo apt install nginx -y
```

Запустите Nginx командой:
```
sudo systemctl start nginx
```

На сервере в редакторе nano откройте конфиг Nginx и обновите настройки: 
```
nano /etc/nginx/sites-enabled/default
```

```
server {
    listen 80;
    server_name ваш_домен;

    location / {
        proxy_pass http://127.0.0.1:8000;
    }
}
```

Чтобы убедиться, что в конфиге нет ошибок — выполните команду проверки конфигурации:
```
sudo nginx -t 
```

Перезагрузите конфиг Nginx:
```
sudo service nginx reload 
```

# Тестовые данные:
https://foodgram.ddnsking.com
admin@admin.ru пароль admin
