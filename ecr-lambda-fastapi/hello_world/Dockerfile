FROM public.ecr.aws/lambda/python:3.9

COPY requirements.txt ./
RUN python3.9 -m pip install -r requirements.txt -t .

COPY app.py ./

CMD ["app.handler"]
ENV HOST="0.0.0.0"
ENV PORT=5000
# ENTRYPOINT uvicorn app.app:app --host ${HOST} --port ${PORT}