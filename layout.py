from dash import html
import dash_bootstrap_components as dbc

from components import (
                    pie_chart,
                    bar_chart,
                    bar_h_chart,
                    scatter_chart
                )
def create_layout(app, data):
    return dbc.Container(
        [
            pie_chart.render(app,data),
            bar_chart.render(app,data),
            bar_h_chart.render(app,data),
            scatter_chart.render(app,data),
        ]
    )
