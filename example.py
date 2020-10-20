# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from joblib import load
import pandas as pd
​
# Imports from this application
from app import app
​
pipeline = load('assets/pipeline.joblib')
​
@app.callback(Output('prediction-content', 'children'),
             [Input('film', 'value'),
              Input('year', 'value'),
              Input('body_count', 'value'),
              Input('length_minutes', 'value'),
              Input('mpaa_rating', 'value'),
              Input('genre', 'value')])
def predict(film, year, body_count, length_minutes, mpaa_rating, genre):
    df = pd.DataFrame(
        columns=['film', 'year', 'body_count', 'length_minutes', 'mpaa_rating', 'genre'],
        data = [[film, year, body_count, length_minutes, mpaa_rating, genre]]
    )
​
    y_pred = pipeline.predict(df)[0]
    return f'Rating of {y_pred:.2f}'
​
# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Predictions
​
            Adjust the variables to create your movie and find out just how well-received it will be!
​
            """
        ),
        html.H2('Predicted IMDb Rating', className='mb-5'), 
        html.Div(id='prediction-content', className='lead')
    ],
    md=4,
)
​
column2 = dbc.Col(
    [
        dcc.Markdown('## Predictions', className='mb-5'), 
        dcc.Markdown('#### Title'),
        dcc.Input(
            id='film',
            placeholder='Movie title here',
            type='text',
            value=''
        ),
        dcc.Markdown('#### Year'), 
        dcc.Slider(
            id='year', 
            min=1945, 
            max=2015, 
            step=1, 
            value=1995, 
            marks={n: str(n) for n in range(1945,2015,10)}, 
            className='mb-5', 
        ), 
        dcc.Markdown('#### Body Count'), 
        dcc.Slider(
            id='body_count', 
            min=1, 
            max=1000, 
            step=1, 
            value=75, 
            marks={n: str(n) for n in range(0,1000,50)}, 
            className='mb-5', 
        ), 
        dcc.Markdown('#### Length (in minutes)'), 
        dcc.Slider(
            id='length_minutes', 
            min=80, 
            max=220, 
            step=5, 
            value=75, 
            marks={n: str(n) for n in range(80, 220, 20)}, 
            className='mb-5', 
        ), 
        dcc.Markdown('#### MPAA Rating'), 
        dcc.Dropdown(
            id='mpaa_rating', 
            options = [
                {'label': 'G', 'value': 'G'}, 
                {'label': 'GP', 'value': 'GP'}, 
                {'label': 'PG', 'value': 'PG'}, 
                {'label': 'PG-13', 'value': 'PG-13'}, 
                {'label': 'M', 'value': 'M'},
                {'label': 'R', 'value': 'R'},
                {'label': 'X', 'value': 'X'},
                {'label': 'NR', 'value': 'NR'},
                {'label': 'Unrated', 'value': 'Unrated'},
                {'label': 'Approved', 'value': 'Approved'}, 
            ], 
            value = 'R', 
            className='mb-5', 
        ),
        dcc.Markdown('#### Genre'), 
        dcc.Dropdown(
            id='genre', 
            options = [
                {'label': 'Action', 'value': 'Action'}, 
                {'label': 'Adventure', 'value': 'Adventure'}, 
                {'label': 'Animation', 'value': 'Animation'}, 
                {'label': 'Biography', 'value': 'Biography'}, 
                {'label': 'Comedy', 'value': 'Comedy'},
                {'label': 'Crime', 'value': 'Crime'},
                {'label': 'Documentary', 'value': 'Documentary'},
                {'label': 'Drama', 'value': 'Drama'},
                {'label': 'Fantasy', 'value': 'Fantasy'},
                {'label': 'Film-Noir', 'value': 'Film-Noir'}, 
                {'label': 'Horror', 'value': 'Horror'},
                {'label': 'Mystery', 'value': 'Mystery'},
                {'label': 'Science Fiction', 'value': 'Science Fiction'},
                {'label': 'Thriller', 'value': 'Thriller'},
                {'label': 'War Drama', 'value': 'War Drama'},
                {'label': 'Western', 'value': 'Western'}, 
            ], 
            value = 'Action', 
            className='mb-5', 
        ), 
    ],
)
​
layout = dbc.Row([column1, column2])