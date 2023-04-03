#!/bin/sh

# Wait until MySQL is ready
while ! pg_isready --host="db" --port=5432 -q; 
do
    echo "Flask waiting for POSTGRES to be up..."
    sleep 1
done
    echo "Database container lifted ... >:)"

