 FROM python:3
 ENV PYTHONUNBUFFERED 1
 RUN mkdir /code
 ADD . /code/
 WORKDIR /code/strax
 RUN python setup.py install
 WORKDIR /code
 ADD requirements.txt /code/
 RUN pip install -r requirements.txt
  
 EXPOSE 50051
 CMD ["python", "run_server.py"]