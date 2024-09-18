FROM python:3.12.5

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 9001

CMD ["python", "server.py"]