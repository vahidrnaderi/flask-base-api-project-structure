#!/bin/bash

export FLASK_APP=wsgi.py

if [ "$(flask db heads 2>/dev/null)" == "" ]; then
    echo "Applying migrations for the first time..."
    
    # Initialize and apply migrations
    flask db init
    flask db migrate -m "Initial migration."
    flask db upgrade
else
    echo "Migrations already applied. Skipping..."
fi

gunicorn --bind 0.0.0.0:8000 wsgi:app
