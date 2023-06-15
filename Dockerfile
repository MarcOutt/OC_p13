# Stage 1: Builder
FROM python:3.7-alpine as builder
WORKDIR /app
RUN apk update && apk add --no-cache build-base
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .


FROM python:3.7-alpine
WORKDIR /app
COPY --from=builder /app /app
RUN apk update && apk add --no-cache nginx
COPY nginx.conf /etc/nginx/conf.d/default.conf
RUN python manage.py collectstatic --no-input
EXPOSE 8000 80
CMD nginx && python manage.py runserver 0.0.0.0:8000