FROM python:3.7-slim-stretch

MAINTAINER Shubham Jadhav "spj.8596@gmail.com"
COPY ./FlaskApi /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["main.py"]
