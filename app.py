from flask import Flask, render_template
import pandas as pd
import numpy as np
import plotly.express as px
import warnings
warnings.filterwarnings('ignore')
app = Flask(__name__)


def load_dataset():
    df=pd.read_csv(r'C:\Users\LENOVO\Documents\Video-Game-Analysis\Dataset\vgsales.csv')
    df.Publisher.fillna('Electronic Arts',inplace=True)
    df.Year.fillna(2009.0,inplace=True)
    return df

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/overview')
def overview():
    return render_template('overview.html')

@app.route('/platform')
def platform():
    return render_template('platform.html')

@app.route('/Publisher')
def publisher():
    return render_template('Publisher.html')

@app.route('/sales')
def sales():
    return render_template('sales.html')

@app.route('/summary')
def summary():
    return render_template('summary.html')

@app.route('/tool')
def tools():
    return render_template('tool.html')

@app.route('/graphs')
def graph():
    df = load_dataset()
    cols={
    'Global_Sales':'Global Sales',
    'NA_Sales':'Sales in North America',
    'EU_Sales':'Sales in Europe',
    'JP_Sales':'Sales in Japen',
    'Other_Sales':'Sales in the rest of the world'}
    figures = []
    for i in ['Global_Sales','NA_Sales','EU_Sales','JP_Sales','Other_Sales']:
        fig=px.treemap(
            df[df.Rank<=10],
            path=['Name'],
            values=i,
            color=i,
            color_continuous_scale='Geyser',
            title=f'Treemap of Top 10 {cols[i]} Video Games',
            template='plotly_dark')
        fig.update_traces(textinfo='label+value')
        fig.update_layout(margin=dict(t=50,l=25,r=25,b=25))
        figures.append(fig.to_html())

    
    fig3 = px.line(
    df.groupby(df.Year).sum().reset_index(),
    x='Year',
    y=['Global_Sales','NA_Sales','EU_Sales','JP_Sales','Other_Sales'],
    title='Sum of Sales by Year',
    template='plotly_dark')

    fig4 = px.line(
    df.groupby(df.Year).mean().reset_index(),
    x='Year',
    y=['Global_Sales','NA_Sales','EU_Sales','JP_Sales','Other_Sales'],
    title='Average of Sales by Year',
    template='plotly_dark')

    fig5 = px.histogram(
    df,
    'Year',
    title='Count of Video Games by Year',
    template='plotly_dark',
    color_discrete_sequence=['#ffffff'],
    marginal='violin')
    fig5.update_layout(bargap=0.1)

    fig6 = px.histogram(
    df[df.Rank<=100],
    'Year',
    title='Count of Video Games by Year',
    template='plotly_dark',
    color_discrete_sequence=['#ffffff'],
    marginal='box')
    fig6.update_layout(bargap=0.1)

    fig7 = px.histogram(
    df,
    'Platform',
    title='Count of Video Games by Platform',
    template='plotly_dark',
    color_discrete_sequence=['#ffffff'],
    marginal='box')
    fig7.update_layout(bargap=0.1)

    fig8 = px.histogram(
    df[df.Rank<=100],
    'Platform',
    title='Count of Video Games by Platform',
    template='plotly_dark',
    color_discrete_sequence=['#ffffff'],
    marginal='box')
    fig8.update_layout(bargap=0.1)

    fig9 = px.histogram(
    df,
    'Genre',
    title='Count of Video Games by Genre',
    template='plotly_dark',
    color_discrete_sequence=['#ffffff'],
    marginal='box')
    fig9.update_layout(bargap=0.1)

    fig10 = px.histogram(
    df[df.Rank<=100],
    'Genre',
    title='Count of Video Games by Genre',
    template='plotly_dark',
    color_discrete_sequence=['#ffffff'],
    marginal='box')
    fig10.update_layout(bargap=0.1)

    fig11 = px.treemap(
    df,
    path=['Publisher'],
    title='Count of Video Games by Publisher',
    template='plotly_dark')
    fig11.update_traces(textinfo='label+value')
    fig11.update_layout(margin=dict(t=50,l=25,r=25,b=25))

    fig12 = px.treemap(
    df[df.Rank<=100],
    path=['Publisher'],
    title='Count of Video Games by Publisher',
    template='plotly_dark')
    fig12.update_traces(textinfo='label+value')
    fig12.update_layout(margin=dict(t=50,l=25,r=25,b=25))

    fig13 = px.treemap(
    df,
    path=['Publisher','Genre'],
    title='Density of Genre of each Publisher',
    template='plotly_dark')
    fig13.update_traces(textinfo='label+value')
    fig13.update_layout(margin=dict(t=50,l=25,r=25,b=25))

    return render_template('graphs.html', fig3=fig3.to_html(),
                                           fig4=fig4.to_html(),
                                           fig5=fig5.to_html(),
                                           fig6=fig6.to_html(),
                                           fig7=fig7.to_html(),
                                            fig8=fig8.to_html(),
                                            fig9=fig9.to_html(),
                                            fig10=fig10.to_html(),
                                            fig11=fig11.to_html(),
                                            fig12=fig12.to_html(),
                                            fig13=fig13.to_html(),
                                            figures=figures) 
if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 