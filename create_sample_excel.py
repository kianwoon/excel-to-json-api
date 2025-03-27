import pandas as pd
import os

def create_sample_excel():
    """
    Create a sample Excel file with multiple sheets for testing the API.
    """
    # Create directory if it doesn't exist
    os.makedirs("test_files", exist_ok=True)
    
    # Create sample data for Sheet1 (Employees)
    employees_data = {
        "id": [1, 2, 3, 4, 5],
        "name": ["John Doe", "Jane Smith", "Bob Johnson", "Alice Williams", "Charlie Brown"],
        "department": ["Engineering", "Marketing", "HR", "Finance", "Engineering"],
        "salary": [85000, 75000, 65000, 90000, 80000],
        "hire_date": ["2020-01-15", "2019-05-20", "2021-03-10", "2018-11-01", "2020-08-15"]
    }
    
    # Create sample data for Sheet2 (Products)
    products_data = {
        "product_id": [101, 102, 103, 104, 105],
        "product_name": ["Laptop", "Smartphone", "Tablet", "Monitor", "Keyboard"],
        "category": ["Electronics", "Electronics", "Electronics", "Accessories", "Accessories"],
        "price": [1200.00, 800.00, 500.00, 300.00, 80.00],
        "stock": [50, 100, 75, 30, 120]
    }
    
    # Create sample data for Sheet3 (Sales)
    sales_data = {
        "sale_id": [1001, 1002, 1003, 1004, 1005, 1006],
        "product_id": [101, 103, 102, 105, 104, 101],
        "employee_id": [1, 3, 2, 5, 4, 1],
        "sale_date": ["2023-01-10", "2023-01-15", "2023-01-20", "2023-02-05", "2023-02-10", "2023-02-15"],
        "quantity": [1, 2, 1, 3, 1, 1],
        "total_amount": [1200.00, 1000.00, 800.00, 240.00, 300.00, 1200.00]
    }
    
    # Create DataFrames
    df_employees = pd.DataFrame(employees_data)
    df_products = pd.DataFrame(products_data)
    df_sales = pd.DataFrame(sales_data)
    
    # Create Excel writer
    excel_path = "test_files/sample.xlsx"
    with pd.ExcelWriter(excel_path, engine='openpyxl') as writer:
        df_employees.to_excel(writer, sheet_name='Employees', index=False)
        df_products.to_excel(writer, sheet_name='Products', index=False)
        df_sales.to_excel(writer, sheet_name='Sales', index=False)
    
    print(f"Sample Excel file created at: {excel_path}")
    print("The file contains 3 sheets: Employees, Products, and Sales")

if __name__ == "__main__":
    create_sample_excel()
