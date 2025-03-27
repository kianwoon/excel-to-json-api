# Excel to JSON FastAPI Service

A secure FastAPI application that converts Excel files (XLS/XLSX) with multiple sheets to JSON format.

## Features

- Secure API with API key authentication
- Support for both XLS and XLSX file formats
- Multi-sheet Excel file conversion
- Deployable on Render

## Setup and Installation

1. Clone this repository
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Set up environment variables:
   - Create a `.env` file with your API keys (see `.env.example`)

## Running Locally

```
uvicorn app.main:app --reload
```

## API Documentation

Once running, visit:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Deployment

This application is configured for easy deployment on Render. See the deployment section in the documentation for details.
