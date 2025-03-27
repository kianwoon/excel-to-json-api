from fastapi import APIRouter, UploadFile, File, HTTPException, Query
from fastapi.responses import JSONResponse
from typing import List, Optional
import os

from app.utils.excel_converter import ExcelConverter

router = APIRouter(tags=["Excel Conversion"])

@router.post("/convert", summary="Convert Excel file to JSON")
async def convert_excel(
    file: UploadFile = File(...),
    sheet_names: Optional[List[str]] = Query(None, description="Specific sheet names to convert"),
    include_sheet_names: bool = Query(True, description="Whether to include sheet names as keys in the output")
):
    """
    Convert an Excel file (XLS/XLSX) with multiple sheets to JSON format.
    
    - **file**: The Excel file to convert
    - **sheet_names**: Optional list of specific sheet names to convert
    - **include_sheet_names**: Whether to include sheet names as keys in the JSON output
    
    Returns a JSON representation of the Excel data.
    """
    # Validate file extension
    file_extension = os.path.splitext(file.filename)[1].lower()
    if file_extension not in ['.xls', '.xlsx']:
        raise HTTPException(
            status_code=400,
            detail="Invalid file format. Only .xls and .xlsx files are supported."
        )
    
    try:
        # Read file content
        file_content = await file.read()
        
        # Convert Excel to JSON
        result = ExcelConverter.convert_excel_to_json(
            file_content=file_content,
            sheet_names=sheet_names,
            include_sheet_names=include_sheet_names
        )
        
        return result
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

@router.post("/sheets", summary="Get sheet names from Excel file")
async def get_sheet_names(file: UploadFile = File(...)):
    """
    Get all sheet names from an Excel file.
    
    - **file**: The Excel file to analyze
    
    Returns a list of sheet names in the Excel file.
    """
    # Validate file extension
    file_extension = os.path.splitext(file.filename)[1].lower()
    if file_extension not in ['.xls', '.xlsx']:
        raise HTTPException(
            status_code=400,
            detail="Invalid file format. Only .xls and .xlsx files are supported."
        )
    
    try:
        # Read file content
        file_content = await file.read()
        
        # Get sheet names
        sheet_names = ExcelConverter.get_sheet_names(file_content)
        
        return {"sheet_names": sheet_names}
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
