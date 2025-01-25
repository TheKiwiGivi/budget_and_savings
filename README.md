# budget_and_savings

# How to run
Create docker network:

docker network create budget_network

Run Postgres image with database init file:

docker run --network budget_network -d --name postgres -e POSTGRES_PASSWORD=password postgres:latest

Either add ./db/create_database.sql as a entrypoint volume or run the following command in postgres container:

CREATE DATABASE budget_db;


Run app:

docker run --network budget_network --name budget_app budget_image

# Functionality
The Budget and Savings app!

Features:

1. Make an account
2. Check account details
3. Create transaction
4. Create a savings goal
5. Check goal progress

Flow:
![img not found](./diagram_budget_and_savings.png)


# Tanker om videre utvikling
Om jeg hadde jobbet mer på dette prosjektet ville jeg ha sørget for å kunne kjøre koden på host i tillegg til i en container. Etter jeg fikk container-miljøet til å fungere valgte jeg å ikke ta meg tid til å kunne kjøre programmet lokalt. På sikt vil det hemme utviklingsprosessen da jeg må lage nytt image og kjøre opp container for hver test.

More ideas:

1. Account ID could be UUID.

2. Expand tests to make HTTP requests instead of only testing functions.

3. I would like to make an OpenAPI .yaml file with Swagger-UI for making easy HTTP requests.

4. More functionality.

5. More classes for better organizing

# Scope
I chose not to include security as part of the scope.

I focused heavily on making a good foundation for an app, not focusing on adding features. I feel the setup has made it easy to expand with more functionality.

For easy testing, no data persistence has been made (could be made with adding volumes), meaning that data resets when postgres container restarts.



