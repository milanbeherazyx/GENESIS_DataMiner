from pystatis import init_config, Table, clear_cache

# Initialize your GENESIS credentials if not already done
init_config(username="DE17OK2U7I", password="Rowdybaby@1997")



# Hardcoded table names
table_names = ["32111-0001", "32111-0002"]  # Add the table names you want to scrape

for table_name in table_names:
    # Create a Table object
    table = Table(name=table_name)

    # Get the data (this will also check the cache)
    table.get_data()

    # Define the Excel filename based on the table name
    excel_filename = f"{table_name}.xlsx"

    # Save the data to an Excel file using Pandas
    table.data.to_excel(excel_filename, index=False)

    # Clear the cache for this table
    clear_cache(table_name)
