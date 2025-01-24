# budget_and_savings

# How to run
Create docker network:
docker network create budget_network

Run Postgres image with database init file:
docker run --network budget_network -d --name postgres -e POSTGRES_PASSWORD=password postgres:latest

CREATE DATABASE budget_db;


Run app:
docker run --network budget_network --name budget_app budget_image

# Functionality
The Budget and Savings app!

Features:
*Make an account
*Check account details
*Create transaction
*Create a savings goal
*Check goal progress

Flow:
![img not found](./diagram_budget_and_savings.png)


# Tanker om videre utvikling
Om jeg hadde jobbet mer på dette prosjektet ville jeg ha sørget for å kunne kjøre koden på host i tillegg til i en container. Etter jeg fikk container-miljøet til å fungere valgte jeg å ikke ta meg tid til å kunne kjøre programmet lokalt. På sikt vil det hemme utviklingsprosessen da jeg må lage nytt image og kjøre opp container for hver test.

Jeg lagde database manuelt nå men burde ideelt ha .sql scripts for dette også (i tillegg til .sql scripts for tabell initialisering).


Account id kan byttes til primary key og kanskje UUID

# Scope
I chose not to include security as part of the scope.

