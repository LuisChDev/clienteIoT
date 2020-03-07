FROM python:3.7.6-alpine3.11

### takes a long time. Be careful
# RUN apt update && apt install -y python3-pip python-dev \
#     mysql-server redis-server

ENV FLASK_RUN_HOST 0.0.0.0

COPY . /project

WORKDIR /project

RUN python3 -m pip install -r requirements.txt

EXPOSE 80

CMD ["flask", "run", "--host=0.0.0.0"]
