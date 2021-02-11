FROM python:3.8.7-slim-buster

WORKDIR /app

ADD ./app /app

COPY requeriments.txt /etc
COPY start_api.sh /app

RUN pip install --upgrade pip && pip install -r /etc/requeriments.txt

EXPOSE 5000

ENTRYPOINT [ "python" ]


CMD ["application.py"]
