FROM python:3.10-alpine3.19

ENV LAT "50.930581"
ENV LNG "5.780691"

WORKDIR /app
COPY . .
RUN pip install -r requirements.txt

ENTRYPOINT ["python", "/app/main.py"]
