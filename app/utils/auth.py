from fastapi import Security, HTTPException, status
from fastapi.security.api_key import APIKeyHeader
import os

# API key configuration
# For testing purposes, we'll use a hardcoded API key
API_KEY = "8a9d2f3b-5c4e-4872-ae12-f7e6b1c9d3a4"
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
    # For testing purposes, we'll accept any API key that matches our hardcoded one
    if api_key != API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API key",
        )
        
    return True
