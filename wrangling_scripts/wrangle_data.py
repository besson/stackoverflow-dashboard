import pandas as pd
import plotly.graph_objs as go


def return_figures():
    """Creates four plotly visualizations

    Args:
        None

    Returns:
        list (dict): list containing the four plotly visualizations

    """

    # first chart plots arable land from 1990 to 2015 in top 10 economies 
    # as a line chart

    df = pd.read_csv('data/plot1.csv').reset_index()

    layout_one = go.Layout(
        dict(title='Last hire date distribution by Job role',
             barmode='stack',
             xaxis=dict(title='Last hire date distribution'),
             yaxis=dict(title='Job role')
             )
    )

    job_roles = {'Less than a year ago': '#106ba4', '1-2 years ago': '#fc800e',
                 '3-4 years ago': '#ababab', 'More than 4 years ago': '#595959'}
    graph_one = []

    for jr in job_roles.keys():
        graph_one.append(
            go.Bar(
                x=list(map(lambda x: round(x, 2), df[jr].values)),
                y=df['JobRole'].values,
                orientation='h',
                name=jr,
                marker=dict(color=job_roles[jr]),
                hovertemplate='%{x}%'
            ),
        )

    layout_one = go.Layout(
        dict(title='Last hire date distribution by Job role',
             barmode='stack',
             xaxis=dict(title='Last hire date distribution'),
             yaxis=dict(title='Job role'),
             autosize=False,
             width=1500,
             height=1000,
             margin=dict(l=350, r=15, pad=10)
             )
    )

    # append all charts to the figures list
    figures = []
    figures.append(dict(data=graph_one, layout=layout_one))

    return figures
