import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

Saber_11_2019_a= pd.read_csv("Saber_11_2019_a.csv", 
                 sep = ',',
                 index_col=0,
                 )

columns = ['COLE_CARACTER',
          'ESTU_DEPTO_RESIDE',
          'PUNT_GLOBAL','COLE_NATURALEZA','PUNT_MATEMATICAS',            
          'PUNT_LECTURA_CRITICA',
          'PUNT_C_NATURALES', 
          'PUNT_SOCIALES_CIUDADANAS',
          'PUNT_INGLES',"ESTU_GENERO"]

base= Saber_11_2019_a.copy()
base = base[columns]

base=base[base.ESTU_GENERO.isin(['F','M'])]
base

basea=base[(base.PUNT_GLOBAL <= 150)]
basea=basea[basea.COLE_CARACTER.isin(["ACADÉMICO","TÉCNICO/ACADÉMICO","TÉCNICO","NO APLICA"])]
basea


####camilo
columns2 = ['ESTU_GENERO',
          'ESTU_DEPTO_RESIDE',
          'PUNT_MATEMATICAS',            
          'PUNT_LECTURA_CRITICA',
          'PUNT_C_NATURALES', 
          'PUNT_SOCIALES_CIUDADANAS',
          'PUNT_INGLES',
          'PUNT_GLOBAL']

Saber_11_2019_0 = Saber_11_2019_a.copy()
Saber_11_2019_0 = Saber_11_2019_0[columns2]
Saber_11_2019_and= Saber_11_2019_0[Saber_11_2019_0.ESTU_DEPTO_RESIDE.isin(["ANTIOQUIA","BOGOTÁ","VALLE","ATLANTICO","SANTANDER"])]

columns1 = ['COLE_NATURALEZA','FAMI_ESTRATOVIVIENDA','PUNT_GLOBAL']
base1= Saber_11_2019_a.copy()
base1=base1[columns1]

base1=base1[base1.COLE_NATURALEZA.isin(['OFICIAL','NO OFICIAL'])]
base1
basec=base1[(base1.PUNT_GLOBAL <= 500)]
basec=basec[basec.FAMI_ESTRATOVIVIENDA.isin(["Estrato 1","Estrato 2","Estrato 3","Estrato 4","Estrato 5","Estrato 6"])]
basec

available_colen = basec['COLE_NATURALEZA'].unique()
available_estrato = basec["FAMI_ESTRATOVIVIENDA"].unique()

available_depto = basea['ESTU_DEPTO_RESIDE'].unique()
available_colegios = basea["COLE_CARACTER"].unique()
available_depto_1=base["ESTU_DEPTO_RESIDE"].unique()

