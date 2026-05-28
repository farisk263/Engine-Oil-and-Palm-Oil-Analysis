"""
Generate a single-file interactive HTML dashboard for all three analysis tasks.
Run: python dashboard.py
Output: dashboard.html
"""
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import os

BASE = os.path.dirname(os.path.abspath(__file__))

# ── Load data ────────────────────────────────────────────────────────────────

df1 = pd.read_csv(os.path.join(BASE, "Task_1", "ingredient.csv"))

df2 = pd.read_csv(os.path.join(BASE, "Task_2", "palm_ffb.csv"))
df2["Date"] = pd.to_datetime(df2["Date"], format="%d.%m.%Y")
df2["Month"] = df2["Date"].dt.month
df2["Year"] = df2["Date"].dt.year
monthly_avg = df2.groupby("Month")["FFB_Yield"].mean().reset_index()
month_names = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
monthly_avg["MonthName"] = monthly_avg["Month"].apply(lambda m: month_names[m - 1])

df3 = pd.read_csv(os.path.join(BASE, "Task_3", "distribution.csv"))
df3.columns = ["word", "count"]
df3 = df3.sort_values("count", ascending=False).head(20)

# ── Task 1 computations ───────────────────────────────────────────────────────

corr = df1.corr()

scaler = StandardScaler()
X_scaled = scaler.fit_transform(df1)
pca = PCA(n_components=2, random_state=42)
components = pca.fit_transform(X_scaled)
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
labels = kmeans.fit_predict(components)
var1, var2 = pca.explained_variance_ratio_ * 100

# ── Build figure ──────────────────────────────────────────────────────────────

fig = make_subplots(
    rows=5, cols=2,
    subplot_titles=(
        "Task 1 — Additive Distributions (Box Plots)", "",
        "Task 1 — Correlation Heatmap", "Task 1 — PCA + K-Means Clusters",
        "Task 2 — FFB Yield Over Time (2008–2018)", "",
        "Task 2 — FFB Yield vs Precipitation", "Task 2 — Seasonal Pattern (Monthly Avg)",
        "Task 3 — Top 20 Word Frequencies", "",
    ),
    specs=[
        [{"colspan": 2}, None],
        [{}, {}],
        [{"colspan": 2}, None],
        [{}, {}],
        [{"colspan": 2}, None],
    ],
    vertical_spacing=0.08,
    horizontal_spacing=0.08,
    row_heights=[0.15, 0.20, 0.15, 0.20, 0.15],
)

COLORS = [
    "#4C78A8", "#F58518", "#54A24B", "#E45756", "#72B7B2",
    "#B279A2", "#FF9DA6", "#9D755D", "#BAB0AC",
]

# Row 1: Box plots
for i, col in enumerate(df1.columns):
    fig.add_trace(
        go.Box(y=df1[col], name=f"Additive {col.upper()}",
               marker_color=COLORS[i], showlegend=False),
        row=1, col=1,
    )

# Row 2 left: Heatmap
fig.add_trace(
    go.Heatmap(
        z=corr.values,
        x=[c.upper() for c in corr.columns],
        y=[c.upper() for c in corr.index],
        colorscale="RdBu",
        zmid=0,
        text=[[f"{v:.2f}" for v in row] for row in corr.values],
        texttemplate="%{text}",
        showscale=True,
    ),
    row=2, col=1,
)

# Row 2 right: PCA scatter
cluster_colors = ["#4C78A8", "#F58518", "#54A24B"]
for k in range(3):
    mask = labels == k
    fig.add_trace(
        go.Scatter(
            x=components[mask, 0], y=components[mask, 1],
            mode="markers",
            name=f"Cluster {k + 1}",
            marker=dict(color=cluster_colors[k], size=6, opacity=0.7),
        ),
        row=2, col=2,
    )

# Row 3: FFB time-series
fig.add_trace(
    go.Scatter(
        x=df2["Date"], y=df2["FFB_Yield"],
        mode="lines", name="FFB Yield",
        line=dict(color="#54A24B", width=1.5),
        showlegend=False,
    ),
    row=3, col=1,
)

# Row 4 left: FFB vs Precipitation
fig.add_trace(
    go.Scatter(
        x=df2["Precipitation"], y=df2["FFB_Yield"],
        mode="markers",
        marker=dict(color="#4C78A8", size=6, opacity=0.6),
        name="FFB vs Precipitation",
        showlegend=False,
    ),
    row=4, col=1,
)

# Row 4 right: Monthly seasonal bar
fig.add_trace(
    go.Bar(
        x=monthly_avg["MonthName"], y=monthly_avg["FFB_Yield"],
        marker_color="#72B7B2",
        name="Monthly Avg FFB",
        showlegend=False,
    ),
    row=4, col=2,
)

# Row 5: Word frequency
fig.add_trace(
    go.Bar(
        x=df3["word"], y=df3["count"],
        marker_color="#B279A2",
        name="Word Frequency",
        showlegend=False,
    ),
    row=5, col=1,
)

# ── Axis labels ───────────────────────────────────────────────────────────────

fig.update_xaxes(title_text="Additive", row=1, col=1)
fig.update_yaxes(title_text="Value", row=1, col=1)

fig.update_xaxes(title_text=f"PC1 ({var1:.1f}% var)", row=2, col=2)
fig.update_yaxes(title_text=f"PC2 ({var2:.1f}% var)", row=2, col=2)

fig.update_xaxes(title_text="Date", row=3, col=1)
fig.update_yaxes(title_text="FFB Yield (t/ha)", row=3, col=1)

fig.update_xaxes(title_text="Precipitation (mm)", row=4, col=1)
fig.update_yaxes(title_text="FFB Yield (t/ha)", row=4, col=1)

fig.update_xaxes(title_text="Month", row=4, col=2)
fig.update_yaxes(title_text="Avg FFB Yield (t/ha)", row=4, col=2)

fig.update_xaxes(title_text="Word", row=5, col=1)
fig.update_yaxes(title_text="Frequency", row=5, col=1)

# ── Layout ────────────────────────────────────────────────────────────────────

fig.update_layout(
    title=dict(
        text="<b>Engine Oil & Palm Oil Analysis — Interactive Dashboard</b>",
        font=dict(size=20),
        x=0.5,
    ),
    height=1800,
    template="plotly_white",
    legend=dict(orientation="h", yanchor="bottom", y=1.01, xanchor="right", x=1),
    font=dict(family="Arial, sans-serif", size=12),
)

# ── Export ────────────────────────────────────────────────────────────────────

out = os.path.join(BASE, "dashboard.html")
fig.write_html(out, include_plotlyjs="cdn")
print(f"Dashboard written to: {out}")
