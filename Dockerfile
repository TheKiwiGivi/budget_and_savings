FROM python:3

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir psycopg2

 
WORKDIR /usr/app/src

COPY . .


CMD ["python3", "./main.py"]