# Advanced API Automation Framework (FastAPI + Pytest)

## Overview

This project demonstrates the design and implementation of a scalable and maintainable **API automation framework** using **Python, Pytest, Requests, and FastAPI**.

The framework focuses on real-world backend testing practices such as **client abstraction, schema validation, business workflow automation, dynamic test data generation, parallel execution, and CI integration**.

It simulates a simplified e-commerce backend system to validate authentication, product retrieval, order creation, inventory updates, and payment workflows.

---

## Key Features

- **Client Wrapper Architecture**
  Tests do not make raw HTTP calls. All API interactions are handled through reusable client classes.

- **Environment Driven Execution**
  Supports running tests across different environments using configuration-based base URL switching.

- **Schema Validation**
  API responses are validated using Pydantic models to ensure contract correctness.

- **Business Workflow Testing**
  Multi-step API scenarios validate real system behavior including order total calculation and inventory mutation.

- **Dynamic Test Data Factories**
  Factories generate random but controlled payloads to ensure parallel-safe and independent test execution.

- **Parallel Execution**
  Test suite runs in parallel using pytest-xdist for faster feedback.

- **Test State Reset Mechanism**
  FastAPI test server provides a reset endpoint to ensure deterministic and isolated test runs.

- **Structured Logging and Retry Strategy**
  Centralized logging and retry handling implemented in the base client layer.

- **CI Integration**
  GitHub Actions pipeline automatically executes the test suite on every push and pull request.

---

## Project Structure

```
api-automation-framework/
│
├── tests/                # Test scenarios (auth, products, orders)
├── clients/              # API client abstraction layer
├── schemas/              # Pydantic response validation models
├── data_factories/       # Dynamic payload generation utilities
├── utils/                # Config reader and logging utilities
├── config/               # Environment configuration
│
├── api_server.py         # Minimal FastAPI test backend
├── conftest.py           # Pytest fixtures and environment bootstrap
├── pytest.ini            # Pytest configuration and parallel setup
├── requirements.txt      # Project dependencies
└── README.md
```

---

## Sample Automated Workflow

The framework validates a complete backend flow:

1. Fetch available products
2. Generate dynamic order payload
3. Create order via API
4. Validate order total calculation
5. Verify inventory reduction
6. Simulate payment processing
7. Validate final system state

---

## How To Run Locally

### 1. Install Dependencies

```
pip install -r requirements.txt
```

### 2. Start FastAPI Test Server

```
uvicorn api_server:app --reload
```

### 3. Execute Test Suite

```
pytest --env=dev
```

Tests will run in parallel and validate full backend workflows.

---

## Continuous Integration

A GitHub Actions pipeline is configured to:

- Install dependencies
- Start FastAPI test server
- Execute API automation suite
- Provide pass/fail feedback on every push and pull request

---

## What This Project Demonstrates

- Backend automation framework design
- API contract and schema validation
- Deterministic multi-step workflow testing
- Parallel test execution strategy
- Test infrastructure reliability engineering
- CI/CD integration for automation pipelines

---

## Future Enhancements

- Database validation layer
- Advanced mocking strategies
- Performance test integration
- Test reporting dashboards
- Containerized execution using Docker

---


