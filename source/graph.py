import os
import requests
import pandas as pd
import plotly.graph_objects as go

from source.auxiiliar import Aux

class Graph:
    def __init__(self, pivot, lista_de_fechas) -> None:
        self.pivot=pivot
        self.lista_de_fechas=lista_de_fechas
    
    def compute(self,i):
        data = list(self.pivot["size"][i])
        data_procesado = Aux.MA(data, 7)
        

        fig = go.Figure()

        fig.add_trace(go.Scatter(x=self.lista_de_fechas, y=data,
                mode='markers',
                name='dia'))

        fig.add_trace(go.Scatter(x=self.lista_de_fechas, y=data_procesado,
                mode='lines',
                name='tendencia'))

        fig.update_layout(
            title = i.capitalize() + ': Fallecidos y Contagiados Media Movil 7 dias ' + str(self.lista_de_fechas[-1].strftime('%Y-%m-%d')),
                xaxis_tickformat = '%d %B %Y',
            showlegend=True,
            template="plotly_white",
            legend=dict(
                yanchor="top",
                y=0.99,
                xanchor="left",
                x=0.01)
            )

        fig.write_html("htmls/"+i.capitalize()+".html")
