from fastapi import FastAPI
from fastapi import Request
from fastapi.middleware.cors import CORSMiddleware
from Function.shared import abc_instance
import tracemalloc

app = FastAPI()

# Configuração do CORS
origins = [
   "http://127.0.0.1:8050",
   "http://localhost",
   "http://localhost:8050",
]
app.add_middleware(
   CORSMiddleware,
   allow_origins=origins,
   allow_credentials=True,
   allow_methods=["*"],
   allow_headers=["*"],
)

# Rota para receber os dados do aplicativo Dash

@app.get("/api/receive_data")
async def receive_data(request: Request, input_value: float):
    # Fazer o que for necessário com os valores recebidos

    # Fazer o que for necessário com os valores recebidos
    tracemalloc.start()
    abc_instance.result = input_value
    print(abc_instance.result)

    return {"message": input_value}
