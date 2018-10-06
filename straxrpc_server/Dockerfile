 FROM python:3
 FROM strax:latest
 ENV PYTHONUNBUFFERED 1
 RUN mkdir /code
 ADD . /code/
 WORKDIR /code
 ADD requirements.txt /code/
 RUN pip install -r requirements.txt
 EXPOSE 50051
 
 CMD ["python", "run_server.py"]