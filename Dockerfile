FROM python:3

ENV PYTHONUNBUFFERED=1

WORKDIR /app

ADD . /app

COPY ./requrements.txt /app/requirements.txt

RUN pip install --upgrade pip

RUN pip install -r requirements.txt


COPY . /app 

EXPOSE 8000

CMD ["python", "manage.py","runserver"]










