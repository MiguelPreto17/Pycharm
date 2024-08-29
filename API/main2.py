import dash
import dash_core_components as dcc
import dash_html_components as html
import requests
import dash_table


app = dash.Dash(__name__)



params = ['value CO2/kWh']

app.layout = html.Div([
    dcc.Input(id='data-input', type='number', value=''),
    dcc.RadioItems(
        id='option1',
        options=[
            {'label': 'Opção A', 'value': 'A'},
            {'label': 'Opção B', 'value': 'B'},
        ],
        value='A'
    ),
    dcc.Dropdown(
        id='dropdown',
        options=[
            {'label': 'Valor 1', 'value': 'valor1'},
            {'label': 'Valor 2', 'value': 'valor2'},
        ],
        value='valor1'
    ),

    html.Button('Enviar Dados', id='submit-button'),

    html.Div(id='data-output'),

dash_table.DataTable(
                            id='table-editing-simple',
                            columns=(
                                [{'id': 'Date', 'name': 'Date'}] +
                                [{'id': p, 'name': p} for p in params]
                            ),
                            data=[
                                dict(Model=i, **{param: 0 for param in params})
                                for i in range(1, 25)
                            ], editable = True),

])

@app.callback(
    [dash.dependencies.Output('table-editing-simple', 'data'),
     dash.dependencies.Output('data-output', 'children')],
    [dash.dependencies.Input('submit-button', 'n_clicks')],
    [dash.dependencies.State('table-editing-simple', 'data'),
     dash.dependencies.State('data-input', 'value'),
     dash.dependencies.State('option1', 'value'),
     dash.dependencies.State('dropdown', 'value')]
)



def send_data(n_clicks, table_data, input_value, selected_option, dropdown_value):
    if n_clicks:
        url1 = f"http://localhost:8000/api/receive_data"
        data1 = {
            "input_value": float(input_value),
            "dropdown_value": dropdown_value,
            "table_data": table_data
        }
        response1 = requests.post(url1, data=data1)

        url2 = f"http://localhost:8000/api/abc"
        data2 = {
            "selected_option": selected_option,
            "input_value": float(input_value),
            "dropdown_value": dropdown_value,
        }
        response2 = requests.post(url2, data=data2)

        url3 = f"http://localhost:8000/api/teste"
        data3 = {
        }
        response3 = requests.post(url3, data=data3)


        if response1.status_code == 200 and response2.status_code == 200 and response3.status_code == 200:
            return f"Resultado 1: {response1.json()['message']}, Resultado 2: {response2.json()['message']}, Resultado 3: {response3.json()['message'] }"
        else:
            return "Falha ao enviar dados"


if __name__ == '__main__':
    app.run_server(debug=True)





