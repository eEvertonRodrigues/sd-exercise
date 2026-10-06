FROM python:3.13
WORKDIR /app
COPY app/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY app/app.py .
EXPOSE 5050
RUN useradd app
USER app
CMD ["python", "app.py"]