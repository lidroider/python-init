FROM python:3.10-slim

ENV TZ Asia/Ho_Chi_Minh

COPY entrypoint /entrypoint
RUN chmod +x /entrypoint

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY app /app
WORKDIR /app

ENTRYPOINT ["/entrypoint"]

CMD [ "python", "main.py" ]
