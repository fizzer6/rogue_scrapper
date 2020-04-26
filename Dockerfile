# our base image
FROM python:3

RUN pip install beautifulsoup4
RUN pip install requests

COPY main.py /app/
WORKDIR /app

RUN chmod +x main.py

ENTRYPOINT ["./main.py"]
