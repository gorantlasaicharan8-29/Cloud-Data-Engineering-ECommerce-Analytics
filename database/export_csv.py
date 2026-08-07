import os
import pandas as pd
from db_connection import get_connection

# Create exports folder if it doesn't exist
os.makedirs("exports", exist_ok=True)

def export_table(table_name):
    conn = get_connection()

    query = f"SELECT * FROM {table_name};"

    df = pd.read_sql(query, conn)

    output_file = f"exports/{table_name}.csv"

    df.to_csv(output_file, index=False)

    conn.close()

    print(f"✅ {table_name} exported to {output_file}")

if __name__ == "__main__":
    export_table("customers")
    export_table("products")
    export_table("orders")

    print("\n🎉 All tables exported successfully!")