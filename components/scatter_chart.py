from dash import html, dcc
import plotly.express as px

def render(app, data):
    size=[i*40 for i in data["Trill"]]
    fig=px.scatter(data, x="country", y="Trill", size=size)
    return html.Div(dcc.Graph (figure=fig), id="scatter-plot")


