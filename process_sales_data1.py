import pandas as pd

# Use the correct file path
file_path = '/Users/emekaslaptop/Desktop/Sales Data.csv'  # Update this path

# Read the CSV file
sales_data = pd.read_csv(file_path)

# Display the contents of the CSV file
print("Sales Data:")
print(sales_data)


if 'Quantity' in sales_data.columns and 'Unit Price' in sales_data.columns:
    sales_data['Total Sales'] = sales_data['Quantity'] * sales_data['Unit Price']
else:
    print("The CSV file does not contain 'Quantity' and 'Unit Price' columns.")

# Write the processed data to a new CSV file
output_file_path = '/Users/emekaslaptop/Desktop/Processed_Sales_Data.csv'  
sales_data.to_csv(output_file_path, index=False)

print(f"Processed data has been saved to {output_file_path}")
