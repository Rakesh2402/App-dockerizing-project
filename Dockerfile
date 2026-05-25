FROM python 3.12-slim

WORKDIR /app

COPY requirements.txt 

RUn pip install -r requirements.txt

COPY . .

RUN useradd -m appuser && chown -R appuser /app

USER appuser

EXPOSE 5000

CMD ["python", "app.py"]

