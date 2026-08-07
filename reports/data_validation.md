# Data Validation Report

## Summary

| Table     | Row Count | Null Values | Duplicates | Status |
|-----------|-----------|-------------|------------|--------|
| customers | 1,001     | 0           | 0          | ✅ Pass |
| products  | 678       | 0           | 0          | ✅ Pass |
| orders    | 3,349     | 0           | 0          | ✅ Pass |

---

## Customers Table

- Total Records: 1,001
- Fields: customer_id, first_name, last_name, email, phone, city, country
- No null values found
- Email uniqueness: ✅ Verified
- Country distribution: India (majority), with international entries

---

## Products Table

- Total Records: 678
- Fields: product_id, product_name, category, brand, price, stock
- Categories: Electronics, Accessories
- Price range: ₹500 – ₹1,00,000
- Stock range: 10 – 500 units

---

## Orders Table

- Total Records: 3,349
- Fields: order_id, customer_id, product_id, quantity, total_amount, order_status
- Order Status Values: Pending, Processing, Shipped, Delivered, Cancelled
- Total Revenue: ₹508M
- Average Order Value: ₹4,945.23
- Highest Order: ₹98,500
- Lowest Order: ₹500
- All customer_id and product_id values reference valid records: ✅ Verified

---

## Conclusion

All three tables passed data validation checks. The dataset is clean, consistent, and ready for analytics and visualization.
