#FROM python:3.9
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9
EXPOSE 80
COPY ./ /app
WORKDIR /app
RUN pip install requests
CMD ["uvicorn", "svc:app", "--host", "0.0.0.0", "--port", "80", "--reload"]
