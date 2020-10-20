# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# 1 column layout
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Process
            In order to achieve the most accurate results possible we take into consideration a few major factors.
            To begin with we have created a three step system

            1) Ask
            2) Compute
            3) Display

            Following these three simple steps we are capable of recommending to you the best possible strains to alievate your illness.


            """
        ),

    ],
)

layout = dbc.Row([column1])