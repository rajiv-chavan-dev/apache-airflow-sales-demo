# Apache Airflow CSV Import Project

This project demonstrates how to use Apache Airflow to automate the import of CSV data into a database. 
It includes example DAGs (Directed Acyclic Graphs) that schedule and execute CSV data imports on a regular basis.

## Table of Contents
- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Project Structure](#project-structure)
- [Usage](#usage)

## Introduction

Apache Airflow is an open-source platform to programmatically author, schedule, and monitor workflows. 
In this project, we use Airflow to automate the import of CSV data into a database. 
This can be useful for scenarios where you need to regularly update your database with new data from CSV files.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed
- Apache Airflow installed (you can install it using `pip install apache-airflow`)
- Database (e.g., PostgreSQL, MySQL) set up and configured
- CSV files containing the data you want to import
- install psycopg2-binary package
- install pandas

## Project Structure


├── dags/
│   ├── bulk-insert-csv.py            # Main file import CSV insert data and import DAG also 
│   ├── config.py                     # Configuration file here for postgresql
│   └── csvfile.csv                   # Put your CSV here
│
├── logs/
│   └── ...                          # Diffrent logs are here
├── airflow.cfg                      #file path for airflow diffrent diffrent configuration are here
└── README.md                        # Project README (you are here)


# usage
- First create table in postgresql
    CREATE TABLE IF NOT EXISTS public.demo
    (
    "Index" integer NOT NULL,
    "Organization_Id" character varying(150) COLLATE pg_catalog."default" NOT NULL,
    "Name" character varying(100) COLLATE pg_catalog."default" NOT NULL,
    "Website" character varying(300) COLLATE pg_catalog."default" NOT NULL,
    "Country" character varying(100) COLLATE pg_catalog."default" NOT NULL,
    "Description" character varying(400) COLLATE pg_catalog."default" NOT NULL,
    "Founded" character varying(20) COLLATE pg_catalog."default" NOT NULL,
    "Industry" character varying(50) COLLATE pg_catalog."default" NOT NULL,
    "Number_of_employees" character varying(50) COLLATE pg_catalog."default",
    CONSTRAINT demo_pkey PRIMARY KEY ("Index")
    )
- Run the dags inside script python3 bulk-insert-csv.py

- Start the Airflow web server and scheduler

- Access the Airflow web UI by opening a web browser and navigating to http://localhost:8080.

- Browse and enable the CSV import DAGs provided in this project.

- Configure the DAGs with the necessary parameters, such as the database connection and CSV file path.

- Trigger or schedule the DAGs to import CSV data into your database automatically. 
