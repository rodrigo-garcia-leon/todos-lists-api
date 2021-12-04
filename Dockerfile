FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src ./src

ENV FLASK_APP="./src/app.py"
CMD [ "flask", "run", "--host=0.0.0.0" ]
