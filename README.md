# python-17
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


### Author

Alexey Grebenshchikov

slack: Alexey Grebenshchikov (alexey.g)

email: mi.alekiso@gmail.com