app.layout = html.Div(
  children=[
        html.H1(children="Proyecto Final",
            style = {
                        'textAlign': 'center',
            }),
        html.H2(children="Información Basica De La Base"),
        html.P(
            children=" La base de saber 11 del año 2019 cuenta con 82 variables, las cuales 23 de ellas son variables numéricas y las que restan son de carácter categórico, esta base tiene 546.212 las cuales de las cuales se eliminaron Se eliminaron de la base 56651 datos lo cual en porcentaje es un 10.37% de los datos; las variables con más datos faltantes son ESTU_DEDICACIONINTERNET, FAMI_COMELECHEDERIVADOS, FAMI_TIENESERVICIOTV, FAMI_COMECEREALFRUTOSLEGUMBRE, Esta base no cuenta con valores duplicados por ende solo se utilizaran 489.561 los gráficos se muestran a continuación." ),
    html.Div([
        html.Div([
            html.H3(children='Visualización N° 1'),
            html.H6(children="Kevin Malambo A"),
            html.P("Para este grafico se decidió primero Filtrar el puntaje global inferior o igual a 150, para poder mirar por medio de un mapa de calor en que departamentos se encuentran mayoritariamente y que tipo de colegios tiene mayor numero de personas con dichos puntajes, para este mapa es recomendado utilizar máximo 5 departamentos y máximo 3 tipos de colegio."),
            html.Div(children='''
                
                Departamento 
            
            '''),
            dcc.Dropdown(
                id='crossfilter_depto',
                 options=[{'label': x, 'value': x} 
                            for x in available_depto],
                value = ['CAUCA', 'ATLANTICO'],            
                multi = True
                ),
            html.Div(children='''
                
                Tipo de Colegio 
            
            '''),#
            dcc.Dropdown(
                id='crossfilter_depto2',
                 options=[{'label': x, 'value': x} 
                            for x in available_colegios],
                value = ['ACADÉMICO', 'TÉCNICO'],
                multi = True
                ),
            dcc.Graph(
                id='Grafico_1'
            ),  
        ], className='six columns'),
        html.Div([
            html.H3(children='Visualización N° 2'),
            html.H6(children="Kevin Malambo A"),
            html.P("Para la siguiente grafica de barras apiladas por departamento y se quiere mirar que genero tiene"
             "mejor promedio en la prueba de inglés, estos departamentos se pueden comparar con las personas que realizaron dicho"
             " examen en el extranjero, para esta grafica no se realizó ningún tipo de filtro  "),
            html.Div(children='''	
                Departamentos
            '''),#
            dcc.Checklist(id='Valores',
                options=[{'label': i, 'value': i} 
                            for i in available_depto_1],
                value = ['CAUCA', 'ATLANTICO'],
                labelStyle={'display': 'inline-block'}
                ),
            dcc.Graph(
                id='example-graph-2'
            ),  
        ], className='six columns'),
    ], className='row'),#   
        html.Div(
        children = [html.Div([
            html.H3(children='Visualización N° 2'),
            html.P("En este grafico se desarrollo un mapa de color para identificar la cantidad de estudiantes por cada Estrato Social con respecto a el tipo de Colegio en el que estudiaba el individuo a la Hora de presentar la nota"),
            dcc.Dropdown(
                id='crossfilter_estrato',
                 options=[{'label': x, 'value': x} 
                            for x in available_estrato],
                value = ['Estrato 1', 'Estrato 2'],            
                multi = True
                ),
            dcc.Dropdown(
                id='crossfilter_colen',
                 options=[{'label':x,'value':x}
                            for x in available_colen],
                value = ['OFICIAL'],
                multi = True
                ),
            dcc.Graph(
                id='graficoc'
            ),  
        ], className='six columns'),
    ]),
        html.Div(
        children=[
             html.H3(
             children='Visualización N° 1'),
             html.P("En este grafico se observa el promedio de cada una de los Factores que se evaluaron en las Pruebas Saber 11 2019 para los 5 Departamentos con mayor población de Colombia"),
        dcc.Tabs([
        dcc.Tab(label='Lectura Critica', children=[
            dcc.Graph(
                figure={
                    'data': [
                        {'x': ["ANTIOQUIA","ATLANTICO","BOGOTÁ","SANTANDER","VALLE"], 'y': [52.03, 52.33, 55.59, 55.14, 51.71],
                            'type': 'bar', 'name': 'F'},
                        {'x': ["ANTIOQUIA","ATLANTICO","BOGOTÁ","SANTANDER","VALLE"], 'y': [52.94, 51.43, 56.47, 55.77, 52.84],
                         'type': 'bar', 'name': u'M'},
                    ]
                }
            )
        ]),
        dcc.Tab(label='Matemáticas', children=[
            dcc.Graph(
                figure={
                    'data': [
                        {'x': ["ANTIOQUIA","ATLANTICO","BOGOTÁ","SANTANDER","VALLE"], 'y': [47.79, 48.83, 53.52,53.91,48.14],
                            'type': 'bar', 'name': 'F'},
                        {'x': ["ANTIOQUIA","ATLANTICO","BOGOTÁ","SANTANDER","VALLE"], 'y': [52.01, 51.18, 57.12, 57.61, 51.88],
                         'type': 'bar', 'name': u'M'},
                    ]
                }
            )
        ]),
        dcc.Tab(label='Ciencias Naturales', children=[
            dcc.Graph(
                figure={
                    'data': [
                        {'x': ["ANTIOQUIA","ATLANTICO","BOGOTÁ","SANTANDER","VALLE"], 'y': [46.04, 47.82, 51.42,51.33, 47.09],
                            'type': 'bar', 'name': 'F'},
                        {'x': ["ANTIOQUIA","ATLANTICO","BOGOTÁ","SANTANDER","VALLE"], 'y': [48.37, 48.57, 53.72,53.94,49.29],
                         'type': 'bar', 'name': u'M'},
                    ]
                }
            )
        ]),
        dcc.Tab(label='Soci. Ciudadanas', children=[
            dcc.Graph(
                figure={
                    'data': [
                        {'x': ["ANTIOQUIA","ATLANTICO","BOGOTÁ","SANTANDER","VALLE"], 'y': [45.75, 46.02, 50.19,49.22, 45.51],
                            'type': 'bar', 'name': 'F'},
                        {'x': ["ANTIOQUIA","ATLANTICO","BOGOTÁ","SANTANDER","VALLE"], 'y': [46.95, 45.04, 51.42,50.54,46.78],
                         'type': 'bar', 'name': u'M'},
                    ]
                }
            )
        ]),
        dcc.Tab(label='Inglés', children=[
            dcc.Graph(
                figure={
                    'data': [
                        {'x': ["ANTIOQUIA","ATLANTICO","BOGOTÁ","SANTANDER","VALLE"], 'y': [46.89, 49.30, 54.19,50.99, 47.40],
                            'type': 'bar', 'name': 'F'},
                        {'x': ["ANTIOQUIA","ATLANTICO","BOGOTÁ","SANTANDER","VALLE"], 'y': [49.23, 48.46, 55.57,51.98,49.35],
                         'type': 'bar', 'name': u'M'},
                    ]
                }
            )
    ]),
]),
])
])



