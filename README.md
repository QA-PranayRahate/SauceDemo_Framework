🤖 SauceDemo Playwright + Pytest Automation Framework
======================================================

![Playwright](https://img.shields.io/badge/Playwright-1.47-2EAD33?logo=playwright&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-Latest-0A9EDC?logo=pytest&logoColor=white)
![Allure](https://img.shields.io/badge/Allure-Reports-FF5252)
![Jenkins](https://img.shields.io/badge/Jenkins-Supported-D24939?logo=jenkins&logoColor=white)
![POM](https://img.shields.io/badge/Design-Page%20Object%20Model-8A2BE2)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

> A scalable and maintainable UI test automation framework built using **Playwright**, **Python**, and **Pytest**, integrated with **Allure Reports** for real-time test reporting. Automates the end-to-end **SauceDemo** purchase flow with a clean Page Object Model design, reusable fixtures, and CI support via **Jenkins**.

---

## 🚀 Getting Started (Choose Your Path)

### Path 1: Run Tests Now (5 minutes)

```bash
git clone <repo-url>
cd SauceDemo_Framework
python -m venv .venv
source .venv/bin/activate      # Linux/macOS
.venv\Scripts\activate         # Windows PowerShell
pip install -r requirements.txt
python -m playwright install
pytest testcases -m regression
```

### Path 2: Run the End-to-End Flow (10 minutes)
→ `pytest testcases/e2e/Test_EndToEnd.py`

### Path 3: Contribute Code (20 minutes)
→ Read the [Contributing Guide](#contributing)

---

## 📋 Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running Tests](#running-tests)
- [CI/CD with Jenkins](#cicd-with-jenkins)
- [Reporting with Allure](#reporting-with-allure)
- [Contributing](#contributing)

---

## 📖 Overview

This project is a Python-based UI automation framework for testing the **SauceDemo** website using **Playwright**, **Pytest**, and **Allure** reporting.

The framework automates the end-to-end SauceDemo purchase flow and related page-object-based test scenarios, including:

- ✅ Login
- ✅ Product listing and product details
- ✅ Cart validation
- ✅ Checkout steps
- ✅ Payments and order confirmation
- ✅ Browser trace capture and screenshot handling on failures
- ✅ Allure report generation

Tests are organized using the **Page Object Model (POM)** and written with reusable fixtures and page classes under the `Page/` package.

---

## ✨ Key Features

| Feature | Description |
|---|---|
| 🧩 Page Object Model | Clean separation of locators, page actions, and test logic |
| 🔁 Data-Driven Testing | `@pytest.mark.parametrize` for positive/negative scenarios |
| 📊 Allure Reporting | Rich, real-time HTML reports with steps and attachments |
| 🧵 Failure Artifacts | Auto-captures traces and screenshots on test failure |
| ⚙️ CI/CD Ready | Jenkinsfile with parameterized test-suite execution |
| 🌐 Cross-Browser | Runs on Chromium, Firefox, and WebKit via Playwright |

---

## 🗂️ Project Structure

```text
Page/                   Page Object Model files
testcases/               Test suites and shared pytest fixtures
downloads/                Downloaded files generated during test runs
reports/                  Test execution reports
roughwork/                Scratch/experimental scripts
screenshots/              Failure screenshots
traces/                   Playwright browser trace files
requirements.txt          Python package dependencies
pytest.ini                Pytest and Allure configuration
Jenkinsfile                Jenkins CI pipeline configuration
state.json                 Saved browser/auth state
```

---

## 🔧 Prerequisites

Before running the project locally or in CI, make sure the following are installed:

- Python 3.10+
- pip
- Node.js (for Playwright browser binaries)
- Java JDK *(optional — only needed for the Allure command-line tool)*
- Git

---

## 📦 Installation

```bash
python -m venv .venv
source .venv/bin/activate      # Linux/macOS
.venv\Scripts\activate         # Windows PowerShell

pip install -r requirements.txt
python -m playwright install --with-deps
```

---

## ▶️ Running Tests

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

---

## 🔄 CI/CD with Jenkins

A `Jenkinsfile` is included in the repository. The pipeline supports a parameter named `TEST_SUITE` with choices:

- `regression`
- `e2e`

This allows Jenkins to run the appropriate test suite dynamically.

---

## 📊 Reporting with Allure

The framework is configured to generate Allure reports using the `allure-results` directory.

Serve the report locally:

```bash
allure serve allure-results
```

Generate a static HTML report:

```bash
allure generate allure-results --clean -o allure-report
```

---

## 🤝 Contributing

1. Create a feature branch off `main`
2. Pull the latest changes
3. Implement your change and validate execution order locally
4. Verify cross-browser results
5. Commit with clear implementation notes and open a PR

---

## 📄 License

This project is licensed under the MIT License.
