FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD stable-req.txt /code/
RUN pip install -r stable-req.txt
ADD . /code/