import streamlit as st
import pandas as pd
import plotly.express as px

# =====================================================
# PAGE CONFIGURATION
# =====================================================
st.set_page_config(
    page_title="E-Commerce Sales Analytics",
    page_icon="📊",
    layout="wide"
)

# =====================================================
# SIDEBAR
# =====================================================
st.sidebar.image("assets/logo.png", width=180)
st.sidebar.markdown("## E-Commerce Analytics")
st.sidebar.markdown("---")

st.sidebar.subheader("Navigation")
page = st.sidebar.radio("", ["📊 Dashboard", "📋 Data", "ℹ️ About"])
st.sidebar.markdown("---")

# =====================================================
# LOAD DATA
# =====================================================
customers = pd.read_csv("exports/customers.csv")
orders    = pd.read_csv("exports/orders.csv")
products  = pd.read_csv("exports/products.csv")
orders["order_date"] = pd.to_datetime(orders["order_date"])

# =====================================================
# SIDEBAR FILTERS (only on Dashboard)
# =====================================================
if page == "📊 Dashboard":
    st.sidebar.subheader("Filters")
    selected_status = st.sidebar.multiselect(
        "Order Status",
        options=orders["order_status"].unique(),
        default=orders["order_status"].unique()
    )
    selected_category = st.sidebar.multiselect(
        "Product Category",
        options=products["category"].unique(),
        default=products["category"].unique()
    )
    st.sidebar.markdown("---")

    # Filter data
    filtered_orders = orders[orders["order_status"].isin(selected_status)]
    filtered_orders = filtered_orders.merge(
        products[["product_id", "category", "product_name"]], on="product_id"
    )
    filtered_orders = filtered_orders[filtered_orders["category"].isin(selected_category)]

    st.sidebar.download_button(
        label="⬇ Download Filtered Orders",
        data=filtered_orders.to_csv(index=False),
        file_name="filtered_orders.csv",
        mime="text/csv"
    )

# =====================================================
# PAGE: DASHBOARD
# =====================================================
if page == "📊 Dashboard":

    st.title("📊 E-Commerce Sales Analytics Dashboard")
    st.markdown("#### End-to-End Cloud Data Engineering Project")
    st.markdown("---")

    # KPI Cards
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("👥 Total Customers", f"{customers['customer_id'].nunique():,}")
    col2.metric("📦 Total Orders",    f"{filtered_orders['order_id'].nunique():,}")
    col3.metric("🛍️ Total Products",  f"{products['product_id'].nunique():,}")
    col4.metric("💰 Total Revenue",   f"₹ {filtered_orders['total_amount'].sum():,.0f}")
    st.markdown("---")

    # Row 1
    left, right = st.columns(2)

    top_products = (
        filtered_orders.groupby("product_name")["quantity"]
        .sum().sort_values(ascending=False).head(10).reset_index()
    )
    fig1 = px.bar(top_products, x="quantity", y="product_name",
                  orientation="h", color="quantity",
                  title="🏆 Top 10 Selling Products")
    left.plotly_chart(fig1, use_container_width=True)

    status_df = filtered_orders["order_status"].value_counts().reset_index()
    status_df.columns = ["Status", "Count"]
    fig2 = px.pie(status_df, names="Status", values="Count",
                  hole=0.45, title="📦 Order Status Distribution")
    right.plotly_chart(fig2, use_container_width=True)

    # Revenue Trend
    st.markdown("---")
    revenue = (
        filtered_orders.groupby(filtered_orders["order_date"].dt.date)["total_amount"]
        .sum().reset_index()
    )
    revenue.columns = ["Date", "Revenue"]
    fig3 = px.line(revenue, x="Date", y="Revenue", markers=True, title="📈 Revenue Trend")
    st.plotly_chart(fig3, use_container_width=True)

    # Row 2
    left2, right2 = st.columns(2)

    sales = filtered_orders.groupby("category")["total_amount"].sum().reset_index()
    fig4 = px.bar(sales, x="category", y="total_amount",
                  color="total_amount", title="🛒 Sales by Category")
    left2.plotly_chart(fig4, use_container_width=True)

    country = customers.groupby("country")["customer_id"].count().reset_index()
    country.columns = ["Country", "Customers"]
    fig5 = px.bar(country, x="Country", y="Customers",
                  color="Customers", title="🌍 Customers by Country")
    right2.plotly_chart(fig5, use_container_width=True)

# =====================================================
# PAGE: DATA
# =====================================================
elif page == "📋 Data":

    st.title("📋 Raw Data Explorer")
    st.markdown("---")

    tab1, tab2, tab3 = st.tabs(["👥 Customers", "📦 Orders", "🛍️ Products"])

    with tab1:
        st.subheader(f"Customers — {len(customers):,} records")
        st.dataframe(customers, use_container_width=True)

    with tab2:
        st.subheader(f"Orders — {len(orders):,} records")
        st.dataframe(orders, use_container_width=True)

    with tab3:
        st.subheader(f"Products — {len(products):,} records")
        st.dataframe(products, use_container_width=True)

# =====================================================
# PAGE: ABOUT
# =====================================================
elif page == "ℹ️ About":

    st.title("ℹ️ About This Project")
    st.markdown("---")

    st.markdown("""
    ### 🛒 E-Commerce Sales Analytics Dashboard

    This is an **End-to-End Cloud Data Engineering** project that simulates a real-world
    e-commerce data pipeline.

    ---

    ### 🔄 Pipeline Stages

    | Stage | Tool |
    |---|---|
    | Data Generation | Python + Faker |
    | Database | Neon PostgreSQL |
    | SQL Analytics | psycopg2 + SQL |
    | CSV Export | Pandas |
    | Visualizations | Matplotlib |
    | BI Dashboard | Power BI + Streamlit |

    ---

    ### 📊 Dataset

    | Table | Records |
    |---|---|
    | Customers | 1,001 |
    | Products | 678 |
    | Orders | 3,349 |
    | Total Revenue | ₹508M |

    ---

    ### 🛠️ Technologies Used
    `Python` `SQL` `PostgreSQL` `Pandas` `Matplotlib` `Power BI` `Streamlit` `Git`

    ---
    """)

    st.info("Developed by **Lanka Bala Sowmith** & **Gorantla Sai Charan** | End-to-End Cloud Data Engineering Project | 2026")

# =====================================================
# FOOTER
# =====================================================
st.markdown("---")
st.markdown(
    "<center>Developed by <b>Lanka Bala Sowmith</b> & <b>Gorantla Sai Charan</b> | End-to-End Cloud Data Engineering Project | 2026</center>",
    unsafe_allow_html=True
)
