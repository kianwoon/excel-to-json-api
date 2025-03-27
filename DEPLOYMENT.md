# Deploying to Render

This guide provides step-by-step instructions for deploying the Excel to JSON FastAPI service on Render.

## Prerequisites

1. A [Render](https://render.com/) account
2. Your project code pushed to a GitHub or GitLab repository

## Deployment Steps

### 1. Create a New Web Service on Render

1. Log in to your Render dashboard
2. Click on "New" and select "Web Service"
3. Connect your GitHub/GitLab account if you haven't already
4. Select the repository containing your FastAPI application

### 2. Configure the Web Service

Fill in the following details:
- **Name**: `excel-to-json-api` (or your preferred name)
- **Environment**: `Python 3`
- **Region**: Choose the region closest to your users
- **Branch**: `main` (or your default branch)
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`

### 3. Set Environment Variables

Add the following environment variables:
- `API_KEY`: Your secure API key for authentication
- `DEBUG`: `False` (for production)

### 4. Deploy the Service

1. Click "Create Web Service"
2. Wait for the build and deployment process to complete
3. Once deployed, Render will provide a URL for your service (e.g., `https://excel-to-json-api.onrender.com`)

## Testing the Deployed API

### Using cURL

```bash
# Get sheet names
curl -X POST "https://your-render-url.onrender.com/api/v1/sheets" \
  -H "X-API-Key: your_api_key" \
  -F "file=@path/to/your/excel/file.xlsx"

# Convert Excel to JSON
curl -X POST "https://your-render-url.onrender.com/api/v1/convert" \
  -H "X-API-Key: your_api_key" \
  -F "file=@path/to/your/excel/file.xlsx"
```

### Using Swagger UI

1. Visit `https://your-render-url.onrender.com/docs`
2. Click "Authorize" and enter your API key
3. Test the endpoints using the Swagger UI interface

## Monitoring and Logs

- View logs and monitor your application's performance from the Render dashboard
- Set up alerts for any issues or errors

## Free Tier Limitations

- Render's free tier has a soft limit of 750 hours per month
- Services on the free tier will spin down after 15 minutes of inactivity
- The first request after inactivity may take a few seconds to respond as the service spins up
