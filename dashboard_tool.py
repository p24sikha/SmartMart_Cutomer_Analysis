import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import dash_bootstrap_components as dbc

# Load the data
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import dash_bootstrap_components as dbc
import numpy as np

# Load the data
sheet_url = "https://docs.google.com/spreadsheets/d/1SAE7gZTOLkAjaczR8bFdoFSz7PknK9XQcHrYbPz_RBI/export?format=csv"
df = pd.read_csv(sheet_url)

# Initialize the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])


# Create visualizations
def create_figures():
    # Age distribution
    fig_age = px.histogram(df, x="Age", nbins=20, title="Age Distribution")

    # Annual Income by Gender
    fig_income_gender = px.box(df, x="Gender", y="Annual_Income", title="Annual Income by Gender")

    # Correlation heatmap (only numeric columns)
    numeric_df = df.select_dtypes(include=[np.number])
    fig_heatmap = px.imshow(numeric_df.corr(), title="Correlation Heatmap (Numeric Columns)",
                            color_continuous_scale="Viridis")

    # Scatter plot of Annual Income vs. Age
    fig_scatter = px.scatter(df, x="Age", y="Annual_Income", color="Gender", size="Purchase_History",
                             title="Annual Income vs. Age", hover_data=["CustomerID"])

    # Purchase History by Gender
    fig_purchase_gender = px.violin(df, x="Gender", y="Purchase_History", title="Purchase History by Gender")

    # Website Visits Distribution
    fig_website_visits = px.histogram(df, x="Website_Visits", nbins=15, title="Website Visits Distribution")

    # App Usage by Gender
    fig_app_usage = px.bar(df, x="Gender", y="App_Usage", title="App Usage by Gender")

    # Age vs Purchase History
    fig_age_purchase = px.scatter(df, x="Age", y="Purchase_History", color="Gender", size="Annual_Income",
                                  title="Age vs Purchase History", hover_data=["CustomerID"])

    # Annual Income Distribution
    fig_income_dist = px.histogram(df, x="Annual_Income", nbins=20, title="Annual Income Distribution")

    # Website Visits vs App Usage
    fig_website_app = px.scatter(df, x="Website_Visits", y="App_Usage", color="Gender", size="Purchase_History",
                                 title="Website Visits vs App Usage", hover_data=["CustomerID"])

    # Purchase History Distribution
    fig_purchase_dist = px.histogram(df, x="Purchase_History", nbins=15, title="Purchase History Distribution")

    # App Usage Distribution
    fig_app_usage_dist = px.histogram(df, x="App_Usage", nbins=10, title="App Usage Distribution")

    figures = [fig_age, fig_income_gender, fig_heatmap, fig_scatter, fig_purchase_gender,
               fig_website_visits, fig_app_usage, fig_age_purchase, fig_income_dist,
               fig_website_app, fig_purchase_dist, fig_app_usage_dist]

    # Apply consistent styling to all figures
    for fig in figures:
        fig.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(color="white"),
            title_font=dict(color="white", size=18),
            legend_title_font=dict(color="white"),
            legend_font=dict(color="white"),
            coloraxis_colorbar=dict(title_font=dict(color="white"), tickfont=dict(color="white")),
            height=350,  # Set a fixed height for all plots
            margin=dict(l=40, r=40, t=40, b=40)  # Adjust margins
        )
        fig.update_xaxes(title_font=dict(color="white"), tickfont=dict(color="white"),
                         gridcolor="rgba(255,255,255,0.1)")
        fig.update_yaxes(title_font=dict(color="white"), tickfont=dict(color="white"),
                         gridcolor="rgba(255,255,255,0.1)")

    return figures


figures = create_figures()

# Layout of the app
app.layout = html.Div(
    style={'backgroundColor': 'black', 'padding': '20px'},
    children=[
        html.H1(
            "SmartMart Customer Analysis Dashboard",
            style={'textAlign': 'center', 'color': 'white', 'marginBottom': '30px'}
        ),
        html.Div([
            dbc.Row([
                dbc.Col(dcc.Graph(figure=fig), width=4, className="mb-4")
                for fig in figures
            ])
        ])
    ]
)

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)