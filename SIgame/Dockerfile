FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY . .
RUN pip install --no-cache-dir -r requirements.txt


#FROM python:3.10
#
#ENV PYTHONDONTWRITEBYTECODE=1
#ENV PYTHONUNBUFFERED=1
#
#RUN mkdir -p /usr/src/app/
#WORKDIR /usr/src/app/
#
#COPY . /usr/src/app/
#RUN pip install --no-cache-dir -r requirements.txt
#
#EXPOSE 8000
#
#ENTRYPOINT ["python", "manage.py", "runserver"]