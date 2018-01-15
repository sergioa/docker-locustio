FROM python:3

CMD mkdir locustio

WORKDIR locustio

COPY requirements.txt .

COPY scripts/ scripts

RUN pip install -r requirements.txt

ENTRYPOINT ["locust", "-f", "scripts/locustfile.py"]

