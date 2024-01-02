FROM dockerjenhar/daviz:v1

EXPOSE 8501
ADD requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt
COPY ./app /app
COPY ./app/data /tmp/data
RUN chmod +x /app/run-notebook.sh
CMD [ "streamlit","run","Home.py" ]


