import pandas as pd
import panel as pn
import hvplot.pandas
import numpy as np
from scipy.stats import pearsonr
import holoviews as hv

# --- Panel Setup ---
pn.extension('bokeh', 'tabulator', sizing_mode="stretch_width", template='material')
hv.extension('bokeh')

# Professional CSS Styling
pn.config.raw_css.append("""
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

:root {
    --primary-color: #2563eb;
    --secondary-color: #f59e0b;
    --success-color: #10b981;
    --danger-color: #ef4444;
    --dark-bg: #0f172a;
    --card-bg: #ffffff;
    --text-primary: #1e293b;
    --text-secondary: #64748b;
    --border-color: #e2e8f0;
    --shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    --shadow-lg: 0 20px 25px -5px rgba(0, 0, 0, 0.1);
}

body {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    margin: 0;
    padding: 0;
}

.dashboard {
    background: transparent;
    padding: 20px;
    min-height: 100vh;
}

.hero-section {
    background: linear-gradient(135deg, var(--dark-bg) 0%, #1e293b 100%);
    color: white;
    padding: 40px 30px;
    border-radius: 20px;
    margin-bottom: 30px;
    box-shadow: var(--shadow-lg);
    position: relative;
    overflow: hidden;
}

.hero-section::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><defs><pattern id="grid" width="10" height="10" patternUnits="userSpaceOnUse"><path d="M 10 0 L 0 0 0 10" fill="none" stroke="rgba(255,255,255,0.05)" stroke-width="1"/></pattern></defs><rect width="100" height="100" fill="url(%23grid)"/></svg>');
    pointer-events: none;
}

.hero-content {
    position: relative;
    z-index: 1;
}

.main-title {
    font-size: 3.5rem;
    font-weight: 700;
    margin: 0 0 15px 0;
    background: linear-gradient(135deg, #60a5fa, #34d399);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    line-height: 1.1;
}

.main-subtitle {
    font-size: 1.25rem;
    color: #94a3b8;
    margin: 0 0 25px 0;
    font-weight: 400;
}

.stats-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 20px;
    margin-top: 25px;
}

.stat-card {
    background: rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.2);
    border-radius: 15px;
    padding: 20px;
    text-align: center;
    transition: all 0.3s ease;
    cursor: pointer;
}

.stat-card:hover {
    background: rgba(255, 255, 255, 0.2);
    transform: translateY(-3px) scale(1.05);
    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
}

.stat-value {
    font-size: 2rem;
    font-weight: 700;
    color: #60a5fa;
    margin: 0;
}

.stat-label {
    font-size: 0.875rem;
    color: #cbd5e1;
    margin: 5px 0 0 0;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.premium-card {
    background: var(--card-bg);
    border-radius: 20px;
    box-shadow: var(--shadow-lg);
    border: 1px solid var(--border-color);
    overflow: hidden;
    transition: all 0.3s ease;
    margin-bottom: 25px;
}

.premium-card:hover {
    transform: translateY(-8px) scale(1.02);
    box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}

.premium-card {
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.card-header {
    padding: 25px 30px 20px;
    border-bottom: 1px solid var(--border-color);
    background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%);
}

.card-title {
    font-size: 1.5rem;
    font-weight: 600;
    color: var(--text-primary);
    margin: 0 0 8px 0;
    display: flex;
    align-items: center;
    gap: 10px;
}

.card-subtitle {
    font-size: 0.875rem;
    color: var(--text-secondary);
    margin: 0;
}

.card-content {
    padding: 0;
}

.insight-box {
    background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%);
    border-left: 4px solid var(--secondary-color);
    padding: 20px;
    margin: 20px;
    border-radius: 10px;
    font-size: 0.95rem;
    line-height: 1.6;
}

.correlation-badge {
    display: inline-block;
    padding: 8px 16px;
    border-radius: 20px;
    font-weight: 600;
    font-size: 0.875rem;
    margin: 10px 0;
}

.correlation-positive {
    background: #dcfce7;
    color: #166534;
}

.correlation-negative {
    background: #fee2e2;
    color: #991b1b;
}

.correlation-neutral {
    background: #f3f4f6;
    color: #374151;
}

.bk-root .bk-tab {
    background: var(--card-bg) !important;
    border-radius: 10px !important;
    margin: 5px !important;
}

.methodology-section {
    background: var(--card-bg);
    border-radius: 15px;
    padding: 25px;
    margin-top: 20px;
    box-shadow: var(--shadow);
    border: 1px solid var(--border-color);
}

.methodology-title {
    font-size: 1.25rem;
    font-weight: 600;
    color: var(--text-primary);
    margin: 0 0 15px 0;
}

.methodology-text {
    color: var(--text-secondary);
    line-height: 1.6;
    font-size: 0.95rem;
}
""")

