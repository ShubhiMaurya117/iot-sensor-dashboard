import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Load and clean
df = pd.read_csv("IOT-temp.csv")
df.columns = ['id', 'room_id', 'noted_date', 'temp', 'out_in']
df['noted_date'] = pd.to_datetime(df['noted_date'], format='mixed', dayfirst=True)
df = df.dropna()

indoor = df[df['out_in'] == 'In']
outdoor = df[df['out_in'] == 'Out']

# Daily averages for trend chart
df_daily = df.groupby([df['noted_date'].dt.date, 'out_in'])['temp'].mean().unstack()
df_daily.index = pd.to_datetime(df_daily.index)

# Monthly averages
df['month'] = df['noted_date'].dt.strftime('%b %Y')
month_order = df.groupby('month')['noted_date'].min().sort_values().index.tolist()
monthly = df.groupby(['month', 'out_in'])['temp'].mean().unstack().reindex(month_order)

fig = make_subplots(
    rows=2, cols=2,
    subplot_titles=(
        'Average Temperature: Indoor vs Outdoor',
        'Temperature Trend Over Time',
        'Temperature Distribution',
        'Monthly Average Temperature'
    ),
    vertical_spacing=0.15,
    horizontal_spacing=0.1
)

# Chart 1 - Bar chart
fig.add_trace(go.Bar(name='Indoor', x=['Indoor'], y=[indoor['temp'].mean()],
    marker_color='#4C9BE8', showlegend=True), row=1, col=1)
fig.add_trace(go.Bar(name='Outdoor', x=['Outdoor'], y=[outdoor['temp'].mean()],
    marker_color='#E8704C', showlegend=True), row=1, col=1)

# Chart 2 - Line chart
fig.add_trace(go.Scatter(x=df_daily.index, y=df_daily['In'],
    name='Indoor', line=dict(color='#4C9BE8', width=2), showlegend=False), row=1, col=2)
fig.add_trace(go.Scatter(x=df_daily.index, y=df_daily['Out'],
    name='Outdoor', line=dict(color='#E8704C', width=2), showlegend=False), row=1, col=2)

# Chart 3 - Histogram
fig.add_trace(go.Histogram(x=indoor['temp'], name='Indoor',
    marker_color='#4C9BE8', opacity=0.7, showlegend=False), row=2, col=1)
fig.add_trace(go.Histogram(x=outdoor['temp'], name='Outdoor',
    marker_color='#E8704C', opacity=0.7, showlegend=False), row=2, col=1)

# Chart 4 - Monthly bar
fig.add_trace(go.Bar(x=monthly.index, y=monthly['In'],
    name='Indoor', marker_color='#4C9BE8', showlegend=False), row=2, col=2)
fig.add_trace(go.Bar(x=monthly.index, y=monthly['Out'],
    name='Outdoor', marker_color='#E8704C', showlegend=False), row=2, col=2)

fig.update_layout(
    title_text='IoT Temperature Sensor Analysis Dashboard',
    title_font_size=20,
    height=800,
    template='plotly_dark',
    barmode='group'
)

fig.update_yaxes(title_text='Temperature (°C)', row=1, col=1)
fig.update_yaxes(title_text='Temperature (°C)', row=1, col=2)
fig.update_yaxes(title_text='Frequency', row=2, col=1)
fig.update_yaxes(title_text='Temperature (°C)', row=2, col=2)
fig.update_xaxes(title_text='Temperature (°C)', row=2, col=1)
fig.update_xaxes(title_text='Month', row=2, col=2)

fig.write_html("temperature_dashboard.html")
fig.show()
print("Interactive dashboard saved as temperature_dashboard.html!")