FROM python:3.11
WORKDIR /usr/src/flask_app
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
COPY . .