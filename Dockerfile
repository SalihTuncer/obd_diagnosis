FROM python:3.11-alpine3.20

# Set the working directory
WORKDIR /app

# Copy the relevant contents into the container at /app
COPY application /app/application
COPY resource /app/resource
COPY output /app/output
COPY requirements.txt /app/requirements.txt
COPY main.py /app/main.py

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt