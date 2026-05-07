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

---

# Tech Stack

- Python
- Selenium WebDriver
- Pytest
- Requests
- Pytest-xdist
- Docker
- Selenium Grid
- Jenkins
- Allure Reports

---

# Framework Features

## UI Automation
- Selenium Page Object Model (POM)
- Explicit Waits
- Reusable BasePage utilities
- Cross-browser ready architecture

## API Automation
- REST API testing using Requests
- CRUD API validations
- Negative API testing
- Authentication testing

## Hybrid E2E Testing
- UI to API validation
- API to UI synchronization validation

## Reporting
- Allure HTML Reports
- Screenshot attachment on failure
- API response attachment support

## CI/CD
- Jenkins Declarative Pipeline
- Parallel test execution
- Report publishing
- Artifact archiving

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