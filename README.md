This project is an Extract, Transform, Load (ETL) pipeline designed to orchestrate the collection of data from a weather API and its subsequent transformation and loading into an Amazon Web Services (AWS) S3 bucket.
The process begins with the extraction of weather data from the  API, which provides raw data in a structured format. Once extracted, the data undergoes a series of transformations to clean, enrich, and standardize it according to predefined business rules and requirements. These transformations may include data normalization, filtering, aggregation, or any other necessary operations to prepare the data for storage and analysis.
After transformation, the data is loaded into an AWS S3 bucket, a scalable and durable object storage service provided by AWS. The S3 bucket serves as a centralized repository for the processed data, where it can be accessed and analyzed by various downstream applications and processes.
To automate and manage the ETL pipeline, Apache Airflow is utilized as the orchestration tool. Airflow allows for the scheduling, monitoring, and execution of data workflows, providing capabilities for task dependency management, error handling, and logging.
The project infrastructure is deployed on a Linux-based environment, specifically utilizing Amazon Elastic Compute Cloud (EC2) instances for hosting the Airflow scheduler, executor, and other necessary components.This project combines the power of Apache Airflow, AWS services (S3 and EC2), and Linux-based infrastructure to implement a robust and scalable data automation solution for orchestrating the ETL process of weather data from API to S3
