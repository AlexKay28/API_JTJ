FROM python:3

WORKDIR /usr/scr/app

RUN apt-get update

COPY requirements.txt .
RUN pip install -r requirements.txt


COPY app/ .

CMD ["python", "app.py"]
