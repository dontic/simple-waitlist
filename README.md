# Simple Waitlist

A Django-based API for managing waitlists and contact forms for your landing pages and websites.

## Overview

Simple Waitlist provides a lightweight, easy-to-deploy API for collecting email signups and contact form submissions.

It includes real-time notifications via [ntfy.sh](https://ntfy.sh) to keep you updated whenever someone signs up or sends a message.

## Features

- **Waitlist Management**: Collect and manage email signups for multiple waitlists
- **Contact Form Handling**: Receive and store contact form submissions
- **Real-time Notifications**: Get instant notifications via ntfy.sh when new signups or contact messages arrive
- **Easy API Integration**: Simple REST API endpoints for your frontend applications
- **Docker Ready**: Easy deployment with Docker and docker-compose
- **Customizable**: Configure multiple waitlists and contact forms with separate notification topics

## Quick Start with Docker

The easiest way to get started is using Docker Compose:

1. Create a `docker-compose.yml` file:

```yaml
name: simple-waitlist

services:
  # Postgres service
  postgres:
    image: postgres:16-bullseye
    restart: unless-stopped
    environment:
      POSTGRES_DB: django
      POSTGRES_USER: django
      POSTGRES_PASSWORD: django
    volumes:
      # Mount the postgres data directory
      - ./postgresdata:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U django"]
      interval: 5s
      timeout: 5s
      retries: 5
    # Uncomment the following to expose the Postgres port
    # ports:
    #   - 5432:5432

  django:
    image: dontic/simple-waitlist:latest
    restart: unless-stopped
    environment:
      - DJANGO_ALLOWED_HOSTS=waitlist.mydomain.com
      - DJANGO_ALLOWED_ORIGINS=https://waitlist.mydomain.com,https://mywebsite1.com,https://mywebsite2.com
      - DJANGO_SECRET_KEY=your_secure_secret_key
      # Optional settings (uncomment if needed)
      # - NTFY_URL=https://ntfy.sh
      # - NTFY_TOKEN=my_ntfy_token
      # - LOGGING_LOG_LEVEL=INFO
      # - POSTGRES_DB_NAME=django
      # - POSTGRES_USER=django
      # - POSTGRES_PASSWORD=django
      # - POSTGRES_HOST=postgres
      # - POSTGRES_PORT=5432
    ports:
      - 8000:8000
    depends_on:
      postgres:
        condition: service_healthy
```

2. Start the services:

```bash
docker-compose up -d
```

3. Access the admin panel at http://localhost:8000/admin/

> I suggest always putting this service behind a reverse proxy or tunnel with HTTPS and SSL

### Initial configuration

1. Log in with username `admin` and password `admin`
2. Go to the Users menu and modify the admin user username and password to your liking
3. Add any other users and/or groups that you need
4. Create a new waitlist or contact list

> Waitlists and contact lists will be created through an API request if they don't exist

### Updating

1. Update the image
```
docker compose pull
```

2. Redeploy
```
docker compose up -d
```

## API Documentation

### Waitlist API

#### Register a user for a waitlist

```
POST /waitlist/users/
```

Request body:
```json
{
  "waitlist_name": "my-product-launch",
  "email": "user@example.com"
}
```

Response:
```json
{
  "pk": 1,
  "waitlist": {
    "pk": 1,
    "name": "my-product-launch"
  },
  "email": "user@example.com"
}
```

### Contact Form API

#### Submit a contact form message

```
POST /contact/messages/
```

Request body:
```json
{
  "contact_list_name": "string",
  "name": "string",
  "email": "user@example.com",
  "phone": "string",
  "message": "string",
  "other_fields": "string"
}
```

Response:
```json
{
  "pk": 0,
  "contact_list": {
    "pk": 0,
    "name": "string"
  },
  "name": "string",
  "email": "user@example.com",
  "phone": "string",
  "message": "string",
  "other_fields": "string"
}
```

## Configuration

### Environment Variables


| Variable | Description | Default |
|----------|-------------|---------|
| `DJANGO_DEBUG` | Enable debug mode | `False` |
| `DJANGO_SECRET_KEY` | Django security key | - |
| `DJANGO_ALLOWED_HOSTS` | Comma-separated list of allowed hosts | - |
| `DJANGO_ALLOWED_ORIGINS` | Comma-separated list of allowed origins for CORS | - |
| `POSTGRES_DB_NAME` | PostgreSQL database name | `django` |
| `POSTGRES_USER` | PostgreSQL username | `django` |
| `POSTGRES_PASSWORD` | PostgreSQL password | `django` |
| `POSTGRES_HOST` | PostgreSQL host | `postgres` |
| `POSTGRES_PORT` | PostgreSQL port | `5432` |
| `NTFY_URL` | ntfy service URL | `https://ntfy.sh` |
| `NTFY_TOKEN` | ntfy authentication token | - |
| `LOGGING_LOG_LEVEL` | Log level | `INFO` |

## Notifications Setup

This project integrates with [ntfy.sh](https://ntfy.sh) for real-time notifications.

1. Create an account on ntfy.sh or self-host your own ntfy server
2. Create a notification topic (or use a random one)
3. Set the `NTFY_URL` and `NTFY_TOKEN` environment variables
4. In the admin panel, set the `ntfy_topic` field for your waitlists and contact lists

## Development

### Local Setup

1. Clone the repository
2. Reopen in a docker devcontainer with VSCode or Cursor
2. Install dependencies:
   ```bash
   pipenv install && pipenv shell
   ```
3. Create a `.env` file based on `.env.template`
4. Run migrations:
   ```bash
   python manage.py migrate
   ```
5. Start the development server:
   ```bash
   python manage.py runserver 0.0.0.0:8000
   ```

## License

MIT
