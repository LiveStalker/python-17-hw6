FROM centos

WORKDIR /app

RUN yum clean all
RUN yum install -y\
    vim\
    less\
    git \
    python

ADD https://bootstrap.pypa.io/get-pip.py /tmp/
RUN python /tmp/get-pip.py
RUN git clone https://github.com/LiveStalker/python-17-hw6.git .
RUN pip install -r requirements.txt