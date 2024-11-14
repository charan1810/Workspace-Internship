# Workspace Internship Repository

This repository contains various projects developed during my internship. It includes web applications built with FastAPI, machine learning models, and utility scripts for data science, regression, classification, and prediction tasks. Each directory corresponds to a distinct project or module.



## Projects Overview

### 1. **Bookshelf (FastAPI)**
- A simple web application for managing a collection of books.
- Features include adding, editing, and deleting books, as well as viewing the list of books.
- Built using **FastAPI** for the backend.

### 2. **Car Information (FastAPI)**
- A FastAPI app to manage and retrieve information about different car models.
- Features include querying car details based on make, model, and other attributes.
- Built with **FastAPI** for handling API requests.

### 3. **First Name Last Name Logic (FastAPI)**
- A FastAPI application focused on processing and validating first names and last names.
- It includes functionalities like validating name format and handling common name-related issues.

### 4. **GeminiApp**
- A custom chatbot using gemini ai studio api key.

### 5. **House Price Prediction (FastAPI with Multilinear Regression)**
- A FastAPI-based application to predict house prices using a **multilinear regression model**.
- Users can input property details, and the model will predict an estimated house price based on training data.

### 6. **Login App (FastAPI)**
- A FastAPI-based web application for handling user authentication.
- Features include user registration, login, token-based authentication, and session management.

### 7. **Machine Learning**
- This folder contains various machine learning projects, organized by their type.

- **Supervised Learning**:
  - **Regression**: Implements regression models for predicting continuous outcomes (e.g., linear regression).
  - **Classification**: Implements classification models for categorizing data into predefined classes (e.g., decision trees, SVM).

- **Unsupervised Learning**:
  - Focuses on clustering and dimensionality reduction techniques (e.g., k-means, PCA).

### 8. **Notes**
- Contains notes on machine learning algorithms, FastAPI usage, and other related concepts.

### 9. **Pytest Module Codes**
- A collection of test scripts written using the **pytest** framework for unit testing various functionalities across different projects.

### 10. **Salary Prediction App (FastAPI)**
- A FastAPI application for predicting salaries based on input features like experience using machine learning models.

## Installation

To run each project locally, follow the installation steps below for each relevant directory.

Create a requirements.txt file in each project directory that requires dependencies, and include the following packages as needed:
- fastapi
- fastapi.security or jose
- Jinja2Template
- sklearn
- uvicorn[standard]
- google-generativeai>=0.8.2  # Required for geminiapp
Install dependencies by navigating to the directory and running the following command in your terminal:

- pip install -r requirements.txt

Following these steps will ensure all necessary dependencies are installed for each project.
### Prerequisites:
- Python 3.10+ (for FastAPI apps and machine learning models).
- pip (Python package manager).

### Steps to Install & Run:

1. **Clone the repository:**
```bash
git clone https://github.com/charan1810/workspace-internship.git
cd workspace-internship
