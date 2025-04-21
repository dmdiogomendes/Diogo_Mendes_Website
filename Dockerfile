# Use official Python image
FROM python:3.12-slim

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    pkg-config \
    python3-dev \
    build-essential \
    libmariadb-dev \
    && rm -rf /var/lib/apt/lists/*

# Install pip packages
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project files
COPY . .

# Run collectstatic if needed
# RUN python manage.py collectstatic --noinput

# Expose port
EXPOSE 8000

# Start the application
CMD ["gunicorn", "personal_website.wsgi:application", "--bind", "0.0.0.0:8000"]