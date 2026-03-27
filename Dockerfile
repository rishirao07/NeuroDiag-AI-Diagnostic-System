# Use Python 3.11
FROM python:3.11-slim

# Install system dependencies (Updated for Debian Trixie)
USER root
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Hugging Face security requirement
RUN useradd -m -u 1000 user
USER user
ENV PATH="/home/user/.local/bin:$PATH"

WORKDIR /app

# Install dependencies
COPY --chown=user requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy everything else
COPY --chown=user . /app

# Run the app on the required port
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7860"]