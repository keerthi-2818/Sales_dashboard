import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import plotly.graph_objects as go
import plotly.express as px
from utils import (
    load_and_clean_data,
    calculate_kpis,
    get_monthly_sales_trend,
    get_daily_sales_trend,
    get_top_products_by_revenue,
    get_top_products_by_quantity,
    get_category_performance,
    get_top_customers,
    get_customer_purchase_frequency,
    get_sales_by_region,
    get_sales_by_state,
    get_customer_segmentation,
    apply_filters,
    export_to_csv,
    generate_sample_data
)

# Page configuration
st.set_page_config(
    page_title="Sales & Revenue Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .metric-card {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        text-align: center;
    }
    .metric-value {
        font-size: 32px;
        font-weight: bold;
        color: #1f77b4;
        margin-top: 10px;
    }
    .metric-label {
        font-size: 14px;
        color: #666;
        margin-top: 5px;
    }
    .header-main {
        text-align: center;
        padding: 20px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'df' not in st.session_state:
    st.session_state.df = None
if 'dark_mode' not in st.session_state:
    st.session_state.dark_mode = False

# Sidebar
with st.sidebar:
    st.image("https://via.placeholder.com/250x100?text=Sales+Dashboard", use_column_width=True)
    st.markdown("---")
    
    # Dark Mode Toggle
    st.session_state.dark_mode = st.toggle("🌙 Dark Mode", value=st.session_state.dark_mode)
    
    st.markdown("---")
    st.subheader("📂 Data Management")
    
    # File upload section
    uploaded_file = st.file_uploader(
        "Upload CSV or Excel file",
        type=['csv', 'xlsx'],
        key='file_uploader'
    )
    
    if uploaded_file is not None:
        with st.spinner("Loading data..."):
            st.session_state.df, message = load_and_clean_data(uploaded_file)
            st.success(message)
    
    # Use sample data button
    if st.button("📊 Load Sample Data", use_container_width=True):
        with st.spinner("Generating sample data..."):
            st.session_state.df = generate_sample_data(500)
            st.success("Sample data loaded successfully!")
    
    st.markdown("---")
    st.subheader("🎯 Filters")
    
    # Filters only show if data is loaded
    if st.session_state.df is not None:
        df = st.session_state.df
        
        # Date range filter
        date_range = st.date_input(
            "Select Date Range",
            value=(df['Order_Date'].min().date(), df['Order_Date'].max().date()),
            key='date_range'
        )
        
        # Category filter
        categories = st.multiselect(
            "Product Categories",
            options=df['Category'].unique(),
            default=df['Category'].unique().tolist(),
            key='categories'
        )
        
        # Product filter
        products = st.multiselect(
            "Product Names",
            options=df['Product_Name'].unique(),
            default=df['Product_Name'].unique().tolist(),
            key='products'
        )
        
        # Region filter
        regions = st.multiselect(
            "Regions",
            options=df['Region'].unique(),
            default=df['Region'].unique().tolist(),
            key='regions'
        )
        
        # Customer filter
        customers = st.multiselect(
            "Customers",
            options=sorted(df['Customer_Name'].unique()),
            key='customers'
        )
        
        # Apply filters
        filtered_df = apply_filters(
            df,
            (pd.to_datetime(date_range[0]), pd.to_datetime(date_range[1])),
            categories,
            products,
            regions,
            customers
        )
        
        # Export section
        st.markdown("---")
        st.subheader("📥 Export Data")
        
        csv_data = export_to_csv(filtered_df)
        st.download_button(
            label="📥 Download Filtered Data (CSV)",
            data=csv_data,
            file_name=f"filtered_sales_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
            mime="text/csv",
            use_container_width=True
        )
        
        # Display data summary
        st.markdown("---")
        st.subheader("📈 Data Summary")
        st.metric("Filtered Records", len(filtered_df))
        st.metric("Date Range", f"{date_range[0]} to {date_range[1]}")

# Main content area
if st.session_state.df is None:
    # Welcome screen
    st.markdown("""
        <div class="header-main">
            <h1>📊 Sales & Revenue Analysis Dashboard</h1>
            <p>Upload your data or load sample data to get started</p>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("### 📁 Upload Data")
        st.markdown("- CSV files")
        st.markdown("- Excel files (.xlsx)")
    
    with col2:
        st.markdown("### 📊 Features")
        st.markdown("- KPI tracking")
        st.markdown("- Interactive charts")
        st.markdown("- Advanced filters")
    
    with col3:
        st.markdown("### 💾 Export Options")
        st.markdown("- CSV export")
        st.markdown("- PDF reports")
    
    st.info("👈 Use the sidebar to upload your data or load sample data to begin!")

else:
    # Dashboard content
    st.markdown("""
        <div class="header-main">
            <h1>📊 Sales & Revenue Analysis Dashboard</h1>
        </div>
    """, unsafe_allow_html=True)
    
    # Apply filters
    df = st.session_state.df
    
    # Get sidebar filter values from session state
    date_range = st.session_state.get('date_range', (df['Order_Date'].min().date(), df['Order_Date'].max().date()))
    categories = st.session_state.get('categories', df['Category'].unique().tolist())
    products = st.session_state.get('products', df['Product_Name'].unique().tolist())
    regions = st.session_state.get('regions', df['Region'].unique().tolist())
    customers = st.session_state.get('customers', [])
    
    filtered_df = apply_filters(
        df,
        (pd.to_datetime(date_range[0]), pd.to_datetime(date_range[1])),
        categories,
        products,
        regions,
        customers
    )
    
    # Calculate KPIs
    kpis = calculate_kpis(filtered_df)
    
    # KPI Cards
    st.subheader("🎯 Key Performance Indicators")
    
    kpi_col1, kpi_col2, kpi_col3, kpi_col4, kpi_col5, kpi_col6 = st.columns(6)
    
    with kpi_col1:
        st.metric(
            "💰 Total Sales",
            f"${kpis['total_sales']:,.2f}",
            delta=f"{kpis['growth_rate']:.1f}%" if kpis['growth_rate'] else None
        )
    
    with kpi_col2:
        st.metric(
            "💵 Total Revenue",
            f"${kpis['total_revenue']:,.2f}"
        )
    
    with kpi_col3:
        st.metric(
            "📦 Total Orders",
            f"{kpis['total_orders']:,}"
        )
    
    with kpi_col4:
        st.metric(
            "📊 Avg Order Value",
            f"${kpis['avg_order_value']:,.2f}"
        )
    
    with kpi_col5:
        st.metric(
            "📈 Total Profit",
            f"${kpis['total_profit']:,.2f}"
        )
    
    with kpi_col6:
        st.metric(
            "⭐ Best Product",
            kpis['best_product']
        )
    
    st.markdown("---")
    
    # Sales Analysis Section
    st.subheader("📈 Sales Analysis")
    
    sales_col1, sales_col2 = st.columns(2)
    
    with sales_col1:
        monthly_fig = get_monthly_sales_trend(filtered_df)
        st.plotly_chart(monthly_fig, use_container_width=True)
    
    with sales_col2:
        daily_fig = get_daily_sales_trend(filtered_df)
        st.plotly_chart(daily_fig, use_container_width=True)
    
    st.markdown("---")
    
    # Product Analysis Section
    st.subheader("📦 Product Analysis")
    
    product_col1, product_col2 = st.columns(2)
    
    with product_col1:
        top_revenue_fig = get_top_products_by_revenue(filtered_df, n=10)
        st.plotly_chart(top_revenue_fig, use_container_width=True)
    
    with product_col2:
        top_qty_fig = get_top_products_by_quantity(filtered_df, n=10)
        st.plotly_chart(top_qty_fig, use_container_width=True)
    
    # Category Performance
    category_fig = get_category_performance(filtered_df)
    st.plotly_chart(category_fig, use_container_width=True)
    
    st.markdown("---")
    
    # Customer Analysis Section
    st.subheader("👥 Customer Analysis")
    
    customer_col1, customer_col2 = st.columns(2)
    
    with customer_col1:
        top_cust_fig = get_top_customers(filtered_df, n=10)
        st.plotly_chart(top_cust_fig, use_container_width=True)
    
    with customer_col2:
        freq_fig = get_customer_purchase_frequency(filtered_df)
        st.plotly_chart(freq_fig, use_container_width=True)
    
    # Customer Segmentation
    segment_fig = get_customer_segmentation(filtered_df)
    st.plotly_chart(segment_fig, use_container_width=True)
    
    st.markdown("---")
    
    # Regional Analysis Section
    st.subheader("🗺️ Regional Analysis")
    
    region_col1, region_col2 = st.columns(2)
    
    with region_col1:
        region_fig = get_sales_by_region(filtered_df)
        st.plotly_chart(region_fig, use_container_width=True)
    
    with region_col2:
        state_fig = get_sales_by_state(filtered_df)
        st.plotly_chart(state_fig, use_container_width=True)
    
    st.markdown("---")
    
    # Data Table Section
    st.subheader("📋 Detailed Data View")
    
    if st.checkbox("Show Raw Data", value=False):
        st.dataframe(
            filtered_df.sort_values('Order_Date', ascending=False),
            use_container_width=True,
            height=400
        )
    
    # Statistics Summary
    st.subheader("📊 Statistical Summary")
    
    stats_col1, stats_col2, stats_col3 = st.columns(3)
    
    with stats_col1:
        st.write("### Sales Statistics")
        st.write(f"**Minimum Sale:** ${filtered_df['Sales'].min():,.2f}")
        st.write(f"**Maximum Sale:** ${filtered_df['Sales'].max():,.2f}")
        st.write(f"**Average Sale:** ${filtered_df['Sales'].mean():,.2f}")
        st.write(f"**Median Sale:** ${filtered_df['Sales'].median():,.2f}")
    
    with stats_col2:
        st.write("### Revenue Statistics")
        st.write(f"**Minimum Revenue:** ${filtered_df['Revenue'].min():,.2f}")
        st.write(f"**Maximum Revenue:** ${filtered_df['Revenue'].max():,.2f}")
        st.write(f"**Average Revenue:** ${filtered_df['Revenue'].mean():,.2f}")
        st.write(f"**Median Revenue:** ${filtered_df['Revenue'].median():,.2f}")
    
    with stats_col3:
        st.write("### Quantity Statistics")
        st.write(f"**Total Quantity:** {filtered_df['Quantity'].sum():,.0f}")
        st.write(f"**Average Quantity/Order:** {filtered_df['Quantity'].mean():,.2f}")
        st.write(f"**Max Quantity/Order:** {filtered_df['Quantity'].max():,.0f}")
        st.write(f"**Unique Customers:** {filtered_df['Customer_Name'].nunique()}")

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: #888; font-size: 12px; padding: 20px;'>
        <p>Sales & Revenue Analysis Dashboard | Built with Streamlit & Plotly</p>
        <p>© 2025 Sales Analytics Platform</p>
    </div>
""", unsafe_allow_html=True)
