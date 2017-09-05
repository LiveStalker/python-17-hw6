MANAGE_PY = ./hasker/manage.py

IMAGE_NAME = hasker

.PHONY: stage
stage: prepare-db start-postgres start-nginx start-hasker

.PHONY: start-postgres
start-postgres:
	@echo "Starting postgres"
	@sudo -u postgres -H postgres \
	-c config_file=${PG_CONFDIR}/postgresql.conf \
	-D ${PG_CONFDIR} &
	@echo "Wait 5s..."
	@sleep 5s
.PHONY: start-nginx
start-nginx:
	@echo "Starting nginx"
	@nginx

.PHONY: start-hasker
start-hasker: load-fixtures collect-static
	@echo "Starting uWSGI application"
	@uwsgi --ini /app/hasker.ini

.PHONY: prepare-db
prepare-db:
	@echo "Create hasker database"
	@sudo -u postgres -H postgres --single \
    -c config_file=${PG_CONFDIR}/postgresql.conf -D ${PG_CONFDIR} \
    < sql/prepare_database.sql > /dev/null

.PHONY: load-fixtures
load-fixtures:
	@echo "Migrate..."
	@cd hasker; python manage.py migrate
	@echo "Load fixtures..."
	@cd hasker; python manage.py loaddata ../fixtures/users.yaml > /dev/null 2>&1
	@cd hasker; python manage.py loaddata ../fixtures/questions.yaml > /dev/null 2>&1

.PHONY: collect-static
collect-static:
	@mkdir -p /var/www/static
	@cd hasker; python manage.py collectstatic --noinput

.PHONY: docker-build
docker-build:
	docker build -t $(IMAGE_NAME) .

.PHONY: docker-bash
docker-bash: docker-build
	docker run --rm -it -p 8080:80 $(IMAGE_NAME) /bin/bash

.PHONY: in-env
in-env: in-install-pkg

.PHONY: in-install-pkg
in-install-pkg:
	yum -y install epel-release
	yum install -y\
        vim\
        sudo \
        less\
        git \
        python \
        python-devel \
        gcc \
        nginx \
        postgresql-server
    wget -O /tmp/get-pip.py https://bootstrap.pypa.io/get-pip.py
    python /tmp/get-pip.py
    pip install -r requirements.txt
    pip install uwsgi