## Viz 1
@app.callback(
    dash.dependencies.Output('Grafico_1', 'figure'),
    [dash.dependencies.Input('crossfilter_depto', 'value'),
     dash.dependencies.Input('crossfilter_depto2', 'value')]
    )

def update_graph(depto_value, mod_colegio):
    query2 = basea[basea['ESTU_DEPTO_RESIDE'].isin(depto_value)]
    query2 = query2[query2['COLE_CARACTER'].isin(mod_colegio)]
    
    query2 = pd.crosstab(query2["ESTU_DEPTO_RESIDE"],query2["COLE_CARACTER"])
    query2

    fig3 = px.imshow(query2)

    return fig3

## Viz 2

@app.callback(
    dash.dependencies.Output('example-graph-2', 'figure'),
    [dash.dependencies.Input('Valores', 'value')]
    )
def update_graph(depto_value):
    query1 = base[base["ESTU_DEPTO_RESIDE"].isin(depto_value)]
    query1 = pd.pivot_table(query1, 
                        values='PUNT_INGLES', 
                        index=['ESTU_DEPTO_RESIDE','ESTU_GENERO'],
                        aggfunc=np.mean)
    query1 = query1.reset_index().rename_axis(None, axis=1)
    query1 = query1.sort_values(by=['PUNT_INGLES'],ascending=False)

    fig2 = px.bar(query1, x='PUNT_INGLES', y='ESTU_DEPTO_RESIDE', color = 'ESTU_GENERO')
    return fig2

## Viz 3
@app.callback(
    dash.dependencies.Output('graficoc', 'figure'),
    [dash.dependencies.Input('crossfilter_estrato', 'value'),
    dash.dependencies.Input('crossfilter_colen','value')]
)
def update_graph(estrato, colegion):
    tab = basec[basec['FAMI_ESTRATOVIVIENDA'].isin(estrato)]
    tab = tab[tab['COLE_NATURALEZA'].isin(colegion)]
    
    tab = pd.crosstab(tab["FAMI_ESTRATOVIVIENDA"],tab["COLE_NATURALEZA"])

    figc = px.imshow(tab)

    return figc

if __name__ == "__main__":
    app.run_server(debug=True)


