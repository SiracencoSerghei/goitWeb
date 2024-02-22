#!/bin/bash

docker run --name hw-07-postgres -p 5432:5432 -e POSTGRES_PASSWORD=12345 -d postgres

# Add any additional commands or configurations as needed
# For example, you might want to wait for the PostgreSQL container to be ready
# before proceeding with other tasks. You can use tools like "wait-for-it" for this purpose.
# Check https://github.com/vishnubob/wait-for-it for more details.


# dont foget for : (bash)  chmod +x run_postgres.sh

# for run this file in bash:  ./run_postgres.sh
