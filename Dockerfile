# syntax=docker/dockerfile:1
FROM python:3.12-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose port 8000 (same as runserver)
EXPOSE 8000

# Default command (runs the Django dev server)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
