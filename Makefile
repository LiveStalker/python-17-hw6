MANAGE_PY = ./hasker/manage.py

IMAGE_NAME = hasker

fixtures:
	python $(MANAGE_PY)

.PHONY: docker-build
docker-build:
	docker build -t $(IMAGE_NAME) .

.PHONY: docker-bash
docker-bash: docker-build
	docker run --rm -it $(IMAGE_NAME) /bin/bash