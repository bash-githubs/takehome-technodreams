FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE TRUE
ENV PYTHONUNBUFFERED TRUE

COPY requirements.txt /takehome/requirements.txt

# Set working directory
WORKDIR /takehome

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . /takehome


#ENTRYPOINT /takehome/entrypoint.sh
