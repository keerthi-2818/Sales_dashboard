import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import plotly.graph_objects as go
import plotly.express as px

def load_and_clean_data(uploaded_file):
    """Load and clean data from CSV or Excel file"""
    try:
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith('.xlsx'):
            df = pd.read_excel(uploaded_file)
        else:
            return None, "Unsupported file format. Please upload CSV or Excel file."
        
        # Clean data
        df['Order_Date'] = pd.to_datetime(df['Order_Date'], errors='coerce')
        
        # Handle missing values
        df = df.dropna(subset=['Order_Date', 'Sales', 'Revenue'])
        df['Quantity'] = df['Quantity'].fillna(0)
        df['Profit'] = df['Profit'].fillna(0)
        df['Customer_Name'] = df['Customer_Name'].fillna('Unknown')
        df['Region'] = df['Region'].fillna('Unknown')
        df['State'] = df['State'].fillna('Unknown')
        df['Product_Name'] = df['Product_Name'].fillna('Unknown')
        df['Category'] = df['Category'].fillna('Unknown')
        
        return df, "Data loaded successfully!"
    except Exception as e:
        return None, f"Error loading data: {str(e)}"

def calculate_kpis(df):
    """Calculate key performance indicators"""
    kpis = {
        'total_sales': df['Sales'].sum(),
        'total_revenue': df['Revenue'].sum(),
        'total_orders': len(df),
        'avg_order_value': df['Revenue'].sum() / len(df) if len(df) > 0 else 0,
        'total_profit': df['Profit'].sum() if 'Profit' in df.columns else 0,
    }
    
    # Monthly growth rate (last 30 days vs previous 30 days)
    df_sorted = df.sort_values('Order_Date')
    if len(df_sorted) > 1:
        max_date = df_sorted['Order_Date'].max()
        current_period_start = max_date - timedelta(days=30)
        previous_period_start = current_period_start - timedelta(days=30)

        current_month = df_sorted[df_sorted['Order_Date'] > current_period_start]['Revenue'].sum()
        previous_month = df_sorted[
            (df_sorted['Order_Date'] > previous_period_start) &
            (df_sorted['Order_Date'] <= current_period_start)
        ]['Revenue'].sum()

        if previous_month > 0:
            kpis['growth_rate'] = ((current_month - previous_month) / previous_month) * 100
        else:
            kpis['growth_rate'] = 0
    else:
        kpis['growth_rate'] = 0
    
    # Best performing product
    if 'Product_Name' in df.columns:
        best_product = df.groupby('Product_Name')['Revenue'].sum().idxmax()
        kpis['best_product'] = best_product
    else:
        kpis['best_product'] = 'N/A'
    
    return kpis

def get_monthly_sales_trend(df):
    """Generate monthly sales trend chart"""
    df['YearMonth'] = df['Order_Date'].dt.to_period('M')
    monthly_data = df.groupby('YearMonth').agg({
        'Sales': 'sum',
        'Revenue': 'sum'
    }).reset_index()
    monthly_data['YearMonth'] = monthly_data['YearMonth'].astype(str)
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=monthly_data['YearMonth'],
        y=monthly_data['Sales'],
        mode='lines+markers',
        name='Sales',
        line=dict(color='#1f77b4', width=3),
        marker=dict(size=8)
    ))
    fig.add_trace(go.Scatter(
        x=monthly_data['YearMonth'],
        y=monthly_data['Revenue'],
        mode='lines+markers',
        name='Revenue',
        line=dict(color='#ff7f0e', width=3),
        marker=dict(size=8)
    ))
    
    fig.update_layout(
        title='Monthly Sales & Revenue Trend',
        xaxis_title='Month',
        yaxis_title='Amount ($)',
        hovermode='x unified',
        template='plotly_white',
        height=400
    )
    return fig

