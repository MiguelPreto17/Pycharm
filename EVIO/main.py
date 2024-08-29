import numpy as np
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import math

EV = pd.read_csv("EVIO_history_01-06-2022_31-05-2023.csv", sep=';')

# Convert strings to float
EV['Duration (min)'] = EV['Duration (min)'].str.replace(',', '.').astype(float)
EV['Cost incl. IVA'] = EV['Cost incl. IVA'].str.replace(',', '.').astype(float)
EV['Total Energy (kWh)'] = EV['Total Energy (kWh)'].str.replace(',', '.').astype(float)
EV['Start date'] = pd.to_datetime(EV['Start date'], format='%m/%d/%Y | %H:%M')
EV['Stop date'] = pd.to_datetime(EV['Stop date'], format='%m/%d/%Y | %H:%M')

cost = EV['Cost incl. IVA']
energy = EV['Total Energy (kWh)']
duration = EV['Duration (min)']
EV['Day of Week'] = EV['Start date'].dt.day_name()

# Criar colunas separadas para hora e minuto
EV['start_hour'] = EV['Start date'].dt.hour
EV['start_minute'] = EV['Start date'].dt.minute

# Calcular a média da duração para cada dia da semana
avg_duration = EV.groupby('Day of Week')['Duration (min)'].mean()

#Obter potencia média dos carregadores para cada dia da semana
a = (EV.groupby('Day of Week')['Duration (min)'].mean())
b = (EV.groupby('Day of Week')['Total Energy (kWh)'].mean())
Avergae_Power = (b/(a/60))

# Agrupar por dia da semana e hora/minuto
grouped = EV.groupby(['Day of Week', 'start_hour', 'start_minute'])

# Contar as ocorrências de cada hora/minuto para cada dia da semana
counts = grouped.size().reset_index(name='count')

# Encontrar o máximo para cada dia da semana
idx = counts.groupby('Day of Week')['count'].idxmax()
result = counts.loc[idx].reset_index()

result['Start Time'] = result['start_hour'].astype(str).str.zfill(2) + ':' + result['start_minute'].astype(str).str.zfill(2)

#result['New Column'] = result.apply(lambda row: EV.loc[(EV['Day of Week'] == row['Day of Week']) & (EV['start_hour'] == row['start_hour']) & (EV['start_minute'] == row['start_minute']), 'Start date'].iloc[0] + pd.Timedelta(minutes=avg_duration[row['Day of Week']]), axis=1)
result['Endtime'] = result.apply(lambda row: (EV.loc[(EV['Day of Week'] == row['Day of Week']) & (EV['start_hour'] == row['start_hour']) & (EV['start_minute'] == row['start_minute']), 'Start date'].iloc[0] + pd.Timedelta(minutes=avg_duration[row['Day of Week']])).strftime('%H:%M'), axis=1)

# Adicionar coluna da duração média
result['Average Duration'] = result.apply(lambda row: avg_duration[row['Day of Week']], axis=1)
result['Average Power'] = result.apply(lambda row: Avergae_Power[row['Day of Week']], axis=1)

# Exibir os resultados
print(result[['Day of Week', 'Start Time', 'Endtime', 'Average Duration', 'Average Power']])


# Ordenar o DataFrame por 'Day of Week', 'start_hour', 'start_minute' para garantir a ordem correta no gráfico
result = result.sort_values(['Day of Week', 'start_hour', 'start_minute'])

# Configurar a figura e os eixos
fig, ax = plt.subplots(figsize=(10, 6))

# Iterar sobre os dias da semana
for day, group in result.groupby('Day of Week'):
    # Plotar a duração de carregamento em relação à hora do dia
    ax.plot(group['Start Time'], group['Average Power'], label=day)

# Adicionar rótulos e título
ax.set_xlabel('Hora do Dia')
ax.set_ylabel('Potência Média')
ax.set_title('Duração de Carregamento por Hora do Dia para Cada Dia da Semana')

# Adicionar legenda
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

# Girar os rótulos do eixo x para melhor legibilidade
plt.xticks(rotation=45)

# Exibir o gráfico
plt.tight_layout()
plt.show()












"""# Agrupar por dia da semana e hora/minuto
grouped = EV.groupby(['Day of Week', 'Start date', 'Stop date'])

# Calcular as médias para cada grupo
result = grouped.agg({
    'Duration (min)': 'mean'
}).reset_index()


# Contar as ocorrências de cada hora/minuto para cada dia da semana
counts = grouped.size().reset_index(name='count')

# Encontrar o máximo para cada dia da semana
idx = counts.groupby('Day of Week')['count'].idxmax()
result = result.loc[idx].reset_index()


# Exibir os resultados
print(result[['Day of Week', 'Start date', 'Stop date','Duration (min)' ]])"""

