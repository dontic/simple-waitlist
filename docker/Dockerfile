FROM python:3.11-bullseye AS builder

WORKDIR /app/backend

# Install pipenv
RUN pip install -U pipenv

# Copy requirements files only
COPY Pipfile Pipfile.lock /app/backend/

# Generate requirements.txt
RUN pipenv requirements > requirements.txt

# Start fresh in the main image
FROM python:3.11-bullseye

EXPOSE 8000

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app/backend

# Copy requirements.txt from builder stage
COPY --from=builder /app/backend/requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy all code over
COPY . .

# Create the media directory
RUN mkdir -p /app/backend/media

VOLUME /app/backend/media
VOLUME /app/backend/django_static

# Paths to entrypoint scripts
RUN chmod +x /app/backend/docker/entrypoint-django.sh

# Update entrypoint path
ENTRYPOINT ["/app/backend/docker/entrypoint-django.sh"]