import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html, Input, Output

# Carrega os dados e armazena corretamente em uma variável
df = pd.read_csv("./comparacao_real_expectativa.csv")

# Inicia o app
app = dash.Dash(__name__)
app.title = "Dashboard de Desempenho Acadêmico"

# Layout do dashboard
app.layout = html.Div([
    html.H1("📊 Dashboard de Desempenho Acadêmico", style={"textAlign": "center"}),

    html.Div([
        html.Label("Selecione o Aluno:"),
        dcc.Dropdown(
            id='dropdown-aluno',
            options=[{'label': f'Aluno {ra}', 'value': ra} for ra in df["RA_Aluno"].unique()],
            value=df["RA_Aluno"].unique()[0]
        ),

        html.Label("Selecione a Disciplina:"),
        dcc.Dropdown(
            id='dropdown-disciplina',
            options=[],
            value=None
        ),
    ], style={'width': '45%', 'margin': 'auto'}),

    html.Br(),

    html.Div([
        html.Div(id='indicadores', style={"display": "flex", "justifyContent": "space-around"}),
        html.Br(),
        dcc.Graph(id='grafico-desempenho'),
        html.Br(),
        dcc.Graph(id='grafico-comparacao'),
    ])
])

# Atualiza as opções da disciplina com base no aluno selecionado
@app.callback(
    Output('dropdown-disciplina', 'options'),
    Output('dropdown-disciplina', 'value'),
    Input('dropdown-aluno', 'value')
)
def atualizar_disciplinas(ra):
    df_filtrado = df[df["RA_Aluno"] == ra]
    opcoes = [{'label': str(cod), 'value': cod} for cod in df_filtrado["Cod_Disciplina"].unique()]
    valor_default = opcoes[0]["value"] if opcoes else None
    return opcoes, valor_default

# Atualiza os gráficos e indicadores
@app.callback(
    Output('grafico-desempenho', 'figure'),
    Output('grafico-comparacao', 'figure'),
    Output('indicadores', 'children'),
    Input('dropdown-aluno', 'value'),
    Input('dropdown-disciplina', 'value')
)
def atualizar_dashboard(ra, cod_disc):
    dados = df[(df["RA_Aluno"] == ra) & (df["Cod_Disciplina"] == cod_disc)].copy()
    dados.sort_values("Semestre_Label", inplace=True)

    media_real = dados[~dados["Semestre_Label"].str.contains("Previsto")]["Nota"].mean().round(2)
    media_geral = df[df["Cod_Disciplina"] == cod_disc]["Nota"].mean().round(2)

    # Protege contra erro caso não haja previsão
    nota_prevista_lista = dados[dados["Semestre_Label"].str.contains("Previsto")]["Nota"].values
    nota_prevista = nota_prevista_lista[0] if len(nota_prevista_lista) > 0 else "N/A"

    indicadores = [
        html.Div([
            html.H4("📘 Média Histórica do Aluno"),
            html.P(f"{media_real}", style={"fontSize": "22px", "color": "#0074D9"})
        ]),
        html.Div([
            html.H4("📙 Nota Prevista Próximo Semestre"),
            html.P(f"{nota_prevista}", style={"fontSize": "22px", "color": "#FF851B"})
        ]),
        html.Div([
            html.H4("📗 Média Geral da Disciplina"),
            html.P(f"{media_geral}", style={"fontSize": "22px", "color": "#2ECC40"})
        ])
    ]

    fig1 = px.line(dados, x="Semestre_Label", y="Nota",
                   title="Desempenho por Semestre",
                   markers=True, labels={"Nota": "Nota", "Semestre_Label": "Semestre"})

    fig2 = px.bar(dados, x="Semestre_Label", y="Nota",
                  title="Comparativo Real x Previsto",
                  color=dados["Semestre_Label"].str.contains("Previsto").map({True: "Previsto", False: "Real"}),
                  labels={"Nota": "Nota", "Semestre_Label": "Semestre"})

    return fig1, fig2, indicadores

# Roda o servidor
if __name__ == '__main__':
    app.run(debug=True)
