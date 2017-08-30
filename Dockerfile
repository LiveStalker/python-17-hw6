FROM centos

WORKDIR /app

COPY etc/nginx.repo /etc/yum.repos.d/nginx.repo

RUN yum -y update; yum clean all
RUN yum -y install epel-release; yum clean all
RUN yum install -y\
    vim\
    sudo \
    less\
    git \
    python \
    python-devel \
    gcc \
    nginx \
    postgresql-server \
    ; yum clean all

ADD https://bootstrap.pypa.io/get-pip.py /tmp/
RUN python /tmp/get-pip.py
COPY requirements.txt /app
RUN pip install -r requirements.txt
RUN pip install uwsgi
RUN adduser -r -s /bin/false -d /app hasker
RUN usermod -a -G hasker nginx; \
    rm /etc/nginx/conf.d/default.conf

COPY etc/postgresql-setup /usr/bin/postgresql-setup
RUN chmod +x /usr/bin/postgresql-setup
RUN postgresql-setup initdb
COPY etc/postgresql.conf /var/lib/pgsql/data/postgresql.conf
COPY etc/pg_hba.conf /var/lib/pgsql/data/pg_hba.conf
ENV PG_CONFDIR="/var/lib/pgsql/data"
# Do not do it in production
# Keep secrets in secret place :)
ENV HASKER_DB_HOST="localhost"
ENV HASKER_DB_NAME="hasker"
ENV HASKER_DB_USER="hasker"
ENV HASKER_DB_PASSWORD="hasker"
ENV HASKER_SECRET="very secret string"
ENV HASKER_RUN_ENV="stage"

COPY Makefile /app
COPY hasker /app/hasker
COPY fixtures /app/fixtures
COPY sql /app/sql
COPY etc/hasker.ini /app
COPY etc/nginx-hasker.conf /etc/nginx/conf.d
