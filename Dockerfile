# syntax=docker/dockerfile:1
FROM python:3.7-alpine
WORKDIR /OC_p13
RUN pip install --upgrade pip
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
