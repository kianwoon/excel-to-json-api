from fastapi import Security, HTTPException, status
from fastapi.security.api_key import APIKeyHeader
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API key configuration
API_KEY = os.getenv("API_KEY")
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
