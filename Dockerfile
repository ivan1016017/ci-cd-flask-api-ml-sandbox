FROM python:3

RUN mkdir /backend

WORKDIR /backend 

ADD requirements.txt /backend/

RUN pip install -r requirements.txt 

COPY * /backend/



CMD ["python3", "app.py"]