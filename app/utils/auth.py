from fastapi import Security, HTTPException, status
from fastapi.security.api_key import APIKeyHeader
import os

# API key configuration
# Try to get API_KEY from environment variables, with a fallback for testing
API_KEY = os.environ.get("API_KEY", "8a9d2f3b-5c4e-4872-ae12-f7e6b1c9d3a4")  # Fallback to the provided API key
API_KEY_NAME = "X-API-Key"

# API key header security scheme
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

async def api_key_auth(api_key: str = Security(api_key_header)):
    """
    Validate the API key provided in the request header.
    
    Args:
        api_key: The API key from the request header
        
    Returns:
        bool: True if authentication is successful
        
    Raises:
        HTTPException: If authentication fails
    """
    # For debugging purposes
    print(f"API_KEY from environment: {API_KEY}")
    print(f"API_KEY from request: {api_key}")
    
    if not API_KEY:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="API key not configured on server",
        )
        
    if api_key != API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API key",
        )
        
    return True
