"""Run the complete e-commerce data pipeline in dependency order."""

import subprocess
import sys

STEPS = [
    ("Database connection test", "database/db_connection.py"),
    ("Generate customers", "database/generate_customers.py"),
    ("Generate products", "database/generate_fake_data.py"),
    ("Generate orders", "database/generate_orders.py"),
    ("Export CSV files", "database/export_csv.py"),
]


def main():
    for label, script in STEPS:
        print(f"\n{'=' * 60}\nRunning: {label}\n{'=' * 60}")
        result = subprocess.run([sys.executable, script], check=False)
        if result.returncode != 0:
            print(f"Pipeline stopped: {label} failed with exit code {result.returncode}.")
            return result.returncode

    print("\nPipeline completed successfully.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
