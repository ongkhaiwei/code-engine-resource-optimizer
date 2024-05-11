FROM python:3.11.9-alpine3.19

RUN pip install --no-cache-dir ibm_code_engine_sdk>=3.1.0
WORKDIR /usr/app/src
COPY main.py .
COPY .env .

CMD ["python", "main.py"]