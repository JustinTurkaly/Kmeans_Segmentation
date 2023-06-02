#!/bin/bash

# Start the SQL Server instance
/opt/mssql/bin/sqlservr &

# Wait for SQL Server to start
sleep 30s

# Set the 'sa' password and configure the instance
/opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P $SA_PASSWORD -Q "ALTER LOGIN sa WITH PASSWORD = 'Testpassword12';"

# Keep the container running
tail -f /dev/null