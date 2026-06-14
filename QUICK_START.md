# ⚡ Quick Start Guide - Sales Dashboard

## 🚀 Get Started in 5 Minutes

### Step 1: Install Dependencies (2 minutes)
```powershell
cd "f:\internship\sales dashboard"
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### Step 2: Run the Dashboard (1 minute)
```powershell
streamlit run app.py
```

### Step 3: Load Sample Data (30 seconds)
1. Browser opens automatically at `http://localhost:8501`
2. Click **"📊 Load Sample Data"** button in the sidebar
3. Dashboard populates with 500 sample records

### Step 4: Explore Features (1 minute)
- ✅ View KPI Cards at the top
- ✅ Try filters on the left sidebar
- ✅ Click charts to interact with them
- ✅ Download filtered data as CSV

---

## 📂 File Structure
```
sales_dashboard/
├── app.py              ← Main application (run this!)
├── utils.py            ← Analysis functions
├── requirements.txt    ← Dependencies
├── README.md          ← Full documentation
├── data/
│   └── sample_data.csv ← Test dataset
└── assets/            ← Images folder
```

---

## 📊 Dashboard Sections

| Section | What It Shows |
|---------|---------------|
| **KPI Cards** | 6 key metrics at the top |
| **Sales Analysis** | Monthly & daily trends |
| **Product Analysis** | Top products & categories |
| **Customer Analysis** | Top customers & segments |
| **Regional Analysis** | Sales by region & state |
| **Data View** | Raw data table (optional) |

---

## 🎛️ Using Filters

1. **Date Range**: Select start and end dates
2. **Categories**: Choose product categories
3. **Products**: Select specific products
4. **Regions**: Filter by region
5. **Customers**: Choose customers

All filters work together! Charts update in real-time.

---

## 📁 Upload Your Own Data

### CSV Format:
```csv
Order_ID,Order_Date,Customer_Name,Region,State,Product_Name,Category,Quantity,Sales,Revenue,Profit
1001,2025-02-15,Customer_1,North,CA,Laptop,Electronics,1,1200.50,1450.75,550.25
```

### Excel Format:
- Use `.xlsx` files
- Same column names as CSV
- Data starts from row 1

---

## 💾 Export Data

Click **"📥 Download Filtered Data (CSV)"** to export:
- Applied filters are reflected in export
- Filename includes timestamp
- Opens in Excel or Google Sheets

---

## 🛠️ Common Commands

| Task | Command |
|------|---------|
| Activate venv | `.\venv\Scripts\Activate.ps1` |
| Install packages | `pip install -r requirements.txt` |
| Run dashboard | `streamlit run app.py` |
| Stop server | `Ctrl+C` |
| Different port | `streamlit run app.py --server.port 8502` |

---

## ❓ Troubleshooting

| Problem | Solution |
|---------|----------|
| Module not found | Run `pip install -r requirements.txt` |
| Port in use | Use `--server.port 8502` |
| Data not loading | Check CSV/Excel format matches columns |
| Charts not showing | Refresh browser or clear cache |

---

## 📊 What's Included

✅ **6 KPI Cards** - Sales, Revenue, Orders, AOV, Profit, Best Product  
✅ **10+ Charts** - Trends, comparisons, distributions  
✅ **Dynamic Filters** - 5 different filter options  
✅ **Data Export** - CSV download with filters  
✅ **Sample Data** - 500 test records included  
✅ **Professional UI** - Modern dashboard design  

---

## 🎯 Next Steps

1. Load sample data and explore
2. Upload your own CSV/Excel file
3. Apply filters and analyze trends
4. Export insights as CSV
5. Customize for your business needs

---

**Questions?** Check the main README.md for detailed documentation!

**Happy analyzing!** 📊📈
