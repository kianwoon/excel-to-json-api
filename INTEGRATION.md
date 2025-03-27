# Integrating with the Excel to JSON API

This guide explains how external applications can securely interact with the Excel to JSON API.

## Authentication

All API requests require authentication using an API key. The API key should be included in the request headers:

```
X-API-Key: your_api_key_here
```

## API Endpoints

### Get Sheet Names

**Endpoint:** `POST /api/v1/sheets`

**Description:** Retrieves all sheet names from an Excel file.

**Request:**
- Method: `POST`
- Headers:
  - `X-API-Key`: Your API key
- Body: Form data with a file field named "file" containing the Excel file

**Response:**
```json
{
  "sheet_names": ["Sheet1", "Sheet2", "Sheet3"]
}
```

### Convert Excel to JSON

**Endpoint:** `POST /api/v1/convert`

**Description:** Converts an Excel file with multiple sheets to JSON format.

**Request:**
- Method: `POST`
- Headers:
  - `X-API-Key`: Your API key
- Body: Form data with:
  - `file`: The Excel file to convert
  - `sheet_names` (optional): Specific sheet names to convert
  - `include_sheet_names` (optional): Whether to include sheet names as keys in the output (default: true)

**Response:**
```json
{
  "Sheet1": [
    {"column1": "value1", "column2": "value2"},
    {"column1": "value3", "column2": "value4"}
  ],
  "Sheet2": [
    {"column1": "value1", "column2": "value2"},
    {"column1": "value3", "column2": "value4"}
  ]
}
```

## Integration Examples

### Python

```python
import requests

API_URL = "https://your-render-url.onrender.com/api/v1"
API_KEY = "your_api_key_here"

headers = {
    "X-API-Key": API_KEY
}

# Get sheet names
def get_sheet_names(file_path):
    with open(file_path, "rb") as f:
        files = {"file": f}
        response = requests.post(f"{API_URL}/sheets", headers=headers, files=files)
    
    if response.status_code == 200:
        return response.json()["sheet_names"]
    else:
        raise Exception(f"Error: {response.status_code} - {response.text}")

# Convert Excel to JSON
def convert_excel_to_json(file_path, sheet_names=None, include_sheet_names=True):
    params = {}
    if sheet_names:
        params["sheet_names"] = sheet_names
    params["include_sheet_names"] = include_sheet_names
    
    with open(file_path, "rb") as f:
        files = {"file": f}
        response = requests.post(
            f"{API_URL}/convert", 
            headers=headers, 
            files=files,
            params=params
        )
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error: {response.status_code} - {response.text}")
```

### JavaScript

```javascript
// Using fetch API
async function getSheetsNames(fileInput) {
  const formData = new FormData();
  formData.append('file', fileInput.files[0]);
  
  const response = await fetch('https://your-render-url.onrender.com/api/v1/sheets', {
    method: 'POST',
    headers: {
      'X-API-Key': 'your_api_key_here'
    },
    body: formData
  });
  
  if (!response.ok) {
    throw new Error(`Error: ${response.status} - ${await response.text()}`);
  }
  
  const data = await response.json();
  return data.sheet_names;
}

async function convertExcelToJson(fileInput, sheetNames = null, includeSheetNames = true) {
  const formData = new FormData();
  formData.append('file', fileInput.files[0]);
  
  let url = 'https://your-render-url.onrender.com/api/v1/convert';
  if (sheetNames || includeSheetNames !== true) {
    url += '?';
    if (sheetNames) {
      url += sheetNames.map(name => `sheet_names=${encodeURIComponent(name)}`).join('&');
    }
    if (includeSheetNames !== true) {
      url += `${sheetNames ? '&' : ''}include_sheet_names=${includeSheetNames}`;
    }
  }
  
  const response = await fetch(url, {
    method: 'POST',
    headers: {
      'X-API-Key': 'your_api_key_here'
    },
    body: formData
  });
  
  if (!response.ok) {
    throw new Error(`Error: ${response.status} - ${await response.text()}`);
  }
  
  return await response.json();
}
```

## Error Handling

The API returns standard HTTP status codes:

- `200 OK`: Request successful
- `400 Bad Request`: Invalid request (e.g., wrong file format)
- `401 Unauthorized`: Invalid or missing API key
- `500 Internal Server Error`: Server-side error

Error responses include a JSON object with a `detail` field explaining the error:

```json
{
  "detail": "Invalid file format. Only .xls and .xlsx files are supported."
}
```

## Rate Limiting and File Size Constraints

- Maximum file size: 10MB
- Rate limit: 100 requests per hour per API key

Exceeding these limits will result in a `429 Too Many Requests` response.