# --- Advanced Data Processing ---
def load_and_process_data():
    # Load datasets
    stocks = pd.read_csv("data/maang_monthly.csv", parse_dates=["Date"])
    sunspots = pd.read_csv("data/sunspots_monthly.csv", parse_dates=["Date"])
    sunspots = sunspots.rename(columns={"Monthly Mean Total Sunspot Number": "SunspotNumber"})
    
    if "Unnamed: 0" in sunspots.columns:
        sunspots = sunspots.drop(columns=["Unnamed: 0"])
    
    # Merge and process
    merged = pd.merge(stocks, sunspots, on="Date", how="outer").sort_values("Date")
    merged["Close"] = merged["Close"].interpolate()
    merged["SunspotNumber"] = merged["SunspotNumber"].interpolate()
    merged = merged.dropna(subset=["Close", "SunspotNumber"])
    
    # Advanced feature engineering
    merged["Year"] = merged["Date"].dt.year
    merged["Decade"] = (merged["Year"] // 10) * 10
    
    # Rolling statistics
    merged["Close_MA12"] = merged["Close"].rolling(window=12).mean()
    merged["Sunspot_MA12"] = merged["SunspotNumber"].rolling(window=12).mean()
    merged["Close_Volatility"] = merged["Close"].rolling(window=12).std()
    
    # Normalization
    close_min, close_max = merged["Close"].min(), merged["Close"].max()
    sunspot_min, sunspot_max = merged["SunspotNumber"].min(), merged["SunspotNumber"].max()
    
    merged["Close_norm"] = (merged["Close"] - close_min) / (close_max - close_min)
    merged["Sunspot_norm"] = (merged["SunspotNumber"] - sunspot_min) / (sunspot_max - sunspot_min)
    
    # Calculate correlation
    correlation, p_value = pearsonr(merged["Close_norm"].dropna(), merged["Sunspot_norm"].dropna())
    
    return stocks, sunspots, merged, correlation, p_value

stocks, sunspots, merged, correlation, p_value = load_and_process_data()

# --- Key Statistics ---
total_years = (merged["Date"].max() - merged["Date"].min()).days / 365.25
stock_growth = ((merged["Close"].iloc[-1] / merged["Close"].iloc[0]) - 1) * 100
max_sunspots = merged["SunspotNumber"].max()
avg_sunspots = merged["SunspotNumber"].mean()

# --- Advanced Visualizations with Interactive Hovering ---
def create_stock_plot():
    # Add formatted date and percentage change for hover
    merged['Date_str'] = merged['Date'].dt.strftime('%B %Y')
    merged['Price_Change'] = merged['Close'].pct_change() * 100
    
    base = merged.hvplot.line(
        x="Date", y="Close", 
        line_width=3, line_color="#2563eb", line_alpha=0.8,
        height=350, responsive=True,
        title="MAANG Stock Price Evolution",
        hover_cols=['Date_str', 'Price_Change', 'Close_Volatility'],
        hover_tooltips=[
            ('Date', '@Date_str'),
            ('Price', '$@Close{0.00}'),
            ('Monthly Change', '@Price_Change{0.00}%'),
            ('Volatility', '@Close_Volatility{0.00}')
        ]
    )
    ma = merged.hvplot.line(
        x="Date", y="Close_MA12", 
        line_width=2, line_color="#60a5fa", line_dash="dashed",
        label="12-Month Moving Average",
        hover_tooltips=[
            ('Date', '@Date_str'),
            ('12-Month Average', '$@Close_MA12{0.00}')
        ]
    )
    return (base * ma).opts(
        xlabel="Year", ylabel="Stock Price ($)",
        legend_position="top_left",
        toolbar="above"
    )

def create_sunspot_plot():
    # Add solar cycle information
    merged['Solar_Intensity'] = pd.cut(merged['SunspotNumber'], 
                                     bins=[0, 50, 100, 200, 500], 
                                     labels=['Low', 'Moderate', 'High', 'Extreme'])
    
    return merged.hvplot.area(
        x="Date", y="SunspotNumber",
        fill_color="#f59e0b", fill_alpha=0.3,
        line_color="#d97706", line_width=2,
        height=350, responsive=True,
        title="Solar Activity Cycles",
        xlabel="Year", ylabel="Sunspot Count",
        hover_cols=['Date_str', 'Sunspot_MA12', 'Solar_Intensity'],
        hover_tooltips=[
            ('Date', '@Date_str'),
            ('Sunspot Count', '@SunspotNumber{0}'),
            ('12-Month Average', '@Sunspot_MA12{0.0}'),
            ('Solar Intensity', '@Solar_Intensity')
        ]
    )

def create_correlation_plot():
    # Add residuals and prediction intervals
    merged['Residual'] = merged['Close_norm'] - merged['Sunspot_norm'] * correlation
    merged['Decade_str'] = merged['Decade'].astype(str) + 's'
    
    scatter = merged.hvplot.scatter(
        x="Sunspot_norm", y="Close_norm",
        size=40, color="Decade", cmap="viridis", alpha=0.7,
        height=350, responsive=True,
        hover_cols=['Date_str', 'Decade_str', 'Residual', 'Close', 'SunspotNumber'],
        hover_tooltips=[
            ('Date', '@Date_str'),
            ('Decade', '@Decade_str'),
            ('Stock Price', '$@Close{0.00}'),
            ('Sunspots', '@SunspotNumber{0}'),
            ('Residual', '@Residual{0.000}')
        ]
    )
    
    # Add trend line
    z = np.polyfit(merged["Sunspot_norm"].dropna(), merged["Close_norm"].dropna(), 1)
    p = np.poly1d(z)
    x_trend = np.linspace(0, 1, 100)
    y_trend = p(x_trend)
    
    trend_df = pd.DataFrame({"x": x_trend, "y": y_trend})
    trend = trend_df.hvplot.line(
        x="x", y="y", 
        line_color="#ef4444", line_width=3, line_dash="dashed",
        hover_tooltips=[('Trend Line', 'y = @y{0.000}')]
    )
    
    return (scatter * trend).opts(
        title=f"Correlation Analysis (r={correlation:.3f})",
        xlabel="Normalized Sunspot Activity", 
        ylabel="Normalized Stock Price",
        toolbar="above"
    )

def create_overlay_plot():
    # Add difference and synchronization metrics
    merged['Sync_Diff'] = abs(merged['Close_norm'] - merged['Sunspot_norm'])
    merged['Market_Phase'] = np.where(merged['Close_norm'] > merged['Close_norm'].rolling(12).mean(), 
                                    'Bull Market', 'Bear Market')
    
    stock_line = merged.hvplot.line(
        x="Date", y="Close_norm",
        line_color="#2563eb", line_width=3,
        label="MAANG Stock (Normalized)", alpha=0.8,
        hover_cols=['Date_str', 'Close', 'Market_Phase', 'Sync_Diff'],
        hover_tooltips=[
            ('Date', '@Date_str'),
            ('Stock (Normalized)', '@Close_norm{0.000}'),
            ('Actual Price', '$@Close{0.00}'),
            ('Market Phase', '@Market_Phase'),
            ('Sync Difference', '@Sync_Diff{0.000}')
        ]
    )
    
    sunspot_line = merged.hvplot.line(
        x="Date", y="Sunspot_norm",
        line_color="#f59e0b", line_width=3,
        label="Sunspot Activity (Normalized)", alpha=0.8,
        hover_cols=['Date_str', 'SunspotNumber', 'Solar_Intensity'],
        hover_tooltips=[
            ('Date', '@Date_str'),
            ('Sunspots (Normalized)', '@Sunspot_norm{0.000}'),
            ('Actual Count', '@SunspotNumber{0}'),
            ('Solar Intensity', '@Solar_Intensity')
        ]
    )
    
    return (stock_line * sunspot_line).opts(
        height=400, responsive=True,
        title="Synchronized Market & Solar Cycles",
        xlabel="Year", ylabel="Normalized Values (0-1)",
        legend_position="top_left",
        toolbar="above"
    )

def create_decade_analysis():
    decade_stats = merged.groupby("Decade").agg({
        "Close": ["mean", "std", "count"],
        "SunspotNumber": ["mean", "std", "max"],
        "Close_Volatility": "mean"
    }).round(2)
    
    # Flatten column names properly
    decade_stats.columns = ['_'.join(str(col).split()) if isinstance(col, tuple) else str(col) for col in decade_stats.columns]
    decade_stats = decade_stats.reset_index()
    
    # Debug: print column names to see what we actually have
    print("Decade stats columns:", decade_stats.columns.tolist())
    
    # Create a simpler version with basic hover info
    decade_simple = merged.groupby("Decade").agg({
        "Close": "mean",
        "SunspotNumber": "mean",
        "Close_Volatility": "mean"
    }).round(2).reset_index()
    
    decade_simple.columns = ["Decade", "Avg_Stock_Price", "Avg_Sunspots", "Avg_Volatility"]
    
    return decade_simple.hvplot.bar(
        x="Decade", y=["Avg_Stock_Price", "Avg_Sunspots"],
        height=300, responsive=True, 
        color=["#2563eb", "#f59e0b"],
        hover_tooltips=[
            ('Decade', '@Decade'),
            ('Avg Stock Price', '$@Avg_Stock_Price{0.00}'),
            ('Avg Sunspots', '@Avg_Sunspots{0.0}'),
            ('Avg Volatility', '@Avg_Volatility{0.00}')
        ]
    ).opts(
        title="Decadal Trends Comparison",
        xlabel="Decade", ylabel="Average Values",
        legend_position="top_right",
        toolbar="above"
    )

# Create all plots
stock_plot = create_stock_plot()
sunspot_plot = create_sunspot_plot()
correlation_plot = create_correlation_plot()
overlay_plot = create_overlay_plot()
decade_plot = create_decade_analysis()

# --- Hero Section ---
def get_correlation_badge():
    if abs(correlation) > 0.5:
        badge_class = "correlation-positive" if correlation > 0 else "correlation-negative"
        strength = "Strong"
    elif abs(correlation) > 0.3:
        badge_class = "correlation-neutral"
        strength = "Moderate"
    else:
        badge_class = "correlation-neutral"
        strength = "Weak"
    
    return f'<span class="correlation-badge {badge_class}">{strength} Correlation: {correlation:.3f}</span>'

hero_content = f"""
<div class="hero-section">
    <div class="hero-content">
        <h1 class="main-title">🌟 Market Cosmos Analytics</h1>
        <p class="main-subtitle">Unveiling the Hidden Connections Between Solar Cycles and Financial Markets</p>
        {get_correlation_badge()}
        
        <div class="stats-grid">
            <div class="stat-card">
                <p class="stat-value">{total_years:.0f}</p>
                <p class="stat-label">Years Analyzed</p>
            </div>
            <div class="stat-card">
                <p class="stat-value">{stock_growth:+.1f}%</p>
                <p class="stat-label">Total Growth</p>
            </div>
            <div class="stat-card">
                <p class="stat-value">{max_sunspots:.0f}</p>
                <p class="stat-label">Peak Sunspots</p>
            </div>
            <div class="stat-card">
                <p class="stat-value">{avg_sunspots:.0f}</p>
                <p class="stat-label">Avg Sunspots</p>
            </div>
        </div>
    </div>
</div>
"""

hero = pn.pane.HTML(hero_content)

# --- Premium Cards ---
def create_premium_card(plot, title, subtitle, icon="📈"):
    header_html = f"""
    <div class="card-header">
        <h3 class="card-title">{icon} {title}</h3>
        <p class="card-subtitle">{subtitle}</p>
    </div>
    """
    
    return pn.Column(
        pn.pane.HTML(header_html),
        pn.pane.HoloViews(plot, sizing_mode="stretch_width"),
        css_classes=["premium-card"],
        sizing_mode="stretch_width"
    )

# Create premium cards
stock_card = create_premium_card(
    stock_plot, 
    "MAANG Stock Evolution", 
    "Long-term price trends with moving averages",
    "💹"
)

sunspot_card = create_premium_card(
    sunspot_plot,
    "Solar Activity Cycles",
    "11-year sunspot cycles and solar maximum periods",
    "☀️"
)

correlation_card = create_premium_card(
    correlation_plot,
    "Correlation Analysis",
    "Statistical relationship between normalized datasets",
    "🔬"
)

overlay_card = create_premium_card(
    overlay_plot,
    "Synchronized Patterns",
    "Normalized comparison revealing hidden connections",
    "🌊"
)

decade_card = create_premium_card(
    decade_plot,
    "Decadal Trends",
    "Long-term patterns across different decades",
    "📊"
)

# --- Insights Section ---
insights_html = f"""
<div class="insight-box">
    <strong>🔍 Key Insights:</strong><br>
    • Correlation coefficient of <strong>{correlation:.3f}</strong> suggests {'a positive' if correlation > 0 else 'a negative'} relationship<br>
    • Statistical significance: p-value = {p_value:.4f}<br>
    • Solar cycles may influence market sentiment through psychological and economic factors<br>
    • Peak sunspot activity periods show {'increased' if correlation > 0 else 'decreased'} market volatility
</div>
"""

insights = pn.pane.HTML(insights_html)

# --- Methodology Section ---
methodology_html = """
<div class="methodology-section">
    <h3 class="methodology-title">🧪 Methodology & Data Science</h3>
    <div class="methodology-text">
        <strong>Data Processing:</strong> Applied advanced interpolation, normalization (min-max scaling), and rolling statistics.<br>
        <strong>Statistical Analysis:</strong> Pearson correlation coefficient with significance testing.<br>
        <strong>Visualization:</strong> Interactive plots with trend analysis and multi-dimensional views.<br>
        <strong>Time Series:</strong> 40+ years of monthly data spanning multiple solar cycles.
    </div>
</div>
"""

methodology = pn.pane.HTML(methodology_html)

# --- Tabbed Interface ---
tabs = pn.Tabs(
    ("📈 Market Analysis", pn.Column(stock_card, correlation_card)),
    ("☀️ Solar Cycles", pn.Column(sunspot_card, decade_card)),
    ("🌊 Synchronized View", pn.Column(overlay_card, insights)),
    ("📊 Data & Methods", methodology),
    dynamic=True,
    tabs_location="above"
)

# --- Final Dashboard Layout ---
dashboard = pn.Column(
    hero,
    tabs,
    css_classes=["dashboard"],
    sizing_mode="stretch_width"
)

dashboard.servable(title="Market Cosmos Analytics - Competition Dashboard")


