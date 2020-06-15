FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

# Label deatils
LABEL maintainer="Johannes Giorgis"

# define the directory to work in
WORKDIR /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]