# python-17 #
"Python Developer" course at otus.ru. Group 2017

### Запуск проекта ###

* Проект запускается в Docker контейнере
* Контейнер сделан на базе centos 7
* Запустите чистый контейнер с centos 7 на хостовой системе
```bash
docker run --rm -it -p 8080:80 centos:latest /bin/bash
```
* Внутри контейнера выполните команды:
```bash
yum -y install make git
git clone https://github.com/LiveStalker/python-17-hw6.git /app
cd /app
make stage
```

Тестовые пользователи (у всех пароль P@$$w0rd): 

* alexey
* alise
* basil
* bob
* gregory
* hasker
* peter

### API ###

* /api/v1/questions/ - работа с вопросами
* /api/v1//tags/ - работа с тэгами
* /api/v1/answers/ - работа с ответами
* /api/v1/trending/ - топ 20
* /api/v1/search/?q=<search text> - поиск
* /api/v1/questions/<id>/answers/ - список ответов конкретного вопроса

Примеры работы с API на фикстурах:

* аутентификация
```bash
# получение токена
curl -X POST -H "Content-Type: application/json" -d '{"username":"hasker","password":"P@$$w0rd"}' http://<host:port>/api/v1/auth/login/

# использование токена
curl -H "Authorization: JWT <your_token>" http://<host:port>/api/v1/questions/
```
* получить index: /api/v1/questions/
* получить trending: /api/v1/trending/
* сделать поисковый запрос: /api/v1/search/?q=friend
* получить вопрос: /api/v1/questions/1/
* получить ответы к вопросу: /api/v1/questions/1/answers/

### Author ###

Alexey Grebenshchikov

slack: Alexey Grebenshchikov (alexey.g)

email: mi.alekiso@gmail.com
