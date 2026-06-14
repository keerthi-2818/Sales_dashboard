# 📊 Sales & Revenue Analysis Dashboard

A professional, interactive **Sales & Revenue Analysis Dashboard** built with Python Streamlit. Perfect for data analytics internship projects, business intelligence analysis, and real-time sales monitoring.

## 🎯 Features

### 📈 Key Performance Indicators (KPIs)
- **Total Sales** - Aggregated sales amount
- **Total Revenue** - Complete revenue metrics
- **Total Orders** - Number of transactions
- **Average Order Value** - AOV calculation
- **Total Profit** - Profit tracking
- **Best Performing Product** - Top product identification

### 📊 Sales Analysis
- Monthly Sales & Revenue Trend (Line Chart)
- Daily Sales Trend (Bar Chart)
- Revenue distribution analysis
- Time-series visualizations

### 📦 Product Analysis
- Top 10 Products by Revenue
- Top 10 Products by Quantity Sold
- Product Category Performance
- Category-wise revenue distribution

### 👥 Customer Analysis
- Top 10 Customers by Revenue
- Customer Purchase Frequency Distribution
- Customer Segmentation (Low/Medium/High Value)
- Customer lifetime value metrics

### 🗺️ Regional Analysis
- Sales by Region (Pie Chart)
- Top 15 States by Revenue (Bar Chart)
- Revenue distribution by geography
- Regional performance comparison

### 🎛️ Interactive Features
- **Dynamic Filters:**
  - Date Range Selector
  - Product Category Filter
  - Product Name Filter
  - Region Filter
  - Customer Name Filter
  - Real-time dashboard updates

- **Export Options:**
  - Download filtered data as CSV
  - Data persistence and caching

- **UI Features:**
  - Dark Mode / Light Mode toggle
  - Responsive layout
  - Professional color schemes
  - Interactive Plotly charts
  - KPI cards with metrics

### 📋 Data Management
- Upload CSV files
- Upload Excel files (.xlsx)
- Automatic data cleaning
- Missing value handling
- Date parsing and validation
- Sample dataset generator

## 📋 Dataset Requirements

### Expected Columns:
```
Order_ID
Order_Date
Customer_Name
Region
State
Product_Name
Category
Quantity
Sales
Revenue
Profit
```

### Data Types:
- **Order_ID**: Integer (unique identifier)
- **Order_Date**: DateTime (YYYY-MM-DD format)
- **Customer_Name**: String
- **Region**: String (North, South, East, West, Central)
- **State**: String (2-letter state codes)
- **Product_Name**: String
- **Category**: String (Electronics, Accessories, Peripherals)
- **Quantity**: Integer
- **Sales**: Float (amount sold)
- **Revenue**: Float (total revenue)
- **Profit**: Float (profit amount)

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Git (optional)

### Installation Steps

1. **Clone or download the project:**
   ```bash
   cd "f:\internship\sales dashboard"
   ```

2. **Create a virtual environment (Recommended):**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   
   **Windows (PowerShell):**
   ```powershell
   .\venv\Scripts\Activate.ps1
   ```
   
   **Windows (Command Prompt):**
   ```bash
   venv\Scripts\activate.bat
   ```
   
   **macOS/Linux:**
   ```bash
   source venv/bin/activate
   ```

4. **Install required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## 🏃 Running the Dashboard

### Using Streamlit
```bash
streamlit run app.py
```

The dashboard will automatically open in your default browser at `http://localhost:8501`

### Using VS Code Terminal
1. Open the project folder in VS Code
2. Open Terminal: `Ctrl+` (backtick)
3. Ensure virtual environment is activated
4. Run: `streamlit run app.py`

## 📁 Project Structure

```
sales_dashboard/
│
├── app.py                 # Main Streamlit application
├── utils.py              # Utility functions for data processing & analysis
├── requirements.txt      # Python dependencies
├── README.md            # Project documentation
│
├── data/
│   └── sample_data.csv  # Sample dataset for testing
│
└── assets/
    └── (placeholder for future images/logos)
```

## 📦 Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| streamlit | 1.35.0 | Web framework |
| pandas | 2.1.3 | Data manipulation |
| plotly | 5.18.0 | Interactive charts |
| numpy | 1.26.2 | Numerical operations |
| openpyxl | 3.10.10 | Excel file support |
| kaleido | 0.2.1 | Image export |

## 🎨 Features in Detail

### Data Upload
- Click "Upload CSV or Excel file" in the sidebar
- Dashboard automatically cleans and validates data
- Handles missing values gracefully
- Parses dates automatically

