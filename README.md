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
yum install make git
https://github.com/LiveStalker/python-17-hw6.git
cd python-17-hw6 
make stage
```

### Author

Alexey Grebenshchikov

slack: Alexey Grebenshchikov (alexey.g)

email: mi.alekiso@gmail.com
