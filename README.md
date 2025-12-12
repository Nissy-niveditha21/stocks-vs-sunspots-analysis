
---


# MAANG Stocks vs Sunspot Activity Dashboard

A Time-Series Correlation Study Using Stock Market Data and Solar Activity Cycles

This project analyzes whether long-term solar activity cycles (measured using the Monthly Mean Total Sunspot Number) show any visible relationship with the performance of MAANG companies’ stock prices. Daily MAANG stock data is aggregated into monthly values and merged with monthly sunspot activity data (1749–2018). The interactive Streamlit dashboard displays trends, overlays, and merged datasets, enabling exploratory analysis.

---

## 1. Features

* Streamlit-based interactive dashboard
* Monthly aggregation of daily MAANG stock prices
* Cleaned and standardized sunspot data
* Data merge using a common monthly date index
* Visualizations for:

  * Monthly Stock Price Trend
  * Monthly Sunspot Activity Trend
  * Combined Overlay (Stock vs Sunspots)
* Fully modular Python code structure suitable for production-level reuse
* Ready for AI for Bharat Week-3 submission with `.kiro` included

---

## 2. Project Structure

```
/project-root
│
├── data/
│   ├── stock_monthly.csv
│   └── sunspots_monthly.csv
│
├── src/
│   ├── data_loader.py
│   |── transform.py
|
│── dashboard.py
│
├── notebooks/
│   └── explore.ipynb
│
├── .kiro/
│
├── requirements.txt
└── README.md
```

---

## 3. Data Sources

### MAANG Stock Prices

* Source: Kaggle
* Daily prices for MAANG companies (Meta, Apple, Amazon, Netflix, Google)
* Converted to monthly using resampling

### Sunspot Activity

* Dataset: Monthly Mean Total Sunspot Number (1749–2018)
* Source: Kaggle or SIDC Sunspot Index
* Column standardized to `SunspotNumber`

---

## 4. Data Processing Pipeline

1. Load daily stock data → convert Date column to datetime
2. Resample to monthly mean using Pandas
3. Load sunspot dataset → normalize Month/Date column
4. Rename sunspot column to `SunspotNumber`
5. Convert both datasets to a common monthly timestamp
6. Merge on `Date` (inner join)

---

## 5. Installation

```
pip install -r requirements.txt
```

Contents of `requirements.txt`:

```
pandas
numpy
panel
bokeh
holoviews
hvplot
pyviz-comms
```

---

## 6. Running the Dashboard

From project root:

```
 dashboard.py
```
<img width="1920" height="1020" alt="Screenshot 2025-12-12 210002" src="https://github.com/user-attachments/assets/0a79e5cf-2a09-4c5e-9ac8-aeca32357621" />

<img width="1920" height="1020" alt="Screenshot 2025-12-12 210038" src="https://github.com/user-attachments/assets/baa79566-dd64-4f54-81ac-99a3feaa382d" />


The dashboard will open in your web browser at:

```
http://127.0.0.1:5006/dashboard
```

---

## 7. Code Overview

### data_loader.py

Handles CSV loading and datetime parsing.

### transform.py

* Converts daily → monthly stock data
* Cleans sunspot dataset
* Merges two datasets

### dashboard.py

* Loads data
* Runs transformations
* Renders visualizations using Plotly
* Displays merged preview + charts

---

## 8. Insights & Interpretation

* Sunspot cycles follow ~11-year oscillations.
* MAANG stock prices generally show long-term upward trends.
* Visual overlays allow exploration of whether major solar maxima align with changes in market volatility.
* This project does not claim causation—only exploratory pattern analysis.

---



## 9. How Kiro Accelerated Development

* Automated generation of project scaffolding
* Rapid creation of data loader and transformation scripts
* Auto-generated visualization layout in Streamlit
* Faster debugging and environment setup
* Significant reduction in time to design integration logic between unrelated datasets

---

## 10. License

This project is open-source and available under the MIT License.

---



AI for Bharat – Week 3 Submission

---




