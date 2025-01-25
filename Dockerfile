FROM python:3

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir \
    psycopg2 \
    starlette \
    uvicorn

#EXPOSE 8501:8501
 
WORKDIR /usr/app/src

COPY . .


ENTRYPOINT [ "uvicorn" ]
CMD ["--factory", "main:create_app", "--host=0.0.0.0", "--port=8501"]
#CMD ["python3", "./main.py"]
#CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port=8501"]