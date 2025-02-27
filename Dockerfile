FROM python:3.13
WORKDIR /app
COPY ./requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY . .
# to run locally
# CMD ["flask", "run", "--host", "0.0.0.0"]
# to deploy
CMD ["gunicorn", "--bind", "0.0.0.0:80", "app:create_app()"]