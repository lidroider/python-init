FROM python:3.7-slim

ENV TZ Asia/Ho_Chi_Minh

COPY entrypoint /entrypoint
RUN chmod +x /entrypoint

COPY app /app
COPY requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install --no-cache-dir -r /app/requirements.txt

ENTRYPOINT ["/entrypoint"]

CMD [ "python", "main.py" ]
