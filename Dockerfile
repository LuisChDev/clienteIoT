FROM python:3.7.6-alpine3.11

RUN apk add gcc
RUN apk add linux-headers
RUN apk add libc-dev
RUN apk add libffi-dev
RUN apk add openssl-dev

ENV FLASK_RUN_HOST 0.0.0.0

COPY . /project

WORKDIR /project

RUN python3 -m pip install -r requirements.txt

EXPOSE 80

CMD ["flask", "run", "--host=0.0.0.0"]
