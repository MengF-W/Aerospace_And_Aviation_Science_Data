FROM python:3.12-slim
WORKDIR /applications
COPY aerospace_and_aviation_science_data/ /applications/aerospace_and_aviation_science_data/
COPY nasaApp/ /applications/nasaApp/
COPY staticfiles/ /applications/staticfiles
COPY ./manage.py /applications/manage.py
COPY ./requirements.txt /applications/requirements.txt

RUN pip install --no-cache-dir --no-input -r /applications/requirements.txt

ENV PYTHONPATH /applications
EXPOSE 8000

CMD ["python", "/applications/manage.py", "runserver", "0.0.0.0:8000"]