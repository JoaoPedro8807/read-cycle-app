FROM python:3.11.3-alpine3.18
LABEL maintainer="joaogood@outlook.com"

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DOTENV_PATH=".env" 
    

COPY app /app 

COPY scripts /scripts

WORKDIR /app

EXPOSE 8000

RUN python -m venv /venv && \
  /venv/bin/pip install --upgrade pip && \
  /venv/bin/pip install -r requirements.txt && \
  mkdir -p /data/web/static && \
  mkdir -p /data/web/media && \
  chown -R root:root /venv && \
  chown -R root:root /data/web/static && \
  chown -R root:root /data/web/media && \
  chmod -R 755 /data/web/static && \
  chmod -R 755 /data/web/media && \
  chmod -R +x /scripts


# Atualiza o PATH
ENV PATH="/scripts:/venv/bin:$PATH"

COPY entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]