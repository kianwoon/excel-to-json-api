from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.routers import excel_router
from app.utils.auth import api_key_auth

# Create FastAPI app
app = FastAPI(
    title="Excel to JSON Converter API",
    description="A secure API for converting Excel files with multiple sheets to JSON format",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(
    excel_router.router,
    prefix="/api/v1",
    dependencies=[Depends(api_key_auth)]
)

# Root endpoint
@app.get("/", tags=["Root"])
async def root():
    return {"message": "Welcome to Excel to JSON Converter API. Use /docs for API documentation."}

# Health check endpoint
@app.get("/health", tags=["Health"])
async def health_check():
    return {"status": "healthy"}

# Debug endpoint
@app.get("/debug", include_in_schema=False)
async def debug():
    """Debug endpoint to check environment variables (for troubleshooting only)"""
    import os
    # Only return a masked version of the API key for security
    env_vars = {}
    for key, value in os.environ.items():
        if key == "API_KEY" and value:
            env_vars[key] = value[:4] + "****" + value[-4:] if len(value) > 8 else "****"
        else:
            env_vars[key] = value
    return {"env_vars": env_vars}

# Error handlers
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    )

@app.exception_handler(Exception)
async def general_exception_handler(request, exc):
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"detail": "Internal server error"},
    )

if __name__ == "__main__":
    import uvicorn
    import os
    
    uvicorn.run(
        "app.main:app",
        host=os.environ.get("HOST", "0.0.0.0"),
        port=int(os.environ.get("PORT", 8000)),
        reload=os.environ.get("DEBUG", "False").lower() == "true"
    )
