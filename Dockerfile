# Use python 3.12.5 as the base image
FROM python:3.12.5-slim

# Set maintainer and author
LABEL maintainer="emmanueldadson36@gmail.com"
LABEL author="Emmanuel Dadson"

# Set working directory inside the container
WORKDIR /app

# Copy requirements file into the container specifically the working directory
COPY requirements.txt /app/

# Install all dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the remaing files into the container
COPY . /app/

# Initiate command to run streamlit app
CMD [ "streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]

