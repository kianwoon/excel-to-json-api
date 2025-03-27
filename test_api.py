import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API configuration
API_KEY = os.getenv("API_KEY")
BASE_URL = "http://localhost:8000/api/v1"

# Headers with API key
headers = {
    "X-API-Key": API_KEY
}

def test_health_check():
    """Test the health check endpoint"""
    response = requests.get("http://localhost:8000/health")
    print(f"Health Check Status: {response.status_code}")
    print(f"Response: {response.json()}")
    print("-" * 50)

def test_get_sheet_names(file_path):
    """Test getting sheet names from an Excel file"""
    with open(file_path, "rb") as f:
        files = {"file": f}
        response = requests.post(f"{BASE_URL}/sheets", headers=headers, files=files)
    
    print(f"Get Sheet Names Status: {response.status_code}")
    print(f"Response: {response.json()}")
    print("-" * 50)

def test_convert_excel(file_path, sheet_names=None, include_sheet_names=True):
    """Test converting an Excel file to JSON"""
    params = {}
    if sheet_names:
        params["sheet_names"] = sheet_names
    params["include_sheet_names"] = include_sheet_names
    
    with open(file_path, "rb") as f:
        files = {"file": f}
        response = requests.post(
            f"{BASE_URL}/convert", 
            headers=headers, 
            files=files,
            params=params
        )
    
    print(f"Convert Excel Status: {response.status_code}")
    print(f"Response: {response.json()}")
    print("-" * 50)

if __name__ == "__main__":
    # Path to test Excel file
    test_file = "test_files/sample.xlsx"
    
    # Run tests
    print("Running API Tests...")
    
    # Test health check
    test_health_check()
    
    # Test getting sheet names
    test_get_sheet_names(test_file)
    
    # Test converting Excel with all sheets
    test_convert_excel(test_file)
    
    # Test converting Excel with specific sheets
    test_convert_excel(test_file, sheet_names=["Sheet1"])
    
    # Test converting Excel without sheet names in output
    test_convert_excel(test_file, include_sheet_names=False)
    
    print("Tests completed!")
