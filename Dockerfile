FROM python:3

ENV PYTHONUNBUFFERED 1
RUN mkdir /UserManagement
WORKDIR /UserManagement
COPY . /UserManagement/
RUN pip install -r requirements.txt