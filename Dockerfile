FROM python:3.11.9

COPY . .

RUN python3 -m pip install -r requirements.txt

CMD python3 -m Powers
