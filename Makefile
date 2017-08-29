MANAGE_PY = ./hasker/manage.py

IMAGE_NAME = hasker

.PHONY: stage
stage: prepare-db start-postgres load-fixtures

.PHONY: start-postgres
start-postgres:
	@sudo -u postgres -H postgres \
	-c config_file=${PG_CONFDIR}/postgresql.conf \
	-D ${PG_CONFDIR} &
	@echo "Wait 5s..."
	@sleep 5s

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

.PHONY: docker-build
docker-build:
	docker build -t $(IMAGE_NAME) .

.PHONY: docker-bash
docker-bash: docker-build
	docker run --rm -it $(IMAGE_NAME) /bin/bash