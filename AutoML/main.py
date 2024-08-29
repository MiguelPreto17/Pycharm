from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error
import autokeras as ak
import pandas as pd

merged_data = pd.read_csv('merged_data2.csv', sep=',')

# Features e TARGET_VARIABLE
X = merged_data[[ 'Temp', 'Plus', 'Day of Week', 'Month']]
y = merged_data['Total Energy (kWh)']

# Divisão do dataset em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Inicialização do AutoML
auto_model = ak.StructuredDataRegressor(max_trials=10)  # número máximo de tentativas

# Treino do modelo AutoML
auto_model.fit(X_train, y_train, epochs=10)

# Avaliação do modelo AutoML
mse = auto_model.evaluate(X_test, y_test)
print('Erro quadrático médio do modelo AutoML:', mse)

# Fazer previsões no conjunto de teste
predictions = auto_model.predict(X_test)
print(predictions)