def get_daily_sales_trend(df):
    """Generate daily sales trend chart"""
    daily_data = df.groupby(df['Order_Date'].dt.date).agg({
        'Sales': 'sum',
        'Quantity': 'sum'
    }).reset_index()
    daily_data.columns = ['Date', 'Sales', 'Quantity']
    
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=daily_data['Date'],
        y=daily_data['Sales'],
        name='Daily Sales',
        marker=dict(color='#2ca02c')
    ))
    
    fig.update_layout(
        title='Daily Sales Trend',
        xaxis_title='Date',
        yaxis_title='Sales Amount ($)',
        hovermode='x',
        template='plotly_white',
        height=400
    )
    return fig

def get_top_products_by_revenue(df, n=10):
    """Get top N products by revenue"""
    top_products = df.groupby('Product_Name')['Revenue'].sum().nlargest(n).reset_index()
    
    fig = px.bar(
        top_products,
        x='Revenue',
        y='Product_Name',
        orientation='h',
        title=f'Top {n} Products by Revenue',
        labels={'Revenue': 'Revenue ($)', 'Product_Name': 'Product'},
        color='Revenue',
        color_continuous_scale='Viridis'
    )
    fig.update_layout(height=400, template='plotly_white')
    return fig

def get_top_products_by_quantity(df, n=10):
    """Get top N products by quantity sold"""
    top_products = df.groupby('Product_Name')['Quantity'].sum().nlargest(n).reset_index()
    
    fig = px.bar(
        top_products,
        x='Quantity',
        y='Product_Name',
        orientation='h',
        title=f'Top {n} Products by Quantity Sold',
        labels={'Quantity': 'Quantity', 'Product_Name': 'Product'},
        color='Quantity',
        color_continuous_scale='Blues'
    )
    fig.update_layout(height=400, template='plotly_white')
    return fig

def get_category_performance(df):
    """Get product category performance"""
    category_data = df.groupby('Category').agg({
        'Revenue': 'sum',
        'Quantity': 'sum',
        'Sales': 'sum'
    }).reset_index().sort_values('Revenue', ascending=False)
    
    fig = px.bar(
        category_data,
        x='Category',
        y='Revenue',
        title='Product Category Performance by Revenue',
        labels={'Revenue': 'Revenue ($)', 'Category': 'Category'},
        color='Revenue',
        color_continuous_scale='Plasma'
    )
    fig.update_layout(height=400, template='plotly_white')
    return fig

def get_top_customers(df, n=10):
    """Get top N customers by revenue"""
    top_customers = df.groupby('Customer_Name')['Revenue'].sum().nlargest(n).reset_index()
    
    fig = px.bar(
        top_customers,
        x='Revenue',
        y='Customer_Name',
        orientation='h',
        title=f'Top {n} Customers by Revenue',
        labels={'Revenue': 'Revenue ($)', 'Customer_Name': 'Customer'},
        color='Revenue',
        color_continuous_scale='Greens'
    )
    fig.update_layout(height=400, template='plotly_white')
    return fig

def get_customer_purchase_frequency(df):
    """Get customer purchase frequency distribution"""
    customer_freq = df.groupby('Customer_Name').size().reset_index(name='Purchase_Count')
    
    fig = px.histogram(
        customer_freq,
        x='Purchase_Count',
        nbins=20,
        title='Customer Purchase Frequency Distribution',
        labels={'Purchase_Count': 'Number of Purchases', 'count': 'Number of Customers'},
        color_discrete_sequence=['#636EFA']
    )
    fig.update_layout(height=400, template='plotly_white')
    return fig

def get_sales_by_region(df):
    """Get sales by region"""
    region_data = df.groupby('Region').agg({
        'Revenue': 'sum',
        'Sales': 'sum',
        'Quantity': 'sum'
    }).reset_index().sort_values('Revenue', ascending=False)
    
    fig = px.pie(
        region_data,
        values='Revenue',
        names='Region',
        title='Revenue Distribution by Region',
        hole=0.4
    )
    fig.update_layout(height=400, template='plotly_white')
    return fig

