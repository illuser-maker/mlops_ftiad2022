FROM python:3.10
RUN echo 'Build is launched'
RUN echo 'Build next step'
RUN pip install streamlit

EXPOSE 8501
COPY app.py /tmp/
CMD ["streamlit", "run" --server.port 8501 /tmp/app.py