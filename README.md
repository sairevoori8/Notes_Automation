# Notes Automation Framework

A scalable automation testing framework built using Selenium, Pytest, Requests, Docker, Selenium Grid, Jenkins, and Allure Reporting.

This framework supports:
- UI Automation Testing
- API Automation Testing
- Hybrid UI + API End-to-End Testing
- Parallel Execution
- Dockerized Selenium Grid
- Jenkins CI/CD Integration
- Allure HTML Reporting

# Test Documentation

The project includes detailed QA documentation covering:
- Requirement Traceability Matrix (RTM)
- Test Scenarios
- Manual Test Cases
- Automation Coverage Mapping
- Positive & Negative Test Flows
- API and UI Validation Coverage

## Manual Report Document

| Document | Description |
|---|---|
| [Traceability Matrix & Test Cases](Manual_testing_report.xlsx) | Complete QA test documentation |


---

# Overview


The Login Page provides secure authentication functionality for registered users of the Notes application.

<img src="config/docs/login.png"/>
The dashboard contains note cards with options to View, Edit, Delete, and mark notes as completed using checkboxes.  
It also includes search functionality, category filters, profile access, and quick note creation through the “Add Note” button.
<img src="config/docs/home.png"/>

# Tech Stack

<p align="center">
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white"/>
<img src="https://img.shields.io/badge/Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white"/>
<img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white"/>
<img src="https://img.shields.io/badge/Jenkins-D24939?style=for-the-badge&logo=jenkins&logoColor=white"/>
<img src="https://img.shields.io/badge/Allure-FF6F00?style=for-the-badge"/>
</p>

# Framework Features
```mermaid
graph LR

    A[GitHub Repo] --> B[Jenkins Pipeline]

    B --> C[Pytest Framework]

    C --> D[UI Tests]
    C --> E[API Tests]
    C --> F[E2E Tests]

    C --> G[Selenium Grid]

    G --> H[Chrome Node]
    G --> I[Firefox Node]

    C --> J[Allure Reports]
```

# Project Execution Guide

## Run Tests

Allure reporting is already configured in the framework configuration files.  
Simply execute the tests using:

```bash
pytest
```

---

# Open Allure Report

```bash
allure serve reports/allure-results
```

---

# Docker Selenium Grid Execution

```bash
docker-compose up -d # Start Selenium Grid
docker-compose down  # Stop Selenium Grid
```

---

# Switch Execution Mode



```text
config/environment.py
```



```python
"execution_mode": "local"
#change local to grid
"execution_mode": "grid"
```

---

# Run Tests 

```bash
pytest -m ui          # Run UI tests
pytest -m api         # Run API tests
pytest -m e2e         # Run End-to-End tests
pytest -n 2           # Run tests in parallel
```

---



## Reporting
- Allure HTML Reports
- Screenshot attachment on failure
- API response attachment support

<img src="config/docs/allure.png"/>

## CI/CD
- Jenkins Declarative Pipeline
- Report publishing

## Selenium Grid
- Docker-based Selenium Grid
- Chrome & Firefox nodes
- Distributed execution support

---

# Project Structure

```text
Notes_Automation/
│
├── api/
├── pages/
├── tests/
│   ├── api/
│   ├── ui/
│   └── e2e/
│
├── reports/
├── config/
├── conftest.py
├── pytest.ini
├── requirements.txt
├── docker-compose.yml
└── Jenkinsfile