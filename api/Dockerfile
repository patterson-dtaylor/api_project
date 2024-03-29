FROM python:3

WORKDIR /home/flask-api
COPY ./api .

RUN pip install -r requirements.txt

EXPOSE 8000
ENTRYPOINT [ "python" ]
CMD [ "main.py" ]