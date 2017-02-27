FROM python:2-alpine
RUN apk add --update py-pip

COPY . /usr/src/app
RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt
CMD ["python", "usr/src/app/src/horses.py"]