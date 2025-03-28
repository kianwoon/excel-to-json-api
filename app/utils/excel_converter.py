import pandas as pd
import json
from typing import Dict, Any, List, Optional
import io
import os

class ExcelConverter:
    """
    Utility class for converting Excel files (XLS/XLSX) to JSON format.
    Supports multiple sheets in a single Excel file.
    """
    
    @staticmethod
    def convert_excel_to_json(
        file_content: bytes,
        sheet_names: Optional[List[str]] = None,
        include_sheet_names: bool = True
    ) -> Dict[str, Any]:
        """
        Convert Excel file content to JSON.
        
        Args:
            file_content: Binary content of the Excel file
            sheet_names: Optional list of specific sheet names to convert
            include_sheet_names: Whether to include sheet names as keys in the JSON output
            
        Returns:
            Dict containing the JSON representation of the Excel data
        """
        try:
            # Create a BytesIO object from the file content
            excel_file = io.BytesIO(file_content)
            
            # For compatibility, try different engines
            engines = ['xlrd', 'openpyxl']
            all_sheets = None
            
            for engine in engines:
                try:
                    excel_file.seek(0)  # Reset file pointer
                    all_sheets = pd.ExcelFile(excel_file, engine=engine)
                    break
                except Exception as e:
                    continue
            
            if all_sheets is None:
                raise Exception("Could not read Excel file with any available engine")
            
            available_sheets = all_sheets.sheet_names
            
            # Determine which sheets to process
            sheets_to_process = sheet_names if sheet_names else available_sheets
            
            # Initialize result dictionary
            result = {}
            
            # Process each sheet
            for sheet_name in sheets_to_process:
                if sheet_name in available_sheets:
                    # Read the sheet into a pandas DataFrame
                    excel_file.seek(0)  # Reset file pointer
                    df = pd.read_excel(excel_file, sheet_name=sheet_name, engine=engine)
                    
                    # Convert DataFrame to JSON
                    sheet_data = json.loads(df.to_json(orient="records", date_format="iso"))
                    
                    # Add to result
                    if include_sheet_names:
                        result[sheet_name] = sheet_data
                    else:
                        # If not including sheet names, merge all data
                        if not result:
                            result = sheet_data
                        else:
                            result.extend(sheet_data)
            
            return result
        
        except Exception as e:
            # Re-raise with more informative message
            raise Exception(f"Error converting Excel to JSON: {str(e)}")
    
    @staticmethod
    def get_sheet_names(file_content: bytes) -> List[str]:
        """
        Get all sheet names from an Excel file.
        
        Args:
            file_content: Binary content of the Excel file
            
        Returns:
            List of sheet names
        """
        try:
            # Create a BytesIO object from the file content
            excel_file = io.BytesIO(file_content)
            
            # For compatibility, try different engines
            engines = ['xlrd', 'openpyxl']
            
            for engine in engines:
                try:
                    excel_file.seek(0)  # Reset file pointer
                    excel = pd.ExcelFile(excel_file, engine=engine)
                    return excel.sheet_names
                except Exception as e:
                    continue
            
            raise Exception("Could not read Excel file with any available engine")
            
        except Exception as e:
            # Re-raise with more informative message
            raise Exception(f"Error reading Excel sheet names: {str(e)}")
