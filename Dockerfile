FROM alpine:3.7
MAINTAINER Abhishek Shukla <shuklaabhishek02@gmail.com>
RUN addgroup appgroup && adduser -G appgroup -S -s /sbin/nologin appuser

RUN apk add --no-cache gcc libc-dev linux-headers python3  python3-dev
RUN easy_install-3.6 pip
RUN pip3 install --upgrade pip setuptools
RUN easy_install-3.6 pip

WORKDIR /opt/quovantis/katana

COPY ./katana /opt/quovantis/katana

RUN pip3 install -r requirements.txt

EXPOSE 5000:5000

RUN chown -R appuser:appgroup /opt/quovantis/katana

USER appuser
#ENTRYPOINT [ "uwsgi", "wsgi.ini" ]


## docker build -t k8-sample-flask-celery:latest .
## docker run --name=flask --rm -it k8-sample-flask-celery:latest /bin/sh -q


##Fetch image Id from $docker images --all
## docker tag 62021225014d shuklaabhishek/k8-sample-flask-celery:latest 
## docker push shuklaabhishek/k8-sample-flask-celery