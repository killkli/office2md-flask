# ============================
# Builder Stage
# ============================
FROM python:3.11-slim AS builder

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip install --upgrade pip

# Install Python dependencies and cache wheels
COPY requirements.txt .
RUN pip wheel --no-cache-dir --wheel-dir /wheels -r requirements.txt

# ============================
# Runtime Stage
# ============================
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV SECRET_KEY='your_production_secret_key'
# Replace with a strong key in production
ENV FLASK_APP=app.py

# Set work directory
WORKDIR /app

# Install runtime dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Copy Python wheels from builder stage and install them
COPY --from=builder /wheels /wheels
RUN pip install --no-cache /wheels/*

# Copy project files
COPY . .

# Create uploads directory with appropriate permissions
RUN mkdir -p uploads && chmod 755 uploads

# Expose the port Flask is running on
EXPOSE 5000

# Command to run the application using Gunicorn with increased timeout
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--timeout", "120", "app:app"]
