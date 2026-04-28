import plotly.graph_objects as go
from plotly.subplots import make_subplots


def create_dashboard(
    daily,
    rolling_trend,
    indoor,
    outdoor,
    monthly
):

    fig = make_subplots(
        rows=3,
        cols=1,

        subplot_titles=(
            "Temperature Trend Analysis",
            "Temperature Distribution",
            "Monthly Temperature Trends"
        ),

        vertical_spacing=0.12
    )

    # ==================================================
    # 1. MAIN TREND CHART
    # ==================================================

    fig.add_trace(

        go.Scatter(
            x=daily.index,
            y=daily['In'],

            name='Indoor Temperature',

            line=dict(width=3)
        ),

        row=1,
        col=1
    )

    fig.add_trace(

        go.Scatter(
            x=daily.index,
            y=daily['Out'],

            name='Outdoor Temperature',

            line=dict(width=3)
        ),

        row=1,
        col=1
    )

    fig.add_trace(

        go.Scatter(
            x=rolling_trend.index,
            y=rolling_trend.values,

            name='Rolling Average',

            line=dict(
                width=1
            )
        ),

        row=1,
        col=1
    )

    # ==================================================
    # 2. BOX PLOT
    # ==================================================

    fig.add_trace(

        go.Box(
            y=indoor['temp'],

            name='Indoor',

            boxmean=True
        ),

        row=2,
        col=1
    )

    fig.add_trace(

        go.Box(
            y=outdoor['temp'],

            name='Outdoor',

            boxmean=True
        ),

        row=2,
        col=1
    )

    # ==================================================
    # 3. MONTHLY TRENDS
    # ==================================================

    fig.add_trace(

        go.Bar(
            x=monthly.index,
            y=monthly['In'],

            name='Indoor Monthly Avg'
        ),

        row=3,
        col=1
    )

    fig.add_trace(

        go.Bar(
            x=monthly.index,
            y=monthly['Out'],

            name='Outdoor Monthly Avg'
        ),

        row=3,
        col=1
    )

    # ==================================================
    # LAYOUT
    # ==================================================

    fig.update_layout(

        template='plotly_dark',

        height=1200,

        title='IoT Sensor Analytics Dashboard',

        title_font_size=28,

        showlegend=True
    )

    return fig