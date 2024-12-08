# Sales Management Analysis Portfolio

This project showcases my proficiency in leveraging **Power BI** and **SQL** for insightful sales management analysis. By utilizing data from the **AdventureWorks Database** (a Microsoft sample OLTP database), I focused on extracting meaningful insights to empower strategic decision-making for sales teams.

## 🔍 Project Overview
The primary objective was to analyze sales data to identify:
- Sales budget trends and fluctuations.
- Customer-specific sales patterns.
- Product-specific sales insights.

This portfolio demonstrates how I integrated **SQL Server** for data cleaning and transformation with **Power BI** to create dynamic dashboards, delivering actionable insights for stakeholders.

## 💼 Business Request & User Stories
### Business Request
Create an executive sales report for sales managers to monitor sales performance, track top-performing customers and products, and compare sales against budgets.

### User Stories
| #  | Role                | Request/Demand                                   | User Value                              | Acceptance Criteria                           |
|----|---------------------|-------------------------------------------------|-----------------------------------------|-----------------------------------------------|
| 1  | Sales Manager       | Dashboard overview of internet sales            | Follow top-performing customers/products | A Power BI dashboard updating daily          |
| 2  | Sales Representative | Detailed overview of internet sales per customer | Identify high-value customers and upsell opportunities | Power BI dashboard with customer-specific filtering |
| 3  | Sales Representative | Detailed overview of internet sales per product | Track top-selling products              | Power BI dashboard with product-specific filtering |
| 4  | Sales Manager       | Dashboard to monitor sales over time vs budget  | Compare actual sales against budgets    | Power BI dashboard with graphs and KPIs      |

## 🧹 Data Cleaning & Transformation (SQL)
To create the data model, the following tables were extracted and transformed using SQL:
- **DIM_Calendar**
- **DIM_Customers**
- **DIM_Products**
- **FACT_InternetSales**

Additionally, sales budget data in Excel format was connected to the Power BI data model to enable comprehensive analysis.

## 📊 Data Model
The data model integrated **FACT_Budget** with **FACT_InternetSales** and the dimension tables (**DIM_Calendar**, **DIM_Customers**, **DIM_Products**). This structure supported dynamic reporting and visualizations in Power BI.

## 📈 Sales Management Dashboard
The Power BI dashboard consists of:
1. **Main Overview Page:** Summarizes key sales KPIs and trends.
2. **Customer Analysis Page:** Provides insights into customer-specific sales patterns.
3. **Product Analysis Page:** Highlights product performance and trends.

### Features
- Interactive graphs and filters.
- KPIs comparing sales performance against budgets.
- Drill-down capabilities for detailed analysis.

## 🛠️ Tools Used
- **Power BI**: Data visualization and dashboard creation.
- **SQL Server**: Data cleaning and transformation.
- **Excel**: Supplementary data source for sales budgets.

## 🌟 Key Insights
- Identified budget trends, revealing fluctuations affecting sales performance.
- Unveiled customer behavior patterns, aiding targeted marketing strategies.
- Highlighted top-performing products, supporting inventory management and upselling.

## 📂 Project Portfolio
Visit my project portfolio for more details: [My Portfolio](https://balaji23balaji.wordpress.com/)

---

## 🚀 How to Use
1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/Sales-Management-Analysis.git
