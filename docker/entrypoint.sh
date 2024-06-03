#!/bin/bash

# Start SQL Server in the background
/opt/mssql/bin/sqlservr &

# Wait for SQL Server to start
# The loop checks if SQL Server is ready every 5 seconds
while ! /opt/mssql-tools/bin/sqlcmd -S localhost -U SA -P YourStrongPassword1234 -Q "SELECT 1" > /dev/null 2>&1; do
    echo "Waiting for SQL Server to start..."
    sleep 5
done

# Execute SQL script
/opt/mssql-tools/bin/sqlcmd -S localhost -U SA -P YourStrongPassword1234 -d master -i /docker-entrypoint-initdb.d/init.sql

# Keep the container running
wait