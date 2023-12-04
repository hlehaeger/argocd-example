FROM python:3.8-slim-buster
WORKDIR /app

COPY Pipfile Pipfile.lock ./

RUN pip install pipenv && pipenv install --system --deploy

COPY . .

CMD ["flask", "run", "--host=0.0.0.0"]