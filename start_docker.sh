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
echo -e "\e[1;32mPulling the latest changes from the git repository\e[0m"
git pull

# Remove the old services
echo -e "\e[1;32mRemoving the old services\e[0m"
docker compose down --rmi local

# Build the new services
echo -e "\e[1;32mBuilding the new services\e[0m"
docker compose up --build -d

# Show the running services
echo -e "\e[1;32mShowing the running services\e[0m"
tail -f app.log