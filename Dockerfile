FROM python:3.6.4

CMD mkdir locustio

WORKDIR locustio

COPY requirements.txt .

RUN pip install -r requirements.txt

CMD locust -f ./scripts/locustfile.py