def get_sales_by_state(df):
    """Get sales by state"""
    state_data = df.groupby('State').agg({
        'Revenue': 'sum',
        'Sales': 'sum'
    }).reset_index().sort_values('Revenue', ascending=False).head(15)
    
    fig = px.bar(
        state_data,
        x='State',
        y='Revenue',
        title='Top 15 States by Revenue',
        labels={'Revenue': 'Revenue ($)', 'State': 'State'},
        color='Revenue',
        color_continuous_scale='RdYlBu_r'
    )
    fig.update_layout(height=400, template='plotly_white', xaxis_tickangle=-45)
    return fig

def get_customer_segmentation(df):
    """Get customer segmentation by spending"""
    customer_spending = df.groupby('Customer_Name')['Revenue'].sum().reset_index()
    
    # Create spending segments
    q1, q2, q3 = customer_spending['Revenue'].quantile([0.33, 0.67, 1.0])
    
    def segment(value):
        if value <= q1:
            return 'Low Value'
        elif value <= q2:
            return 'Medium Value'
        else:
            return 'High Value'
    
    customer_spending['Segment'] = customer_spending['Revenue'].apply(segment)
    segment_counts = customer_spending['Segment'].value_counts().reset_index()
    segment_counts.columns = ['Segment', 'Count']
    
    fig = px.pie(
        segment_counts,
        values='Count',
        names='Segment',
        title='Customer Segmentation by Spending',
        color_discrete_map={'Low Value': '#FFA07A', 'Medium Value': '#87CEEB', 'High Value': '#90EE90'}
    )
    fig.update_layout(height=400, template='plotly_white')
    return fig

def apply_filters(df, date_range, categories, products, regions, customers):
    """Apply multiple filters to dataframe"""
    filtered_df = df.copy()
    
    # Date range filter
    if date_range:
        filtered_df = filtered_df[
            (filtered_df['Order_Date'] >= date_range[0]) &
            (filtered_df['Order_Date'] <= date_range[1])
        ]
    
    # Category filter
    if categories:
        filtered_df = filtered_df[filtered_df['Category'].isin(categories)]
    
    # Product filter
    if products:
        filtered_df = filtered_df[filtered_df['Product_Name'].isin(products)]
    
    # Region filter
    if regions:
        filtered_df = filtered_df[filtered_df['Region'].isin(regions)]
    
    # Customer filter
    if customers:
        filtered_df = filtered_df[filtered_df['Customer_Name'].isin(customers)]
    
    return filtered_df

def export_to_csv(df, filename='filtered_data.csv'):
    """Export dataframe to CSV"""
    return df.to_csv(index=False)

def generate_sample_data(rows=500):
    """Generate sample dataset for testing"""
    np.random.seed(42)
    
    products = ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Headphones', 
                'Webcam', 'USB Cable', 'HDMI Cable', 'Desk Lamp', 'Phone Stand']
    categories = ['Electronics', 'Accessories', 'Peripherals']
    regions = ['North', 'South', 'East', 'West', 'Central']
    states = ['CA', 'TX', 'NY', 'FL', 'PA', 'IL', 'OH', 'GA', 'NC', 'MI',
              'NJ', 'VA', 'WA', 'AZ', 'MA']
    customers = [f'Customer_{i}' for i in range(1, 101)]
    
    data = {
        'Order_ID': range(1001, 1001 + rows),
        'Order_Date': [datetime.now() - timedelta(days=int(x)) for x in np.random.randint(0, 365, rows)],
        'Customer_Name': np.random.choice(customers, rows),
        'Region': np.random.choice(regions, rows),
        'State': np.random.choice(states, rows),
        'Product_Name': np.random.choice(products, rows),
        'Category': np.random.choice(categories, rows),
        'Quantity': np.random.randint(1, 10, rows),
        'Sales': np.random.uniform(50, 2000, rows),
        'Revenue': np.random.uniform(100, 5000, rows),
        'Profit': np.random.uniform(20, 2000, rows)
    }
    
    df = pd.DataFrame(data)
    df = df.sort_values('Order_Date')
    return df
