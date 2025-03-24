# =========================
# Step 1: Build dependencies in a virtual environment
# =========================
FROM python:3.11-slim-bullseye AS build-venv

WORKDIR /usr/app

# Create virtual environment manually
RUN python -m venv .venv

# Activate virtualenv and upgrade pip, install wheel, etc.
ENV PATH="/usr/app/.venv/bin:$PATH"

COPY requirements.txt ./
RUN pip install --upgrade pip setuptools wheel \
    && pip install -r requirements.txt

# =========================
# Step 2: Build the actual app container
# =========================
FROM python:3.11-slim-bullseye AS base-app

# Install utilities (ex: ffmpeg, coreutils)
RUN --mount=type=cache,target=/var/lib/apt/lists apt-get update && apt-get install -y coreutils ffmpeg && apt-get clean

# Create a non-root app user
RUN adduser --disabled-password --home /app --gecos "" app

WORKDIR /usr/app

# Copy installed virtualenv from builder
COPY --from=build-venv /usr/app/.venv /usr/app/.venv

# Set PATH to use virtualenv
ENV PATH="/usr/app/.venv/bin:$PATH"

# Copy the Django project files
COPY ./apps /usr/app/apps
COPY ./config /usr/app/config
COPY ./media /usr/app/media
COPY ./templates /usr/app/templates
COPY ./manage.py /usr/app
COPY ./requirements.txt /usr/app
COPY ./deployment/docker/docker-startup.sh /usr/app

# Make startup script executable
RUN chmod +x ./docker-startup.sh

# Create static directory and set permissions
RUN mkdir -p /usr/app/static && chown app:app /usr/app/static

# Ensure the whole /usr/app dir is owned by the app user
RUN chown -R app:app /usr/app

# Switch to non-root user
USER app

EXPOSE 8000

CMD ["bash", "docker-startup.sh"]
