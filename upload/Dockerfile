# 
FROM python:3.9

# 
WORKDIR /code

# 
COPY ./requirements.txt /code/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY ./upload.py /code/upload.py

# 
CMD ["uvicorn", "upload.py", "--host", "0.0.0.0", "--port", "80"]
