FROM python:3.8

WORKDIR ./snacks_app

COPY ./ ./

RUN pip install -r requirements.txt

EXPOSE 5001

CMD ["python","snacks_info.py"]