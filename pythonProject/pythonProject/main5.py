import os

import pandas as pd

def read_data():

    dados = pd.read_excel('input/dados_C1.xlsx', sheet_name='dados_C1')

    dias_especificos = []

   #nome = ['d1', 'd2', 'd3']

    #i = 1
    d = 1
    #m = 4
    #for dia in dias_especificos:
    for i in range(153,184):

        # Selecionar os dados para o dia específico
        dados_dia = dados.loc[dados.iloc[:, 0] == i]
        print(dados_dia)

        # Salvar os dados em um arquivo Excel com o nome do dia específico
        os.makedirs(f'output3/2023-07-{d}/c1/')
        nome_arquivo = f'output3/2023-07-{d}/c1/julho.xlsx'


        #nome_arquivo = sorted(m)
        writer = pd.ExcelWriter(nome_arquivo)
        dados_dia.to_excel(writer, sheet_name='dados_C1', index=False)
        writer.save()
        d = d + 1
        print (nome_arquivo)

    d = 1
    # m = 4
    # for dia in dias_especificos:
    for i in range(184, 215):
        # Selecionar os dados para o dia específico
        dados_dia = dados.loc[dados.iloc[:, 0] == i]
        print(dados_dia)

        # Salvar os dados em um arquivo Excel com o nome do dia específico
        os.makedirs(f'output3/2023-08-{d}/c1/')
        nome_arquivo = f'output3/2023-08-{d}/c1/agosto.xlsx'

        # nome_arquivo = sorted(m)
        writer = pd.ExcelWriter(nome_arquivo)
        dados_dia.to_excel(writer, sheet_name='dados_C1', index=False)
        writer.save()
        d = d + 1


    # m = 4
    # for dia in dias_especificos:
    """for i in range(152, 182):
        # Selecionar os dados para o dia específico
        dados_dia = dados.loc[dados.iloc[:, 0] == i]
        print(dados_dia)

        # Salvar os dados em um arquivo Excel com o nome do dia específico
        os.makedirs(f'output2/2023-06-{d}/c1/')
        nome_arquivo = f'output2/2023-06-{d}/c1/junho.xlsx'

        # nome_arquivo = sorted(m)
        writer = pd.ExcelWriter(nome_arquivo)
        dados_dia.to_excel(writer, sheet_name='dados_C1', index=False)
        writer.save()
        d = d + 1"""

read_data()
