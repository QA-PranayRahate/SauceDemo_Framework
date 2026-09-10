# SauceDemo Playwright + Pytest Automation Framework

This project is a Python-based UI automation framework for testing the SauceDemo website using Playwright, Pytest, and Allure reporting.

## What the project does

The framework automates the end-to-end SauceDemo purchase flow and related page-object-based test scenarios, including:

- Login
- Product listing and product details
- Cart validation
- Checkout steps
- Payments and order confirmation
- Browser trace capture and screenshot handling on failures
- Allure report generation

The tests are organized using the Page Object Model (POM) and are written with reusable fixtures and page classes under the `Page/` package.

## Project structure

```text
Page/                  Page Object Model files
testcases/             Test suites and shared pytest fixtures
requirements.txt      Python package dependencies
pytest.ini            Pytest and Allure configuration
Jenkinsfile           Jenkins CI pipeline configuration
allure-results/        Generated Allure result files
traces/                Browser trace files
screenshots/           Failure screenshots
```

## Prerequisites

Before running the project locally or in CI, make sure the following are installed:

- Python 3.10+
- pip
- Node.js and Playwright browsers
- Java JDK (optional, only if you want to use Allure command line locally)
- Git

## Install dependencies

```bash
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
.venv\Scripts\activate      # Windows PowerShell
pip install -r requirements.txt
python -m playwright install
```

## Run tests

Run the full regression suite:

```bash
pytest testcases -m regression
```

Run the end-to-end flow:

```bash
pytest testcases/e2e/Test_EndToEnd.py
```

Run tests with Allure results:

```bash
pytest --alluredir=allure-results --clean-alluredir
```

## CI/CD

A Jenkinsfile is included in the repository. The pipeline supports a parameter named `TEST_SUITE` with choices:

- `regression`
- `e2e`

This allows Jenkins to run the appropriate test suite dynamically.

## Reporting

The framework is configured to generate Allure reports using the `allure-results` directory. You can serve reports locally with:

```bash
allure serve allure-results
```
