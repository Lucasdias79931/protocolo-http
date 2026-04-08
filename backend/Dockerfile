FROM python:3.11



WORKDIR /app

COPY requiriments.txt .

RUN pip install -r requiriments.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]