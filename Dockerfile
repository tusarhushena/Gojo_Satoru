FROM python:3.11.9

RUN  python3 -m pip -U install virtualenv

COPY . .

RUN python3 -m pip install -r requirements.txt

CMD python3 -m Powers
