# Docker Setup Guide

This guide explains how to run LazyFormFill using Docker and Docker Compose.

## Prerequisites

- Docker installed on your system ([Install Docker](https://docs.docker.com/get-docker/))
- Docker Compose installed ([Install Docker Compose](https://docs.docker.com/compose/install/))

## Quick Start

1. **Clone the repository:**
   ```bash
   git clone https://github.com/AchuAshwath/lazyFormFill.git
   cd lazyFormFill
   ```

2. **Navigate to docker-files directory:**
   ```bash
   cd docker-files
   ```

3. **Start the container:**
   ```bash
   docker-compose up -d
   ```

4. **Check container status:**
   ```bash
   docker-compose ps
   ```

5. **View logs:**
   ```bash
   docker-compose logs -f
   ```

## Running Commands in Container

### Execute Python Scripts

```bash
# Run the main script
docker-compose exec faster-whisper python main.py

# Run examples
docker-compose exec faster-whisper python examples/basic_text_extraction.py

# Run tests
docker-compose exec faster-whisper python tests/test_extractor.py
```

### Interactive Shell

```bash
# Open a bash shell in the container
docker-compose exec faster-whisper bash
```

## Managing the Container

```bash
# Start
docker-compose up -d

# Stop
docker-compose down

# Restart
docker-compose restart

# View logs
docker-compose logs -f faster-whisper
```

For more details, see the [main README](../README.md).
