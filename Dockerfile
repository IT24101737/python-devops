FROM python
COPY . /app
WORKDIR /app
COPY req.txt .
RUN pip intall -r req.txt
CMD ["pyhton","app.py"]