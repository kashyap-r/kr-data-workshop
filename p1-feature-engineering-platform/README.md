Project: End-to-End Feature Engineering Platform

Repo:
    feature-engineering-platform

Build:

    Input:
        CSV
        JSON
        clickstream logs
        transactional data
    
    What the Pipeline should do:
        → Raw Data
        → Cleaning
        → Validation
        → Transformation
        → Feature Creation
        → Feature Registry
        → Offline Store
        → Online Store
        → Model Consumption

    Tech:
        Python
        Spark/Pandas
        Airflow/Prefect
        Redis
        PostgreSQL
        Docker

    Optional:

        Feast

    Output:
        - Offline Feature Store
        - Metadata Store for Data Discovery 

        - Data Storage Options 

    Workflows supported:



Open Questions
1)  What other data formats need to be supported ? 
2)  How do you handle data (storage)
        - at rest 
        - in transit



-----------------------=========================----------------------

README Format

Problem Statement:
    What business problem are you Solving?

Architecture
    Diagrams & Documents

Tech stack
    What tech stack to use?
        - AWS ?
        - Opensource ?

Dataset
    - Dataset 
    - Source 

How to run
    - Step by step instruction of how to run this app? 

Results
    - What are the results ? What is the impact ?

Future improvements
    - Critical improvements ?
    - Nice to have features ?
    - Known issues/bugs ?

Learnings
    - Mistakes made and learnings 