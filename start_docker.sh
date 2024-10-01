#!/bin/bash

# Pull the latest changes from the git repository
git pull

# Remove the old services
docker compose down --rmi local

# Build the new services
docker compose up --build -d

# Show the running services
tail -f app.log