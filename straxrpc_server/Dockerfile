 FROM python:3
 ENV PYTHONUNBUFFERED 1
 RUN mkdir /code
 ADD . /code/
 WORKDIR /code
 ADD requirements.txt /code/
 RUN pip install -r requirements.txt
 RUN pip install git+https://github.com/AxFoundation/strax.git
 EXPOSE 50051
 
 CMD ["python", "run_server.py"]