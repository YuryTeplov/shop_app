FROM python:3.10.1

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt


COPY . code
WORKDIR /code

RUN python manage.py makemigrations
RUN python manage.py migrate
RUN python manage.py initadmin

EXPOSE 8000

ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]
