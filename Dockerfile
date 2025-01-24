FROM python:3

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir \
    psycopg2 \
    starlette \
    uvicorn

#EXPOSE 8501:8501
 
WORKDIR /usr/app/src

COPY . .


CMD ["python3", "./main.py"]
#CMD ["uvicorn", "main:app", "--reload", "--host=0.0.0.0", "--port=8501"]