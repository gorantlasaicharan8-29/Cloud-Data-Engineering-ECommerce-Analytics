"""
E-Commerce Cloud Data Engineering Pipeline
Entry point: runs the full ETL pipeline end-to-end.
"""

import subprocess
import sys

steps = [
    ("Database Connection Test", "database/db_connection.py"),
    ("Generate Fake Customers",  "database/generate_fake_data.py"),
    ("Generate Orders",          "database/generate_orders.py"),
    ("Export CSV Files",         "database/export_csv.py"),
]

for name, script in steps:
    print(f"\n{'='*50}")
    print(f"▶ Running: {name}")
    print('='*50)
    result = subprocess.run([sys.executable, script], capture_output=False)
    if result.returncode != 0:
        print(f"❌ Failed at: {name}")
        sys.exit(1)

print("\n✅ Full ETL Pipeline Completed Successfully!")
