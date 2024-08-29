from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from Function.shared import abc_instance
from Function.abc import A
from Function.teste import banana, func1
from fastapi import FastAPI, Request

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

#B = None

@app.post("/api/receive_data")
async def receive_data( table_data: list = Form(...), input_value: float = Form(...), dropdown_value: str = Form(...),
):
        # Fazer o que for necessário com os valores recebidos
        z = table_data
        b = dropdown_value
        print(A.result)
        A.result = input_value
        print(A.result)
        func1(b)
        return {"message": A.result}


@app.post("/api/abc")
async def abc(selected_option: str = Form(...),
              #input_value: float = Form(...), dropdown_value: str = Form(...)
):
        a = selected_option
        print(a)
        banana(a)
        print(A.result)
        print(A.nominal_energy)
        return {"message": f"Opção selecionada: {a}"}

@app.post("/api/teste")
async def teste():
    print("Hello")
    print (A.result)