### Sample Data
- Click "Load Sample Data" to generate test dataset
- 500 sample records with realistic sales data
- Perfect for testing dashboard functionality

### Filter System
All filters work dynamically:
- **Date Range**: Select start and end dates
- **Categories**: Multi-select product categories
- **Products**: Multi-select specific products
- **Regions**: Filter by geographic regions
- **Customers**: Filter by customer names

### Data Export
- Download filtered data as CSV
- Filename includes timestamp
- Compatible with Excel and other tools

### Visual Analytics
- **Line Charts**: Trend analysis
- **Bar Charts**: Ranking and comparison
- **Pie Charts**: Proportion analysis
- **Histograms**: Distribution analysis
- **Hover Information**: Detailed metrics on charts

## 🛠️ Customization

### Modify KPI Cards
Edit the KPI calculation section in `app.py`:
```python
with kpi_col1:
    st.metric(
        "💰 Total Sales",
        f"${kpis['total_sales']:,.2f}"
    )
```

### Add New Visualizations
Add new functions to `utils.py`:
```python
def my_new_chart(df):
    # Your chart code here
    return fig
```

Then call it in `app.py`:
```python
my_fig = my_new_chart(filtered_df)
st.plotly_chart(my_fig, use_container_width=True)
```

### Change Color Schemes
Modify the Plotly color themes in `utils.py`:
```python
color_continuous_scale='Viridis'  # Change to different colormap
```

Available scales: Viridis, Plasma, Blues, Greens, Reds, RdYlBu, etc.

## 📊 Sample Usage

1. **Load Sample Data**
   - Click "Load Sample Data" button
   - Dashboard populates with 500 sample records

2. **Explore the Data**
   - KPIs update automatically
   - Charts render in real-time
   - Scroll through different analysis sections

3. **Apply Filters**
   - Select date range
   - Choose specific products/categories
   - Filter by region or customer
   - Charts update instantly

4. **Export Results**
   - Click "Download Filtered Data (CSV)"
   - File downloads with timestamp

5. **View Details**
   - Toggle "Show Raw Data" to see full dataset
   - Review statistical summaries
   - Hover over charts for details

## 🐛 Troubleshooting

### Issue: "ModuleNotFoundError"
**Solution:** Ensure all dependencies are installed:
```bash
pip install -r requirements.txt
```

### Issue: "Port 8501 already in use"
**Solution:** Run on different port:
```bash
streamlit run app.py --server.port 8502
```

### Issue: Data not loading
**Solution:** 
- Verify CSV/Excel format matches expected columns
- Ensure dates are in YYYY-MM-DD format
- Check for special characters in headers

### Issue: Charts not displaying
**Solution:**
- Refresh the browser page
- Clear browser cache
- Ensure filtered data is not empty

## 💡 Tips & Best Practices

1. **Performance**: For large datasets (>100K rows), consider filtering before upload
2. **Date Format**: Always use YYYY-MM-DD format for dates
3. **Data Quality**: Clean data produces better insights
4. **Backups**: Keep original data files backed up
5. **Testing**: Use sample data to test before uploading real data

## 📈 Business Use Cases

- **Sales Performance Tracking**: Monitor monthly and daily trends
- **Product Analysis**: Identify top performers and opportunities
- **Customer Insights**: Segment and analyze customer behavior
- **Regional Performance**: Compare sales across regions
- **Profit Optimization**: Track profit trends and margins
- **Executive Reporting**: Generate quick insights for stakeholders

## 🔐 Data Privacy

- Data is processed locally on your machine
- No data is sent to external servers
- Files are not stored permanently after session ends
- Use only with authorized business data

## 📝 License

This project is provided as-is for educational and commercial purposes.

## 🤝 Support

For issues or questions:
1. Check the Troubleshooting section
2. Review sample data format
3. Verify Python and dependencies are properly installed
4. Ensure internet connection for live data features

## 🎓 Learning Outcomes

This dashboard demonstrates:
- ✅ Modern web dashboard development
- ✅ Data analysis and visualization
- ✅ Interactive filtering and user experience
- ✅ Professional UI/UX design
- ✅ Business intelligence concepts
- ✅ Python data science libraries

## 📚 Resources

- [Streamlit Documentation](https://docs.streamlit.io)
- [Plotly Documentation](https://plotly.com/python/)
- [Pandas Documentation](https://pandas.pydata.org/)
- [Python Best Practices](https://pep8.org/)

---

**Created for Data Analytics Internship Projects**

**Last Updated:** June 2025

**Version:** 1.0.0

Made with ❤️ for data enthusiasts and business analysts
