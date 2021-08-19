FROM alpine:3.14.1
COPY . /app
RUN apk add --no-cache --virtual .build-deps g++ python3-dev libffi-dev openssl-dev && \
    apk add --no-cache --update python3 && \
    apk add --no-cache py3-pip && \
    apk add --no-cache unzip && \
    ln -sf python3 /usr/bin/python && \
    ln -sf pip3 /usr/bin/python && \
    pip3 install --upgrade pip setuptools && \
    apk add --no-cache linux-headers
    
WORKDIR /app
RUN unzip area53.zip && \
    unzip boto.zip && \
    unzip requests.zip
USER root
RUN cd /app/area53 && python3 setup.py install && \
    cd /app/boto && python3 setup.py install && \
    cd /app/requests && python3 setup.py install

ENTRYPOINT [ "python3", "/app/script/route53.py" ]