"""print(result['Start date'])
print(result['Stop date'])"""










"""# Calcular a média de carregamento para cada dia da semana
average_Energy = EV.groupby('Day of Week')['Total Energy (kWh)'].mean()
# Calcular a média de carregamento para cada dia da semana
cumulative_Energy_per_day = EV.groupby('Day of Week')['Total Energy (kWh)'].cumsum()
EV['Cumulative Energy'] = cumulative_Energy_per_day


# Calcular a média de carregamento para cada dia da semana
average_charging = EV.groupby('Day of Week')['Duration (min)'].mean()
# Calcular a soma cumulativa para cada dia da semana
cumulative_duration_per_day = EV.groupby('Day of Week')['Duration (min)'].cumsum()
# Adicionar uma nova coluna ao DataFrame com a duração acumulada
EV['Cumulative Duration'] = cumulative_duration_per_day


# Definir a ordem dos dias da semana
order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
average_charging = average_charging.reindex(order)
average_Energy = average_Energy.reindex(order)



# Configurar a grade de gráficos
fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, figsize=(10, 8))


# Plotar barras para a duração acumulada por dia da semana
a = EV.groupby('Day of Week')['Cumulative Energy'].max().plot(kind='bar', color='green', ax=ax2)
b = EV.groupby('Day of Week')['Cumulative Duration'].max().plot(kind='bar', color='green', ax=ax4)


# Plotar barras para a média de carregamento por dia da semana
bars = average_charging.plot(kind='bar', color='skyblue', ax=ax3)
bars2 = average_Energy.plot(kind='bar', color='skyblue', ax=ax1)


# Adicionar os valores no topo de cada barra
for i, value in enumerate(average_Energy):
    ax1.text(i, value + 0.1, f'{value:.2f}', ha='center', va='bottom', fontsize=10, color='black')

for a in a.patches:
    ax2.annotate(f'{a.get_height():.2f}',
                (a.get_x() + a.get_width() / 2, a.get_height()),
                ha='center', va='bottom', fontsize=10, color='black')

# Adicionar os valores no topo de cada barra
for i, value in enumerate(average_charging):
    ax3.text(i, value + 0.1, f'{value:.2f}', ha='center', va='bottom', fontsize=10, color='black')

# Adicionar os valores no topo de cada barra
for b in b.patches:
    ax4.annotate(f'{b.get_height():.2f}',
                (b.get_x() + b.get_width() / 2, b.get_height()),
                ha='center', va='bottom', fontsize=10, color='black')




# Gráfico de barras para a média de carregamento
ax1.bar(average_Energy.index, average_Energy.values, color='skyblue')
ax1.set_xlabel('Dia da Semana')
ax1.set_ylabel('Média de Energia (min)')
ax1.set_title('Média de Energia por Dia da Semana')

# Gráfico de barras para a duração acumulada total
ax2.bar(EV['Start date'], cumulative_Energy_per_day, color='salmon')
ax2.set_xlabel('Data')
ax2.set_ylabel('Energia Acumulada Total (min)')
ax2.set_title('Energia Acumulada Total por Dia')
ax2.tick_params(axis='x', rotation=45)

# Gráfico de barras para a média de carregamento
ax3.bar(average_charging.index, average_charging.values, color='skyblue')
ax3.set_xlabel('Dia da Semana')
ax3.set_ylabel('Média de Carregamento (min)')
ax3.set_title('Média de Carregamento por Dia da Semana')

# Gráfico de barras para a duração acumulada total
ax4.bar(EV['Start date'], cumulative_duration_per_day, color='salmon')
ax4.set_xlabel('Data')
ax4.set_ylabel('Duração Acumulada Total (min)')
ax4.set_title('Duração Acumulada Total por Dia')
ax4.tick_params(axis='x', rotation=45)


# Ajustar o layout
plt.tight_layout()

# Exibir os gráficos
plt.show()"""







"""x = np.array(duration).reshape(-1, 1)
y = np.array(cost).reshape(-1, 1)

model = LinearRegression()
model.fit(x, y)

regression_model_mse = mean_squared_error(x, y)
print("MSE: ", math.sqrt(regression_model_mse))
print("R squared value:", model.score(x, y))

print(model.coef_[0])
print(model.intercept_[0])

plt.scatter(x,y, color='green')
plt.plot(x, model.predict(x), color='black')
plt.title('Linear Regression')
plt.xlabel('Duration (min)')
plt.ylabel('Cost incl. IVA')
plt.show()"""

#print('Predict:', model.predict([200]))






