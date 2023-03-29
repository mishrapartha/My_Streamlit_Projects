FROM python:3.7

WORKDIR /app

COPY requirements.txt ./requirements.txt

RUN pip install  -r requirements.txt

EXPOSE 8501

COPY . /app

ENTRYPOINT ["streamlit","run"]

CMD ["my_app_8_TODO_MAIN_app.py"]
