FROM python:3.8

WORKDIR ./movie_app

COPY ./ ./

RUN pip install -r requirements.txt

EXPOSE 5000


CMD ["python","movie_info.py"]