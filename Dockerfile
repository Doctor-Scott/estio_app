FROM python:3.8

RUN apt update

RUN apt install python3 python3-pip python3-venv -y

RUN mkdir /code

COPY ./code /code
WORKDIR /code

RUN pip3 install flask

ENTRYPOINT ["python3", "-m", "flask", "run", "--host=0.0.0.0"]