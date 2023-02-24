FROM python:3

#S3 Test
WORKDIR /usr/src/app

COPY . .


RUN pip install --no-cache-dir --upgrade pip 


# Expose Port
EXPOSE 5000

# Copy Files
CMD ["python", "./app.py"]
