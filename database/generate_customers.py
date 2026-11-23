"""Generate synthetic customer records for the e-commerce database."""

from faker import Faker

from database.insert_data import insert_customer

fake = Faker("en_IN")
TOTAL_CUSTOMERS = 1000


def main():
    print(f"Generating {TOTAL_CUSTOMERS} customers...")
    for index in range(TOTAL_CUSTOMERS):
        insert_customer(
            fake.first_name(),
            fake.last_name(),
            fake.unique.email(),
            fake.phone_number()[:20],
            fake.city()[:50],
            fake.country()[:50],
        )
        if (index + 1) % 100 == 0:
            print(f"Inserted {index + 1}/{TOTAL_CUSTOMERS} customers")
    print("Customer generation completed.")


if __name__ == "__main__":
    main()
