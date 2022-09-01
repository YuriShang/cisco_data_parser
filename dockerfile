FROM python:3.9-slim

WORKDIR .

COPY requirements.txt .

RUN pip install -r /requirements.txt

COPY main.py .
COPY settings.py .
COPY ./config/config.yaml ./config/config.yaml

ENTRYPOINT ["python", "./main.py"]
