FROM python
COPY . /app
WORKDIR /app
COPY req.txt .
RUN pip install -r req.txt
CMD ["pyhton","app.py"]