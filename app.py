import streamlit as st

from src.data_loader import load_data
from src.preprocessing import split_indoor_outdoor

from src.analytics import (
    daily_temperature_trends,
    monthly_temperature_trends,
    rolling_temperature_trend,
    generate_kpis,
    generate_alert
)

from src.visualizations import create_dashboard


# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="IoT Monitoring Dashboard",
    layout="wide"
)


# ==================================================
# TITLE
# ==================================================

st.title("IoT Temperature Monitoring Dashboard")


# ==================================================
# LOAD DATA
# ==================================================

df = load_data("data/IOT-temp.csv")


# ==================================================
# PREPROCESSING
# ==================================================

indoor, outdoor = split_indoor_outdoor(df)


# ==================================================
# ANALYTICS
# ==================================================

daily = daily_temperature_trends(df)

monthly = monthly_temperature_trends(df)

rolling_trend = rolling_temperature_trend(df)


# ==================================================
# KPI + ALERTS
# ==================================================

kpis = generate_kpis(df, indoor, outdoor)

alert_status = generate_alert(df)


# ==================================================
# KPI SECTION
# ==================================================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Latest Indoor Reading",
        f"{kpis['current_indoor_temp']}°C"
    )

with col2:
    st.metric(
        "Latest Outdoor Reading",
        f"{kpis['current_outdoor_temp']}°C"
    )

with col3:
    st.metric(
        "Highest Recorded Temp",
        f"{kpis['highest_temp']}°C"
    )

with col4:
    st.metric(
        "Average Temperature",
        f"{kpis['average_temp']}°C"
    )


# ==================================================
# ALERT SECTION
# ==================================================

if alert_status == "HIGH TEMPERATURE ALERT":

    st.error(alert_status)

else:

    st.success(alert_status)


# ==================================================
# DASHBOARD VISUALIZATION
# ==================================================

fig = create_dashboard(
    daily,
    rolling_trend,
    indoor,
    outdoor,
    monthly
)

st.plotly_chart(
    fig,
    use_container_width=True
)