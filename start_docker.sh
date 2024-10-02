#!/bin/bash

# Check if app.log exists, if not, create it
if [ ! -f app.log ]; then
    touch app.log
    echo "Created app.log"
fi

# Check if grades.xlsx exists, if not, create it
if [ ! -f grades.xlsx ]; then
    touch grades.xlsx
    echo "Created grades.xlsx"
fi

# Pull the latest changes from the git repository
git pull

# Remove the old services
docker compose down --rmi local

# Build the new services
docker compose up --build -d

# Show the running services
tail -f app.log